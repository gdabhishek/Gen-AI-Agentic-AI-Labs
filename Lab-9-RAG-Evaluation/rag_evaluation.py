
import json
import sys
from pathlib import Path

# Add Lab-10 directory to path to import modules
lab10_path = Path(__file__).parent.parent / "Lab-8-Customer-Support-Chatbot"
sys.path.insert(0, str(lab10_path))
import config
from vector_store_setup import get_vector_store, get_embeddings
from customer_support_chat import create_rag_chain

# Import evaluation libraries
import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from ragas.dataset_schema import EvaluationDataset
from ragas.llms import llm_factory
from typing import List, Dict
from tqdm import tqdm


from openai import OpenAI
client = OpenAI()

evaluator_llm = llm_factory("gpt-4o", client=client)
embeddings = get_embeddings() 

def load_test_cases(json_file_path: str) -> List[Dict]:
    """
    Load test cases from JSON file.
    
    Args:
        json_file_path: Path to JSON file containing test cases
        
    Returns:
        List of test case dictionaries
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)




def generate_answer_and_contexts(question: str, rag_chain, retriever) -> Dict:
    """
    Generate answer and retrieve contexts for a given question using the RAG chain.
    
    Args:
        question: The question to answer
        rag_chain: The RAG chain from Lab-10
        retriever: The retriever to get contexts
        
    Returns:
        Dictionary with 'answer' and 'contexts' keys
    """
    # Retrieve contexts
    retrieved_docs = retriever.invoke(question)
    contexts = [doc.page_content for doc in retrieved_docs]
    
    response = rag_chain.invoke({
        "input": question,
        "chat_history": []  # Empty chat history for evaluation
    })
    
    # Extract answer text
    if hasattr(response, 'content'):
        answer = response.content
    else:
        answer = str(response)
    
    return {
        "answer": answer,
        "contexts": contexts
    }


def create_ragas_dataset(test_cases: List[Dict], rag_chain, retriever) -> EvaluationDataset:
    """
    Convert test cases to RAGAS dataset format.
    Generates responses and contexts dynamically using the RAG chain.
    
    Args:
        test_cases: List of test case dictionaries with user_input, response, retrieved_contexts, reference
        rag_chain: The RAG chain from Lab-10
        retriever: The retriever to get contexts
        
    Returns:
        RAGAS EvaluationDataset ready for evaluation
    """
    print("Generating responses and contexts for each question...")
    
    user_inputs = []
    responses = []
    retrieved_contexts_list = []
    references = []
    
    for i, case in enumerate(tqdm(test_cases, desc="Processing questions")):
        user_input = case['user_input']
        reference = case['reference']
        
        # Generate answer and contexts using RAG chain
        result = generate_answer_and_contexts(user_input, rag_chain, retriever)
        
        user_inputs.append(user_input)
        responses.append(result['answer'])
        retrieved_contexts_list.append(result['contexts'])
        references.append(reference)
    
    # Prepare data in the format expected by RAGAS
    data = {
        'user_input': user_inputs,
        'response': responses,
        'retrieved_contexts': retrieved_contexts_list,
        'reference': references
    }
    
    # Create RAGAS dataset using the correct method
    dataset = Dataset.from_dict(data) # Convert dictionary to Dataset object
    return EvaluationDataset.from_hf_dataset(dataset) # Convert Dataset object to EvaluationDataset object


# ============================================================================
# Evaluation Functions
# ============================================================================

def run_ragas_evaluation(dataset: EvaluationDataset):
    """
    Run RAGAS evaluation on dataset with optional LLM evaluator.
    
    Args:
        dataset: RAGAS EvaluationDataset
        use_llm: Whether to use LLM for evaluation (default: True)
        llm_model: LLM model name if use_llm is True (default: "gpt-5-mini")
        
    Returns:
        EvaluationResult object
    """
    
   
     # Define metrics
    metrics = [
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ]
    print("\nThis may take a few minutes...\n")

    results = evaluate(dataset, metrics=metrics, llm=evaluator_llm, embeddings=embeddings)
    
    return results

def print_summary(results):
    """Print evaluation summary."""
    print("\n" + "=" * 50)
    print("RAGAS EVALUATION SUMMARY")
    print("=" * 50)
    
    scores_df = results.to_pandas()
    
    print(f"\nTotal samples evaluated: {len(scores_df)}")
    
    # Calculate mean scores for each metric
    metrics = ['faithfulness', 'answer_relevancy', 'context_precision', 'context_recall']
    
    print("\nMetric Scores:")
    for metric in metrics:
        if metric in scores_df.columns:
            mean_score = scores_df[metric].mean()
            std_score = scores_df[metric].std()
            print(f"  {metric.replace('_', ' ').title():<25}: {mean_score:.3f} (±{std_score:.3f})")
    
    print()


def print_summary_statistics(scores_df: pd.DataFrame):
    """Print summary statistics for evaluation scores."""
    print("\n" + "=" * 60)
    print("Evaluation Summary Statistics")
    print("=" * 60)
    print()
    
    # Calculate mean scores for each metric
    metrics = ['faithfulness', 'answer_relevancy', 'context_precision', 'context_recall']
    
    for metric in metrics:
        if metric in scores_df.columns:
            mean_score = scores_df[metric].mean()
            std_score = scores_df[metric].std()
            print(f"{metric.replace('_', ' ').title():<25}: {mean_score:.3f} (±{std_score:.3f})")
    
    print()
    print(f"{'Total Questions Evaluated':<25}: {len(scores_df)}")
    print()




def save_results(results, output_file: str = "ragas_evaluation_results.csv"):
    """
    Save evaluation results to CSV.
    
    Args:
        results: EvaluationResult object from RAGAS
        output_file: Output CSV file path
    """
    df = results.to_pandas()
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


def main():
    """Main function to run RAG evaluation."""
    print("=" * 60)
    print("RAG Evaluation Lab - SolarNova Dynamics Chatbot")
    print("=" * 60)
    print()
    
    try:
        # Load test cases from JSON file
        json_file_path = Path(__file__).parent / "rag_dataset.json"
        if not json_file_path.exists():
            print(f"Error: JSON file not found at {json_file_path}")
            print("Please ensure rag_dataset.json exists in the same directory.")
            sys.exit(1)
        
        print(f"Loading test cases from {json_file_path}...")
        test_cases = load_test_cases(str(json_file_path))
        print(f"Loaded {len(test_cases)} test cases.\n")
        
        # Initialize RAG chain and retriever
        print("Initializing RAG chain and retriever...")
        vector_store = get_vector_store()
        rag_chain = create_rag_chain(vector_store)
        # Create retriever separately for generating contexts
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k":2}
        )
        print("RAG chain initialized.\n")
        
        # Convert to RAGAS format (generates responses and contexts dynamically)
        print("Converting to RAGAS dataset format...")
        dataset = create_ragas_dataset(test_cases, rag_chain, retriever)
        print(f"Created dataset with {len(dataset.samples)} samples.\n")
        
        # Run evaluation with LLM
        print("Running RAGAS evaluation with LLM...")
        results_llm = run_ragas_evaluation(dataset)
        
        # Print summary
        print_summary(results_llm)
       
        # Save results
        save_results(results_llm, "ragas_evaluation_llm_results.csv")
        
        print("\n" + "=" * 50)
        print("Evaluation Complete!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\nError during evaluation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()


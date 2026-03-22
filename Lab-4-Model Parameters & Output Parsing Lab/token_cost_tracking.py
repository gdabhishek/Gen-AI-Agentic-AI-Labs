from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

try:
    from litellm import cost_per_token
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False

LITELLM_MODEL_MAP = {
    ("openai", "gpt-4o-mini"): "gpt-4o-mini",
    ("google_genai", "gemini-2.0-flash"): "gemini/gemini-2.0-flash",
    ("anthropic", "claude-haiku-4-5-20251001"): "claude-haiku-4-5-20251001",
}

def get_litellm_model(provider_name: str, model_name: str):
    """Get LiteLLM model identifier for cost calculation."""
    key = (provider_name.lower(), model_name.lower())
    if key in LITELLM_MODEL_MAP:
        return LITELLM_MODEL_MAP[key]
    # Try flexible match
    for (prov, mod), litellm_id in LITELLM_MODEL_MAP.items():
        if prov in provider_name.lower() and (mod in model_name.lower() or model_name.lower() in mod):
            return litellm_id
    return None


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    provider_name: str,
    model_name: str,
) -> tuple:
    """
    Calculate cost using LiteLLM's cost_per_token (live pricing from api.litellm.ai).

    Returns:
        (input_cost_usd, output_cost_usd, total_cost_usd) or (None, None, None) if unknown.
    """
    if not LITELLM_AVAILABLE:
        return None, None, None

    litellm_model = get_litellm_model(provider_name, model_name)
    if not litellm_model:
        return None, None, None

    try:
        input_cost, output_cost = cost_per_token(
            model=litellm_model,
            prompt_tokens=input_tokens,
            completion_tokens=output_tokens,
        )
        if input_cost is not None and output_cost is not None:
            return (float(input_cost), float(output_cost), float(input_cost + output_cost))
    except Exception:
        pass

    return None, None, None


def print_token_usage(response, provider_name: str, model_name: str) -> None:
    """Extract and print token usage and cost (via LiteLLM when available)."""
    print(f"\n{'='*60}")
    print(f"Token Usage for {provider_name} ({model_name})")
    print(f"{'='*60}")
    source = "Source: LiteLLM" if LITELLM_AVAILABLE else None

    if not hasattr(response, "usage_metadata") or not response.usage_metadata:
        print("No usage metadata available.")
        return

    usage = response.usage_metadata
    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)
    total_tokens = usage.get("total_tokens") or (input_tokens + output_tokens)

    print(f"Input Tokens:  {input_tokens}")
    print(f"Output Tokens: {output_tokens}")
    print(f"Total Tokens:  {total_tokens}")

    input_cost, output_cost, total_cost = calculate_cost(
        input_tokens, output_tokens, provider_name, model_name
    )
    if input_cost is not None:
        print(f"Input Cost:   ${input_cost:.6f}")
        print(f"Output Cost:  ${output_cost:.6f}")
        print(f"Total Cost:   ${total_cost:.6f}" + (f" ({source})" if source else ""))
    else:
        print("Cost: Unknown (model not in pricing registry)")


# --- Model setup ---
openai_llm = init_chat_model("gpt-4o-mini", model_provider="openai")
gemini_llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
anthropic_llm = init_chat_model("claude-haiku-4-5-20251001", model_provider="anthropic")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain quantum computing in 10 sentences."),
])


# --- Run inferences ---
try:
    chain = prompt | openai_llm
    openai_response = chain.invoke({})
    print(f"\nResponse (OpenAI): {openai_response.content[:150]}...")
    print_token_usage(openai_response, "openai", "gpt-4o-mini")
except Exception as e:
    print(f"Error with OpenAI: {e}")

try:
    chain = prompt | gemini_llm
    gemini_response = chain.invoke({})
    print(f"\nResponse (Gemini): {gemini_response.content[:150]}...")
    print_token_usage(gemini_response, "google_genai", "gemini-2.0-flash")
except Exception as e:
    print(f"Error with Gemini: {e}")

try:
    chain = prompt | anthropic_llm
    anthropic_response = chain.invoke({})
    print(f"\nResponse (Anthropic): {anthropic_response.content[:150]}...")
    print_token_usage(anthropic_response, "anthropic", "claude-haiku-4-5-20251001")
except Exception as e:
    print(f"Error with Anthropic: {e}")

# Lab-1: Explore Closed Source Models

This lab explores three major closed-source AI models:
- **OpenAI GPT** (via OpenAI API)
- **Anthropic Claude** (via Anthropic API)
- **Google Gemini** (via Google Generative AI API)

## Prerequisites

- Python 3.11 or higher
- API keys for the services you want to use:
  - OpenAI API key
  - Anthropic API key
  - Google API key

## Setup Instructions

### 1. Navigate to the Parent Directory

Navigate to the parent directory (one level up from the lab folder):

```bash
# If you're currently in the lab folder, go up one directory:
cd ..

# Or if you're navigating from elsewhere, use the full path:
# cd "/path/to/Gen_AI_Agentic_AI"
```

### 2. Activate Virtual Environment

```bash
# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Navigate to the Lab Directory and Install Dependencies

```bash
# Navigate to the lab folder
cd "Lab-1- Explore Closed Source Models"

# Install dependencies
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

1. Make sure you're in the lab directory, then copy the example environment file:
   ```bash
   cp .env_example .env
   ```

2. Edit the `.env` file and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   **Note:** You only need to add the API keys for the services you want to use. You can leave unused keys empty.

### 5. Getting API Keys

#### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new secret key

#### Anthropic API Key
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key

#### Google API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key

## Usage

**Important:** Before running any scripts:
1. Make sure your virtual environment is activated (from the parent directory: `source venv/bin/activate`)
2. Navigate to the lab directory: `cd "Lab-1- Explore Closed Source Models"`

### Run OpenAI Example

```bash
python explore_openai.py
```

### Run Claude Example

```bash
python explore_claude.py
```

### Run Gemini Example

```bash
python explore_gemini.py
```

## Project Structure

```
Gen_AI_Agentic_AI/
├── venv/                          # Virtual environment (created in parent directory)
└── Lab-1- Explore Closed Source Models/
    ├── explore_openai.py          # OpenAI GPT example
    ├── explore_claude.py          # Anthropic Claude example
    ├── explore_gemini.py          # Google Gemini example
    ├── .env_example               # Example environment variables file
    ├── requirements.txt           # Python dependencies
    └── README.md                  # This file
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you've activated your virtual environment and installed all dependencies with `pip install -r requirements.txt`

2. **API Key Errors**: Ensure your `.env` file is in the same directory as the Python scripts and contains valid API keys

3. **Import Errors**: Check that all packages in `requirements.txt` are properly installed

## Notes

- Make sure to keep your `.env` file secure and never commit it to version control
- The `.env` file is already in `.gitignore` (if using git) to prevent accidental commits
- API usage may incur costs depending on your usage and the service provider's pricing


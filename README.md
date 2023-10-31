# Guten-Bot

Guten-Bot is a project focused on classic book summarization and question-answering using state-of-the-art language models and natural language processing techniques. It's designed to provide concise book summaries and quick answers to questions related to books. This project is strictly based on Project Gutenberg 
>https://www.gutenberg.org/

## Features

- **Book Retrieval**: Automatically fetch books from Project Gutenberg by title.
- **Book Summarization**: Summarize classic books into shorter, more digestible versions.
- **Question-Answering (Q/A) Chatbot**: Get answers to your questions about the books you're reading.
- **Frontend Application**: An intuitive web-based interface for interacting with the system.

## Models Used

### Summarizing Model
- Model Name: `pszemraj/led-large-book-summary`
- Description: This model is used for summarizing books, providing a condensed version while maintaining key information.

### Embeddings Model
- Model Name: `hkunlp/instructor-base`
- Description: This model is used to create vector embeddings for the books, allowing for efficient book retrieval and analysis.

### Language Models (LLMs)
- Model Name: `replicate/llama-2-70b-chat`
- Description: To generate a coherent and context-aware text we are using “replicate/llama-2-70b-chat” model which is hosted in “Replicate”.  Replicate is a library of open-source models that you can access machine learning models via API calls.

## Technical Stack

- Backend Framework: Flask
- Frontend Framework: Streamlit
- Libraries: textsum Summarizer, Transformers, LangChain, Sentence Transformers, BeautifulSoup
- Deployment: 
    - Backend: Google Colab with GPU instances
    - Frontend: Localhost

## Usage

### Backend

#### Method 1

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
2. Configure `ngrok authtoken`:
    ```bash
    ngrok authtoken'....###YOUR_NGROK_TOKEN'
3. Run flask_backend.py
4. Copy and save ngrok public url
    ```bash
    example: http://73e8-35-247-9-74.ngrok-free.app

#### Method 2
1. Load Flask_Backend.ipynb notebook to your Colab with T4 GPU instance
2. Configure `ngrok` authtoken with your token
    ```bash
    ngrok authtoken'....###YOUR_NGROK_TOKEN'
3. Run all cells
4. Copy and save `ngrok public url`
    ```bash
    example: http://73e8-35-247-9-74.ngrok-free.app 

### Frontend
1. Install the required packages:

   ```bash
   pip install -r requirements.txt
2. Assign the copied `ngrok public url` in `"backend_base_url"` variable in `app.py` file
    ```bash
    backend_base_url = "....###YOUR_PUBLIC_URL"
3. Run streamlit app in Frontend directory:
    ```bash
    streamlit run app.py

## Get in Touch
For questions, feedback, or collaboration opportunities, please reach out to via email at email@gutenbot.com.

We appreciate your interest in Guten-Bot and look forward to your contributions!

Happy reading and summarizing!
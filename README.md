# Guten-Bot

Guten-Bot is a project focused on classic book summarization and question-answering using state-of-the-art language models and natural language processing techniques. It's designed to provide concise book summaries and quick answers to questions related to books. This project is strictly based on Project Gutenberg.

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
- Models: Falcon, Bloom, and more.
- Description: Various LLMs are used for the Q/A chatbot, enabling accurate answers to a wide range of questions.

## Technical Stack

- Backend Framework: Flask
- Frontend Framework: Streamlit
- Libraries: Transformers, LangChain, Sentence Transformers
- Deployment: Google Cloud Platform (GCP) with GPU instances
- Asynchronous Operations: Python `asyncio` and `httpx` for Streamlit

## Usage

### Backend

1. Install the required packages:
   ```bash
   pip install -r requirements.txt


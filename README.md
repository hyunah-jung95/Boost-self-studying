# Boost Self-Studying

## TL;DR
This web application simplifies studying by providing clear and practical explanations of topics based on your uploaded studying documents and Wikipedia. If you’re struggling with complex materials, this app helps break them down into easy-to-understand explanations.

## How It Works

### 1. Embedding

- Upload your studying document, and the app splits it into smaller chunks optimized for embedding.
- Texts are embedded using the Vertex AI embedding model: text-embedding-004.
- Cached embedded data and uploaded files improve processing speed and reduce API costs.

### 2. Retrieve

- Combines data retrieval from your embedded documents and Wikipedia.
- Provides precise and descriptive information about the topics you are studying.

### 3. Explain

- Delivers detailed explanations about the topics in your documents, making it easier to understand and apply.

## How to Run Locally
```
pip install -r requirements.txt
streamlit run main.py
```
## Features

- Document Upload: Supports uploading study documents for detailed analysis.
- Wikipedia Integration: Enriches explanations with reliable information.
- Caching: Speeds up repeated queries by storing embeddings and processed files.

## Future Enhancements

- Customize for User’s Studying Topics
- Improved UI for Topic Navigation
- Integrate Cloud Database and Public Deployment

Feel free to suggest new features or report issues by opening an issue on GitHub.

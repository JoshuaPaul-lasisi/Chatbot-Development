# Customer Service Chatbot

This project is a customer service chatbot built using natural language processing (NLP) techniques. The chatbot classifies customer intents and generates appropriate responses based on the text inputs.

## Project Structure

- **data/**: Contains the raw dataset for customer interactions.
- **models/**: Contains the trained intent classification model.
- **scripts/**: Python scripts for data preprocessing, intent classification, and response generation.
- **app/**: Contains the Streamlit app for deployment and frontend files (CSS, JS).
- **notebooks/**: Jupyter notebooks for data exploration and model development.
- **requirements.txt**: List of dependencies.
- **README.md**: Overview of the project.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Preprocess data and train the model by running scripts in `scripts/`.
3. Start the Streamlit app: `streamlit run app/main.py`

## Deployment

The chatbot is deployed using Streamlit. It offers an interactive frontend where users can type messages, and the chatbot responds accordingly.
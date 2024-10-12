import pandas as pd
import re

def load_data(file_path):
    # Load the data from a CSV file
    return pd.read_csv(file_path)

def clean_text(text):
    # Clean the 'Text' column for NLP
    text = re.sub(r'\W', ' ', str(text))
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def preprocess_data(df):
    # Handle missing values
    df['Geo'].fillna('Unknown', inplace=True)
    df['Customer Comment'].fillna('', inplace=True)
    
    # Clean text for NLP
    df['cleaned_text'] = df['Text'].apply(clean_text)
    return df

if __name__ == "__main__":
    data = load_data('../data/chat.csv')
    clean_data = preprocess_data(data)
    clean_data.to_csv('../data/clean_chat.csv', index=False)
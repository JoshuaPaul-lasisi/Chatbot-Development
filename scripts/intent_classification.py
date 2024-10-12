import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_model(data_path):
    # Load preprocessed data
    data = pd.read_csv(data_path)
    
    # Define features and labels
    X = data['cleaned_text']
    y = data['intent_label']  # Assuming intents have been labeled
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vectorize the text data
    vectorizer = TfidfVectorizer(max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train the Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    # Save model and vectorizer to disk
    with open('../models/intent_classifier.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)

if __name__ == "__main__":
    train_model('../data/clean_chat.csv')
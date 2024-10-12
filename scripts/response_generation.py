# Define responses for intents
responses = {
    "Inquiry": "Thank you for your question! Our support team will get back to you soon.",
    "Complaint": "We apologize for the inconvenience. We're investigating your issue.",
    "Feedback": "Thank you for your feedback! We're glad to hear from you.",
    "Request": "Your request has been received. We'll get back to you shortly."
}

def get_response(intent):
    return responses.get(intent, "I'm sorry, I didn't understand that.")
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Define FAQs (Question-Answer Pairs)
faq_data = {
"What is your name?": "I am an AI-powered FAQ chatbot."
    ,
"How does this chatbot work?": "I use NLP techniques to understand your queries and provide relevant answers."
    ,
"What technologies do you use?": "I use Python, NLTK, and SpaCy for natural language processing."
    ,
"Can you answer all questions?": "I can answer predefined FAQs. If I don't understand a question, I will ask for clarification."
    ,
"Who developed you?": "I was developed as a demo for FAQ-based chatbot applications."
}

# Function to preprocess user input
def preprocess_text(text):
    text = text.lower()
           tokens = word_tokenize(text)
                    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words("english")]
                             return tokens

# Function to match user input with FAQs
                                    def get_response(user_input):
                                    user_tokens = preprocess_text(user_input)
                                            for question, answer in faq_data.items():
                                                question_tokens = preprocess_text(question)
                                                        common_words = set(user_tokens) & set(question_tokens)
                                                        if len(common_words) > 1:
# Matching threshold
                                                                    return answer
                                                                            return "I'm not sure about that. Can you rephrase your question?"

# Main chatbot loop
                                                                                    def chatbot():
                                                                                    print("Chatbot: Hello! Ask me an FAQ or type 'exit' to quit.")
                                                                        while True:
                                                                                    user_input = input("You: ")
                                                                                if user_input.lower() == "exit":
                                                                                                    print("Chatbot: Goodbye!")
                                                                                                    break
                                                                                                    response = get_response(user_input)
                                                                                                            print(f"Chatbot: {response}")

# Run the chatbot
                                                                                        if __name__ == "__main__":
                                                                                                            chatbot()

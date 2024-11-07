import nltk
import spacy
from nltk.chat.util import Chat, reflections


nlp = spacy.load("en_core_web_sm")

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! And you?"]
    ],
    [
        r"are you a robot?",
        ["Yes, I am a robot here to assist you with any questions!"]
    ],
    [
        r"tell me a joke", 
        ["I told my wife she was drawing her eyebrows too high.She looked surprised!"]  
    ],
    [
        r"it was funny",
        ["thank you,do you want to kmow anything more!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ]
]


def analyze_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to run the chatbot
def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ")

        
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a nice day!")
            break

    
        entities = analyze_text(user_input)
        if entities:
            entity_list = ', '.join([f"{ent[0]} ({ent[1]})" for ent in entities])
            print(f"Chatbot: I noticed you mentioned these entities: {entity_list}")

        
        response = chat.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm not sure how to respond to that.")


if __name__ == "__main__":
    chatbot()

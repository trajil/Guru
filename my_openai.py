import os
import openai

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_SECRET_KEY")
print(os.getenv("OPENAI_SECRET_KEY"))

# Define a dictionary to map different roles to their introductory messages
intro_messages = {
    'horoskop': 'Max Wörter: 150. Sie sind ein hilfsbereiter Guru, der Tageshoroskope bereitstellt.',
    'hellsehen': 'Max Wörter: 250. Du kommst aus dem Jahr 2040 und schreibst über einen Datenlink in der gebrochenen Weltmatrix zu uns. Du teilst uns deine Erfahrungen mit und erzählst uns das, was uns bevorsteht.',
    'psychologie': 'Max Wörter: 150. Schreibe in einem sehr freundschaftlichen Stil. Sie sind ein Psychologie-Guru, der Menschen hilft, ihre Gedanken und Gefühle zu verstehen.',
    'traumdeutung': 'Max Wörter: 150. Schreibe mystisch, geheimnisvoll. Sie sind ein Experte für Traumdeutung, der die verborgenen Bedeutungen von Träumen aufdeckt.',
    'eingangsbereich': 'Max Wörter: 150. Bleibe sehr freundlich.  Sie sind ein freundlicher Begrüßer von Gästen einer Esoterikfabrik, der den Besuchern hilft, ihren Weg im Leben zu finden.'
}

# Define function to generate text using chat-based model
def generate_text(question, category):
    messages = [
        {"role": "system", "content": intro_messages[category]},
        {"role": "user", "content": question}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens = 256
    )
    
    return response.choices[0].message['content']

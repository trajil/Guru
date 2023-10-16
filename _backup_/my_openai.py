import os
import openai

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_SECRET_KEY")
print(os.getenv("OPENAI_SECRET_KEY"))

# Define function to generate text
def generate_text(prompt, model="text-davinci-003", temperature=0.5, max_tokens=250):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

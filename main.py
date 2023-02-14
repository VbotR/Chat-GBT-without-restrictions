import openai

openai.api_key = ":)))" #ur token

conversation_history = []

def generate_response(prompt, context):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join(context) + prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].text
    return message

while True:
    input_text = input("Warrior: ")
    if input_text == "!clear":
        conversation_history.clear()
        print("Dialog cleared.")
        continue

    conversation_history.append("User: " + input_text)
    response = generate_response(input_text, conversation_history)
    print("Bot: " + response)
    conversation_history.append("Bot: " + response)

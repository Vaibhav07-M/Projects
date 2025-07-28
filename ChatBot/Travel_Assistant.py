from openai import OpenAI


client = OpenAI(
    api_key = "Your-API-Key-Here",
    base_url = "https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Exiting the chat.")
        break
    
    response = client.chat.completions.create(
        model = "llama3-70b-8192",
        messages = [
            {"role": "system", "content": "You are a travel-focused assistant. Also include the exact location of the place if you are recommending something. If asked anything unrelated to tourism, you politely decline and redirect back to travel-related topics."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content,"\n")
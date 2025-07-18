from openai import OpenAI

client = OpenAI(api_key="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" 
)

print("🤖 PyBot: Ask me anything (type 'bye' to exit)")
print("---------------------------------------------")

while True:
    user = input("user: ")

    if user.lower() == "bye":
        print("chatBot: See you later!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user}
            ]
        )

        reply = response.choices[0].message.content
        print(" chatbot:", reply)
        print("---------------------------------------------")

    except Exception as e:
        print("Error:", str(e))
        break

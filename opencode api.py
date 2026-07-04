from openai import OpenAI

# Initialize the client correctly
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Use the correct chat completions endpoint and a valid model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Highly capable and cost-effective model
    messages=[
        {"role": "user", "content": "Write a short bedtime story about a unicorn."}
    ]
)

# Access the generated text properly
print(response.choices[0].message.content)
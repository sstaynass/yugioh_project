import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
prompt_text = "Here is my Yugioh deck: \n\n[deck]"

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt_text,
  temperature=0.7,
  max_tokens=500
)

print(prompt_text + response['choices'][0]['text'])


# export OPENAI_API_KEY='YOUR_API_KEY_HERE'
# export TWILIO_ACCOUNT_SID='YOUR_ACCOUNT_SID'
# export TWILIO_AUTH_TOKEN='YOUR_AUTH_TOKEN'
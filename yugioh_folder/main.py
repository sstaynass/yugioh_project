import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')
print(os.environ.get('OPENAI_API_KEY'))
prompt_text = 'Here is my Yugioh deck: \n\n[deck]'

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.7,
    max_tokens=300,
    presence_penalty=0.3
)

resp_text = response['choices'][0]['text']

if '[/deck]' in resp_text:
    message_body = resp_text[:resp_text.lower().find('[/deck]')]
else:
    # If it doesn't get to the end of a deck, cut off after the last newline.
    message_body = resp_text[:resp_text.rfind('\n')]

print(message_body)
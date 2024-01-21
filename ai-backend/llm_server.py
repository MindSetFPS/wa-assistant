from outlines import models, generate
from flask import Flask, request
import json
import time
from propmt_templates.prompt import generate_prompts

from conversations import conversations, createConversation, findConversation, getLastMessage

def calculate_time():
    start = time.time()
    end = time.time()
    return end - start

app = Flask(__name__)

# models = [
#     "TheBloke/Mistral-7B-OpenOrca-AWQ",
#       "TheBloke/openchat-3.5-0106-AWQ",
        # "openhermes-2.5-mistral-7b-16k" very recomended by internet people
# ]

model = models.transformers("TheBloke/OpenHermes-2.5-Mistral-7B-16k-AWQ", device="cuda")

# lista de mensajes del usuario
# conversation = []

@app.route("/prompt", methods=['POST'])
def new_prompt():
    data = request.get_json()
    print(data)
    
    max_tokens = int(data['max_tokens'])
    prompt = data["prompt"]
    message_from = data["from"]
    generator = generate.text(model, max_tokens=max_tokens)

    conversation = findConversation(message_from, prompt)
    result = generator(generate_prompts(conversation))

    # append bot response to conversation
    findConversation(message_from, result)

    return json.dumps({ 
        "ok":"true",
        "time" : calculate_time(),
        "answer" : result
    })


# Todo: make a function to clear context

# flask --app llm_server run --host=0.0.0.0 --port=7860

# Instruction templates
# https://github.com/oobabooga/text-generation-webui/blob/d8c3a5bee814f09b0868474002105dcf21a3ff1a/instruction-templates/Vicuna-v0.yaml#L4
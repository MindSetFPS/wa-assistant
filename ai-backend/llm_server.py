from outlines import models, generate
from flask import Flask, request
from flask_cors import CORS
import json
import time
from prompt_templates.prompt import generate_prompts, generate_prompts_pygmalion

from conversations import bot

def calculate_time():
    start = time.time()
    end = time.time()
    return end - start

app = Flask(__name__)
CORS(app)

# models = [
#     "TheBloke/Mistral-7B-OpenOrca-AWQ",
#       "TheBloke/openchat-3.5-0106-AWQ",
        # "TheBloke/OpenHermes-2.5-Mistral-7B-16k-AWQ" very recomended by internet people
        # "TheBloke/Pygmalion-2-7B-AWQ" Roleplay AI  
        #TheBloke/WizardLM-13B-V1.2-AWQ    
# ]

model = models.transformers("TheBloke/Mistral-7B-OpenOrca-AWQ", device="cuda")

@app.route("/prompt", methods=['POST'])
def new_prompt():
    data = request.get_json()
    max_tokens = int(data['max_tokens'])
    prompt = data["prompt"]
    message_from = data["from"]
    generator = generate.text(model, max_tokens=max_tokens)
    # generator_selection = generate.choice(model, ["Tacos", "Pizza", "Puchero", "No tengo eso"])

    index = bot.getConversationIndex(message_from=message_from)
    
    if index is None:
        conversation = bot.createConversation(message_from=message_from, prompt=prompt)

    if index is not None:
        conversation = bot.conversations[index]
        conversation.addMessage(prompt=prompt, from_name=message_from)

    generated_prompt = generate_prompts(conversation.history)
    result = generator(generated_prompt)
    conversation.addMessage(prompt=result, from_name="Bot")

    # append bot response to conversation
    return json.dumps({ 
        "ok":"true",
        "time" : calculate_time(),
        "answer" : result,
        "conversation" : generated_prompt
    })

@app.route("/delete-conversation", methods=['POST'])
def delete_conversation():
    data = request.get_json()

    message_from = data["from"]

    conversation = bot.getConversation(message_from=message_from)

    if conversation is not None:
        conversation.restartContext()

    return json.dumps({
        "ok": "true",
        "time": calculate_time(),
    })

@app.route("/update-context", methods=['POST'])
def edit_context():
    data = request.get_json()

    newContext = data["newContext"]
    bot.prompt = newContext
    return json.dumps({
        "ok": "true",
        "time": calculate_time(),
        "newContext": bot.prompt
    })

@app.route("/get-context", methods=['POST'])
def get_context():
    data = request.get_json()
    return json.dumps({
        "ok": "true",
        "context": bot.prompt
    })

# flask --app llm_server run --host=0.0.0.0 --port=7860

# Instruction templates
# https://github.com/oobabooga/text-generation-webui/blob/d8c3a5bee814f09b0868474002105dcf21a3ff1a/instruction-templates/Vicuna-v0.yaml#L4
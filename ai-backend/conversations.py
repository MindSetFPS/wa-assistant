import pprint

bot = {
    "base_prompt": "Estas por responder una conversacion. Vas a responder preguntas de forma precisa, dar recomendacion y ayudar con el proceso de toma de decisiones. Seguiras las peticiones al pie de la letra. Piensa de forma creativa. Sé amable.",
    "conversations": [
        {
            'from': 'bricel',
            'history': []
        }
    ]
}

def addMessageToConversation(message_from, prompt) -> list:
    index = getConversationIndex(message_from=message_from)
    if index is not None:
        saveLastMessageToHistory(index, prompt)
    
    if index is None:
        index = createConversation(message_from, prompt)

    pprint.pprint(bot["conversations"], width=120)
    return getConversationHistory(index)

def restartConversationContext(message_from: str):
    index = getConversationIndex(message_from=message_from)
    if(len(bot["conversations"]) > 0 and index is not None):
        bot["conversations"].pop(index)

def getConversationIndex(message_from: str):
    return next(
        (index for (index, conversation) in enumerate(bot["conversations"]) if conversation["from"] == message_from), None
    )

def getLastMessage(index):
    return bot["conversations"][index]["last_prompt"]

def saveLastMessageToHistory(index, message):
    bot["conversations"][index]["history"].append(message)

def getConversationHistory(index) -> list:
    return bot["conversations"][index]["history"]

def createConversation(message_from, prompt):
    bot["conversations"].append({
        'from': message_from,
        'history': [prompt]
    })
    return len(bot["conversations"]) -1

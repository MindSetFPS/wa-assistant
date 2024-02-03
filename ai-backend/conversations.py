import pprint

bot = {
    "base_prompt": """Eres un bot de deteccion de patrones. 
    Seguiras la suiguiente instruccion: 
    A continuacion recibiras el texto te una persona que quiere una comida. 
    Responde con la comida que quiere la persona, si dice menciona "pizza" responde pizza.
    Si menciona "puchero" responde puchero.
    Si menciona "tacos" responde tacos.
    Si menciona algo relacionado a dicha comida, intenta responder lo que creas correcto.
       A continuacion te doy unos ejemplos: 
    
    user: hola quiero unos tacos 
    assistant: tacos  
    que: pizzas tiene?
    assistant: pizza
    user: buenos dias, le quedan puchero? 
    assistant: puchero""",
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

def getConversationHistory(index, message_from="") -> list:
    if index is not None:
        return bot["conversations"][index]["history"]
        # saveLastMessageToHistory(index, prompt)
    
    if index is None:
        index = createConversation(message_from, "")
        return bot["conversations"][index]["history"]

def createConversation(message_from, prompt):
    bot["conversations"].append({
        'from': message_from,
        'history': [prompt]
    })
    return len(bot["conversations"]) -1

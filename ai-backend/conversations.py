import pprint

conversations = [
    {
        'from': 'bricel',
        'history': []
    }
]

def findConversation(message_from, prompt) -> list:
    index = next(
        (index for (index, conversation) in enumerate(conversations) if conversation["from"] == message_from), None
    )
    if index is not None:
        saveLastMessageToHistory(index, prompt)
    
    if index is None:
        index = createConversation(message_from, prompt)

    pprint.pprint(conversations, width=120)
    return getConversationHistory(index)
    

def getLastMessage(index):
    return conversations[index]["last_prompt"]

def saveLastMessageToHistory(index, message):
    conversations[index]["history"].append(message)

def getConversationHistory(index) -> list:
    return conversations[index]["history"]

def createConversation(message_from, prompt):
    conversations.append({
        'from': message_from,
        'history': [prompt]
    })

    return len(conversations) -1

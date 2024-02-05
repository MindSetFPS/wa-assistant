from typing import List

class Message:
    def __init__(self, message: str, owner: str) -> None:
        self.message = message
        self.owner = owner

    owner: str
    message: str

class Conversation:
    def __init__(self, from_name: str) -> None:
        self.from_name = from_name
        self.history = []

    from_name: str
    history: List[Message]

    def addMessage(self, prompt, from_name) -> list:
        self.history.append(Message(message=prompt, owner=from_name))

    def restartContext(self):
        self.history = []

    def getLastMessage(self):
        last_message = len(self.history)
        return self.history[last_message]

    def getHistory(self) -> list:
        return self.history

class Bot:
    def __init__(self) -> None:
        pass

    prompt: str = "Eres un agente de atencion a cliente. Tu deber es ayudar a la gente en su proceso de compra. Siempre responderás a todas las preguntas que se te hagan. Eres respetuoso e inteligente. Piensas fuera de la caja."
    conversations: List[Conversation] = []
    
    def getConversationIndex(self, message_from: str):
        return next(
            (index for (index, conversation) in enumerate(self.conversations) if conversation.from_name == message_from), None
        )
    
    def getConversation(self, message_from: str) -> Conversation:

        return next(
            (conversation for (index, conversation) in enumerate(self.conversations) if conversation.from_name == message_from), None
        )


    def createConversation(self, message_from, prompt) -> Conversation:
        
        conversation = Conversation(from_name=message_from)
        conversation.addMessage(prompt=prompt, from_name=message_from)
        
        self.conversations.append(conversation)

        return conversation
bot = Bot()

# bot = {
#     "base_prompt": """Eres un bot de deteccion de patrones. 
#     Seguiras la suiguiente instruccion: 
#     A continuacion recibiras el texto te una persona que quiere una comida. 
#     Responde con la comida que quiere la persona, si dice menciona "pizza" responde pizza.
#     Si menciona "puchero" responde puchero.
#     Si menciona "tacos" responde tacos.
#     Si menciona algo relacionado a dicha comida, intenta responder lo que creas correcto.
#        A continuacion te doy unos ejemplos: 
    
#     user: hola quiero unos tacos 
#     assistant: tacos  
#     que: pizzas tiene?
#     assistant: pizza
#     user: buenos dias, le quedan puchero? 
#     assistant: puchero""",
#     "conversations": [
#         {
#             'from': 'bricel',
#             'history': []
#         }
#     ]
# }
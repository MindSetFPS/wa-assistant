from conversations import bot, Conversation, Message
from typing import List
from pprint import pprint
# Helped me understand Prompt Templating:
# https://huggingface.co/blog/llama2
# https://huggingface.co/docs/transformers/main/chat_templating
# https://github.com/liltom-eth/llama2-webui
# https://github.com/thisserand/llama2_local/blob/main/llama_chat_format.py

def generate_prompts(message_history: List[Message]):
    system_message = bot.prompt
    PROMPT_TEMPLATE = f"""
    <|im_start|>system
    {system_message}<|im_end|>
    """
    ASSISTANT_TEMPLATE = f"""
    <|im_start|>assistant
    """
    FINAL_PROMPT = PROMPT_TEMPLATE
    
    # PROMPT_TEMPLATE + USER_TEMPLATE + ASSISTANT_TEMPLATE

    for i, message in enumerate(message_history):
       if message.owner != "System" and message.owner != "Bot":
        response = f"""
            <|im_start|>user
            {message.message}<|im_end|>
            """
       if message.owner == "Bot":
            response = f"""
            <|im_start|>assistant
            {message.message}<|im_end|>
            """
        
       FINAL_PROMPT = FINAL_PROMPT + response
       print(FINAL_PROMPT + ASSISTANT_TEMPLATE)

    return FINAL_PROMPT + ASSISTANT_TEMPLATE

def generate_prompts_pygmalion(prompt: list):
    system_message = "<|system|>Enter RP mode. Pretend to be Maria whose persona follows: Daniel \nYou shall reply to the user while staying in character, and generate long responses. Maria is a young 20 year old who has recently come to the city and wants to have fun and maybe get a boyfriend. The place is a bar, with vodka and tekila."
    PROMPT_TEMPLATE = f"""
    <|system|>system
    {system_message}<|im_end|>
    """
    ASSISTANT_TEMPLATE = f"""
    <|model|>assistant
    """
    FINAL_PROMPT = PROMPT_TEMPLATE
    
    # PROMPT_TEMPLATE + USER_TEMPLATE + ASSISTANT_TEMPLATE

    for i, message in enumerate(prompt):
    #    print(f"{i+1}:{message}")
       if (i+1)%2 == 1:
        response = f"""
            <|user|>user
            {message}<|im_end|>
            """
       else:
            response = f"""
            <|model|>assistant
            {message}<|im_end|>
            """
        
       FINAL_PROMPT = FINAL_PROMPT + response

    return FINAL_PROMPT + ASSISTANT_TEMPLATE



# print(generate_prompts("Hola, cuales son los planetas del sistema solar?"))






# LLAMA EXAMPLE 2

BOS, EOS = "<s>", "</s>"
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

def format_to_llama_chat_style(history) -> str:
    # history has the following structure:
    # - dialogs
    # --- instruction
    # --- response (None for the most recent dialog)
    prompt = ""
    for i, dialog in enumerate(history[:-1]):
      instruction, response = dialog[0], dialog[1]
      # prepend system instruction before first instruction
      if i == 0:
        instruction = f"{B_SYS}{DEFAULT_SYSTEM_PROMPT}{E_SYS}" + instruction
      else:
        # the tokenizer automatically adds a bos_token during encoding,
        # for this reason the bos_token is not added for the first instruction
        prompt += BOS
      prompt += f"{B_INST} {instruction.strip()} {E_INST} {response.strip()} " + EOS

    # new instruction from the user
    new_instruction = history[-1][0].strip()

    # the tokenizer automatically adds a bos_token during encoding,
    # for this reason the bos_token is not added for the first instruction
    if len(history) > 1:
      prompt += BOS
    else:
      # prepend system instruction before first instruction
      new_instruction = f"{B_SYS}{DEFAULT_SYSTEM_PROMPT}{E_SYS}" + new_instruction

    prompt += f"{B_INST} {new_instruction} {E_INST}"
    return prompt








# LLAMA EXAMPLE

# B_INST, E_INST = "[INST]", "[/INST]"
# B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

# class Message(TypedDict):
#     role: Literal["assistant", "user", "system"]
#     content: str
#     user: NotRequired[str]

# def get_prompt_for_dialog(dialog: List[Message]) -> str:
#     """Process dialog (chat history) to llama2 prompt for
#     OpenAI compatible API /v1/chat/completions.

#     Examples:
#         >>> dialog = [
#                 {
#                     "role":"system",
#                     "content":"You are a helpful, respectful and honest assistant. "
#                 },{
#                     "role":"user",
#                     "content":"Hi do you know Pytorch?",
#                 },
#             ]
#         >>> prompt = get_prompt_for_dialog("Hi do you know Pytorch?")

#     Args:
#         dialog: The dialog (chat history) to generate text from.

#     Yields:
#         prompt string.
#     """
#     # add "<<SYS>>\n{system_prompt}\n<</SYS>>\n\n" in first dialog
#     if dialog[0]["role"] == "system":
#         dialog = [
#             {
#                 "role": dialog[1]["role"],
#                 "content": B_SYS + dialog[0]["content"] + E_SYS + dialog[1]["content"],
#             }
#         ] + dialog[2:]
#     # check roles
#     assert all([msg["role"] == "user" for msg in dialog[::2]]) and all(
#         [msg["role"] == "assistant" for msg in dialog[1::2]]
#     ), (
#         "model only supports 'system', 'user' and 'assistant' roles, "
#         "starting with 'system', then 'user' and alternating (u/a/u/a/u...)"
#     )
#     # add chat history
#     texts = []
#     for prompt, answer in zip(
#         dialog[::2],
#         dialog[1::2],
#     ):
#         texts.append(
#             f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} "
#         )
#     # check last message if role is user, then add it to prompt text
#     assert (
#         dialog[-1]["role"] == "user"
#     ), f"Last message must be from user, got {dialog[-1]['role']}"
#     texts.append(f"{B_INST} {(dialog[-1]['content']).strip()} {E_INST}")
#     return "".join(texts)

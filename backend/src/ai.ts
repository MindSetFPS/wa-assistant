import { LlamaModel, LlamaContext, LlamaChatSession } from 'node-llama-cpp'
import path from 'path'
import { fileURLToPath } from "url"
import MyCustomChatPromptWrapper from './chatwrapper.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
console.log(path.join(__dirname, '..', "models", "llama-2-7b-chat.Q4_K_M.gguf"))

const model = new LlamaModel({
    modelPath: path.join(__dirname, '..', "models", "llama-2-7b-chat.Q4_K_M.gguf")
})
const context = new LlamaContext({ model })
const session = new LlamaChatSession({
    context,
    promptWrapper: new MyCustomChatPromptWrapper(),
    systemPrompt: 'Eres un agente de servicio a cliente.'
})

export { model, context, session }
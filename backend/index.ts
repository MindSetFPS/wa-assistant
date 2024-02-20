// const qrcode = require('qrcode-terminal');
// const { Client, LocalAuth } = require('whatsapp-web.js');
import Whatsapp from 'whatsapp-web.js'
const { Client, LocalAuth } = Whatsapp
import { createClient } from '@supabase/supabase-js'
import { LlamaModel, LlamaContext, LlamaChatSession } from 'node-llama-cpp'
import { fileURLToPath } from "url"
import path from 'path'
import MyCustomChatPromptWrapper from './chatwrapper.js'
import dotenv from 'dotenv'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
dotenv.config()

console.log(path.join(__dirname, '..', "models", "llama-2-7b-chat.Q4_K_M.gguf"))

const supabase = createClient(process.env.PUBLIC_SUPABASE_URL!, process.env.PUBLIC_SUPABASE_API_KEY!)

const model = new LlamaModel({
    modelPath: path.join(__dirname, '..', "models", "llama-2-7b-chat.Q4_K_M.gguf")
})
const context = new LlamaContext({ model })
const session = new LlamaChatSession({
    context,
    promptWrapper: new MyCustomChatPromptWrapper(),
    systemPrompt: 'Eres un agente de servicio a cliente.'
})

async function getConversation(message_from: string) {
    const { data, error } = await supabase
        .from('conversations')
        .select('messages')
        .eq('customer_id', message_from)
        .single()

    if (data) {
        return data.messages
    }
    if (error) {
        console.log(error)
    }
}

const client = new Client({
    authStrategy: new LocalAuth(),
    // Only required if its running inside a container
    // puppeteer: {
    //    args: ['--no-sandbox', '--disable-setuid-sandbox'],   
    // } 
});

// client.on('qr', qr => {
//     qrcode.generate(qr, { small: true });
// });

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message', async message => {
    console.log('Incoming message: ' + message.body + ' from ' + message.from)

    let conversation = await getConversation(message.from)

    if (conversation === undefined) {
        conversation = []
    }

    conversation.push({
        role: 'user',
        content: message.body
    })

    const r = await session.prompt(message.body)

    let outgoingMessage = r;
    console.log("Outgoing message: " + outgoingMessage)
    conversation.push(r)
    message.reply(r);

    console.log(session)
    const { data, error } = await supabase
        .from('conversations')
        .upsert([
            {
                customer_id: message.from,
                messages: conversation,
                customer: message.from,
                isBussiness: false,
                role: 'user',
                business_id: "52bd211b-f1f3-42ab-aa93-e24ac6185952"
            },
        ])
        .select()

    if (error) {
        console.log(error)
    }
});

client.initialize();

// export default client
// Generate QR image https://www.npmjs.com/package/qr-image
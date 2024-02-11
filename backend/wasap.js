// const qrcode = require('qrcode-terminal');
// const { Client, LocalAuth } = require('whatsapp-web.js');
import Whatsapp from 'whatsapp-web.js'
const { Client, LocalAuth } = Whatsapp
import ollama from 'ollama';
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(process.env.PROJECT_URL, process.env.SERVICE_KEY)

async function getConversation(message_from) {
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
// ollama.list()
// .then((a) =>
//     console.log(a)
// )

const client = new Client({
    authStrategy: new LocalAuth(),
    // Only required if its running inside a container
    // puppeteer: {
    //    args: ['--no-sandbox', '--disable-setuid-sandbox'],   
    // } 
});

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});


client.on('message', async message => {
    console.log('Incoming message: ' + message.body + ' from ' + message.from + message.notifyName)

    let conversation = await getConversation(message.from)

    if(conversation === undefined){
        conversation = []
    }

    conversation.push({
        role: 'user',
        content: message.body
    })

    let r = await ollama.chat({
        model: "mistral-openorca:7b-q4_K_M",
        messages: conversation,
        stream: false
    })

    conversation.push(r.message)
    message.reply(r.message.content);

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
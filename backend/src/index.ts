// const qrcode = require('qrcode-terminal');
// const { Client, LocalAuth } = require('whatsapp-web.js');
import Whatsapp from 'whatsapp-web.js'
const { Client, LocalAuth } = Whatsapp
import { model, context, session } from './ai.js'
import { supabase, getConversation } from './supa.js'

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
    if (conversation === undefined) { conversation = [] }

    conversation.push({
        role: 'user',
        content: message.body
    })

    const outgoingMessage = await session.prompt(message.body)

    console.log("Outgoing message: " + outgoingMessage)
    conversation.push(outgoingMessage)
    message.reply(outgoingMessage);

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
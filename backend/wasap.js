// const qrcode = require('qrcode-terminal');
// const { Client, LocalAuth } = require('whatsapp-web.js');
import Whatsapp from 'whatsapp-web.js'
const { Client, LocalAuth} = Whatsapp
import askAI from './api.js';

const client = new Client({
        authStrategy: new LocalAuth(),
        // Only required if its running inside a container
        // puppeteer: {
        //    args: ['--no-sandbox', '--disable-setuid-sandbox'],   
        // } 
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message', message => {
        console.log('Incoming message: ' + message.body + ' from ' + message.author)
        console.log(message)
        askAI(message)
        .then((answer) => {
            console.log(answer)
            message.reply(answer);
        })
});

client.initialize();
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
        askAI('Eres un adolescente que le gusta hablar con sus amigos de latinoamerica, puedes conversar en español y eres un poco sarcastico y conciso, directo al grano.', message.body)
        .then((answer) => {
            console.log(answer)
            message.reply(answer);
        })
});

client.initialize();
<script lang="ts">
	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';
	import ChatTextInput from '../../components/chatTextInput.svelte';
	import ChatTopBar from '../../components/chatTopBar.svelte';
	import API_URL from '$lib/constants';

	type owner = "Bot" | "System" | string;
	interface Message {
		owner: owner,
		text: string
	}
	
	let chatHistory: Message[] = [];
	let hidden = false;
	let user: owner = "9999071819"
	let context: string;
	let newContext: string;
	
	function handleNewMessage(a){
		console.log(a)
		let newMessage: Message = {
			owner: user,
			text: a.detail.prompt
		}
		addMessage(newMessage)
	}
	
	function addMessage(message: Message) {
		askApi(message);
		chatHistory = [message, ...chatHistory];
	}

	function addSystemMessage(message: Message){
		chatHistory = [message, ...chatHistory]
	}

	function handleRestartChatContext(){
		fetch(API_URL + 'delete-conversation', {
			method: 'POST',
			body: JSON.stringify({
				from: user
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				'Access-Control-Allow-Origin': '*'
			}
		})

		let sysMessage: Message = {
			owner: "System",
			text: "El bot ha olvidado los mensajes anteriores." 
		}

		addSystemMessage(sysMessage)
	}



	function getContext() {
		fetch(API_URL + "get-context")
		.then((response) => response.json())
		.then((data) => context = data.context)
	}

	function askApi(message: Message){
		console.log(message);
		fetch(API_URL + 'prompt', {
			method: 'POST',
			body: JSON.stringify({
				max_tokens: 64,
				prompt: message.text,
				from: message.owner
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				'Access-Control-Allow-Origin': '*'
			}
		})
        .then((response) => response.json())
        .then((data) => {
			let newMessage: Message = {
				owner: "Bot",
				text: data.answer
			}
			chatHistory = [newMessage, ...chatHistory]
		})
        .catch((error) => {
            //handle error
        });
	}

	getContext();

</script>

<div class="flex h-full">
	<SideBar {hidden} on:chatClicked={() => hidden = !hidden} />
	{#if !hidden}
		<div id="chat_view" class="absolute left-0 top-0 h-full w-full md:static">
			<div class="flex h-full w-full flex-col justify-between">
				<ChatTopBar {hidden} on:backButtonClicked={() => hidden = !hidden}/>
				<Chat {chatHistory} />
				<ChatTextInput on:newMessage={handleNewMessage} on:deleteChat={ () => handleRestartChatContext()} />				
			</div>
		</div>
	{/if}
</div>
<script lang="ts">
	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';
	import ChatTextInput from '../../components/chatTextInput.svelte';
	import ChatTopBar from '../../components/chatTopBar.svelte';

	type owner = "Bot" | string;
	interface Message {
		owner: owner,
		text: string
	}
	
	let chatHistory: string[] = [];
	let hidden = false;
	let user: owner = "9999071819"
	
	function handleNewMessage(a){
		console.log(a)
		addMessage(a.detail.prompt)
	}
	
	const API_URL: string = 'http://192.168.1.140:7861/';
	function addMessage(message: string) {
		askApi(message);
		chatHistory = [message.trim(), ...chatHistory];
		console.log(chatHistory);
	}

	function handleDeleteChat(){
		chatHistory = [];
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
	}

	function askApi(message: string) {
		console.log(message);
		fetch(API_URL + 'prompt', {
			method: 'POST',
			body: JSON.stringify({
				max_tokens: 64,
				prompt: message,
				from: user
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				'Access-Control-Allow-Origin': '*'
			}
		})
        .then((response) => response.json())
        .then((data) => (chatHistory = [data.answer, ...chatHistory]))
        .catch((error) => {
            //handle error
        });
	}
</script>

<div class="flex h-full">
	<SideBar {hidden} on:chatClicked={() => hidden = !hidden} />
	{#if !hidden}
		<div id="chat_view" class="absolute left-0 top-0 h-full w-full md:static">
			<div class="flex h-full w-full flex-col justify-between">
				<ChatTopBar {hidden} on:backButtonClicked={() => hidden = !hidden}/>
				<Chat {chatHistory} />
				<ChatTextInput on:newMessage={handleNewMessage} on:deleteChat={ () => handleDeleteChat()} />				
			</div>
		</div>
	{/if}
</div>
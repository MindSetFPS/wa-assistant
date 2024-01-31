<script lang="ts">
	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';
	import ChatTextInput from '../../components/chatTextInput.svelte';
	import ChatTopBar from '../../components/chatTopBar.svelte';

	let text = '';
	let prompt = '';
	let chatHistory: string[] = [];
	let hidden = false;
	
	function handleNewMessage(a){
		console.log(a)
		addMessage(a.detail.prompt)
	}

	function handleDeleteChat(){
		chatHistory = [];
	}

	function addMessage(message: string) {
		askApi(message);
		chatHistory = [message.trim(), ...chatHistory];
		console.log(chatHistory);
	}

	function askApi(message: string) {
		console.log(message);
		fetch('http://192.168.1.140:7861/prompt', {
			method: 'POST',
			body: JSON.stringify({
				max_tokens: 64,
				prompt: message,
				from: '999999999'
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
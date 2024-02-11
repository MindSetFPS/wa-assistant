<script lang="ts">
	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';
	import ChatTextInput from '../../components/chatTextInput.svelte';
	import ChatTopBar from '../../components/chatTopBar.svelte';
	import API_URL from '$lib/constants';
	// import { context } from '$lib/store';
	import { onMount } from 'svelte';
	import supabase from '$lib/supabaseClient';
	import type { Tables } from '$lib/supabase';

	type owner = "Bot" | "System" | string;
	
	interface Message {
		owner: owner,
		text: string
	}
	
	let chatHistory: Message[] = [];

	let conversation: Tables<"conversations">;
	let hidden = false;
	let user: owner = "9999071819"
	
	function handleNewMessage(a: CustomEvent){
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
	
	async function getConversation(id: string){
		console.log(id)
		let { data: messages, error } = await supabase
			.from('conversations')
			.select("messages, customer_id")
			.eq("customer_id", id)
			.single()

		if(messages){
			console.log(messages)
			conversation = messages;
		}

		if(error){
			console.log(error)
		}
	}

	function openChatIfNotAlready(){
		console.log("open/close")
	}

	const handleChatClicked = async (data: CustomEvent) => {
		console.log(data.detail.chatId)
		await getConversation(data.detail.chatId)
		openChatIfNotAlready()
	}
		// onMount(() => {
		// 	getContext();
		// })

</script>

<div class="flex h-full">
	<SideBar {hidden} on:chatClicked={handleChatClicked} />
	{#if !hidden}
		<div id="chat_view" class="absolute left-0 top-0 h-full w-full md:static">
			<div class="flex h-full w-full flex-col justify-between">
				{#if conversation}
						<ChatTopBar conversation={conversation} on:backButtonClicked={() => (hidden = !hidden)} />
						<Chat conversation={conversation} />
						<ChatTextInput
							on:newMessage={() => console.log("New message")}
							on:deleteChat={() => handleRestartChatContext()}
						/>
				{/if}
			</div>
		</div>
	{/if}
</div>

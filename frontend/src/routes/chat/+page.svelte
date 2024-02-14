<script lang="ts">
	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';
	import ChatTextInput from '../../components/chatTextInput.svelte';
	import ChatTopBar from '../../components/chatTopBar.svelte';
	import supabase from '$lib/supabaseClient';
	import type { Tables } from '$lib/supabase';
	import { onMount } from 'svelte';

	type owner = "Bot" | "System" | string;
	interface Message {
		owner: owner,
		text: string
	}
	let chatHistory: Message[] = [];
	let chatsList: Tables<"conversations">[];
	let openChat: Tables<"conversations">["messages"];
	let chatIsVisible = true;
	let selectedChatIndex: number = 0;
	let hidden = false;
	let user: owner = "9999071819"
	// function handleNewMessage(a: CustomEvent){
	// 	let newMessage: Message = {
	// 		owner: user,
	// 		text: a.detail.prompt
	// 	}
	// 	addMessage(newMessage)
	// }
	
	// function addMessage(message: Message) {
	// 	askApi(message);
	// 	chatHistory = [message, ...chatHistory];
	// }
	function addSystemMessage(message: Message){
		chatHistory = [message, ...chatHistory]
	}
	// function handleRestartChatContext(){
	// 	fetch(API_URL + 'delete-conversation', {
	// 		method: 'POST',
	// 		body: JSON.stringify({
	// 			from: user
	// 		}),
	// 		headers: {
	// 			'Content-type': 'application/json; charset=UTF-8',
	// 			'Access-Control-Allow-Origin': '*'
	// 		}
	// 	})
		
	// 	let sysMessage: Message = {
	// 		owner: "System",
	// 		text: "El bot ha olvidado los mensajes anteriores." 
	// 	}
	// 	addSystemMessage(sysMessage)
	// }
	
	async function getConversations(){
		let { data: conversations, error } = await supabase
			.from('conversations')
			.select("*")
		if(conversations){
			console.log(conversations)
			chatsList = conversations;
		}
		if(error){
			console.log(error)
		}
	}

	const handleChatClicked = async (data: CustomEvent) => {
		console.log(data.detail.chatIndex)
		if(chatsList.length == 0){
			await getConversations()
		}
		
		if(selectedChatIndex === data.detail.chatIndex){
			chatIsVisible = !chatIsVisible
		} else {
			chatIsVisible = true
		}

		
		selectedChatIndex = data.detail.chatIndex;
		openChat = chatsList[selectedChatIndex]
	}
	
	onMount(async () => {
	// 	getContext();
		await getConversations()
	})


</script>

<div class="flex h-full">
	<SideBar conversations={chatsList} on:chatClicked={handleChatClicked} />
	{#if chatIsVisible && openChat != undefined }
		<div id="chat_view" class="absolute left-0 top-0 h-full w-full md:static">
			<div class="flex h-full w-full flex-col justify-between">
						<ChatTopBar conversation={chatsList[selectedChatIndex].customer_id} on:backButtonClicked={() => (chatIsVisible = !chatIsVisible)} />
						<Chat conversations={[...chatsList[selectedChatIndex].messages]} />
						<ChatTextInput
							on:newMessage={() => console.log("New message")}
							on:deleteChat={() => console.log("Deleted chat")}
						/>
			</div>
		</div>
	{/if}
</div>

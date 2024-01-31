<script lang="ts">
	import Message from './message.svelte';

	export let chatHistory: Message[] = [];
</script>

<div class="flex h-full flex-col-reverse overflow-y-scroll bg-gray-600 px-4">
	{#each chatHistory as chatMessage, i}
		<Message
			message={chatMessage.text}
			name={chatMessage.owner}
			className={chatMessage.owner == 'System'
				? 'mx-auto bg-slate-400 dark:bg-slate-600 text-center align-middle text-xs'
				: chatMessage.owner == "Bot" ? 'mr-auto bg-blue-300 dark:bg-blue-600' : "ml-auto bg-green-400 dark:bg-green-500"
            
            }
		/>
	{/each}
</div>

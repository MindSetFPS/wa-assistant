<script lang="ts">
	import Message from './message.svelte';
	export let conversations: any[];

	// let messages = [...conversations.messages]

	// let messages = [1,2,3,4,5,5,6]

	console.log(conversations);
</script>

<div class="flex h-full flex-col-reverse overflow-y-scroll bg-gray-600 px-4">
	{#await conversations}
		Loading
	{:then}
		{#if (conversations.length > 0)}
			{#each conversations.reverse() as chatMessage}
				<Message
					message={chatMessage.content}
					name={'chatMessage'}
					className={chatMessage.role == 'System'
						? 'mx-auto bg-slate-400 dark:bg-slate-600 text-center align-middle text-xs'
						: chatMessage.role == 'assistant'
							? 'mr-auto bg-blue-300 dark:bg-blue-600'
							: 'ml-auto bg-green-400 dark:bg-green-500'}
				/>
				<!-- {chatMessage} -->
			{/each}
		{/if}
	{/await}
</div>

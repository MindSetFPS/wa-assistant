<script lang="ts">
	import Message from './message.svelte';
	import type { Tables } from '$lib/supabase';

	export let conversation: Tables<'conversations'>;

</script>

<div class="flex h-full flex-col-reverse overflow-y-scroll bg-gray-600 px-4">
	{#await conversation}
		Loading
	{:then}
		{#each conversation.messages as chatMessage, i}
			<Message
				message={chatMessage.content}
				name={'chatMessage'}
				className={chatMessage.role == 'System'
					? 'mx-auto bg-slate-400 dark:bg-slate-600 text-center align-middle text-xs'
					: chatMessage.role == 'assistant'
						? 'mr-auto bg-blue-300 dark:bg-blue-600'
						: 'ml-auto bg-green-400 dark:bg-green-500'}
			/>
		{/each}
	{/await}
</div>

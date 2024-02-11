<script lang="ts">
    import {ArrowLeftOutline} from 'flowbite-svelte-icons';
    import { Avatar } from 'flowbite-svelte';
    import { createEventDispatcher } from 'svelte';
	import type { Tables } from '$lib/supabase';
	
    const dispatch = createEventDispatcher();
    export let conversation: Tables<"conversations">;
    console.log(conversation)
</script>

<div class="flex items-center bg-blue-400 py-4 pl-2 align-middle">
    <ArrowLeftOutline
        size="xl"
        class="mx-2 rounded-full p-2
        text-black hover:bg-slate-500 dark:text-white md:hidden"
        on:click={() => dispatch('backButtonClicked')}
    />
    <Avatar />
    <p class="ml-2 text-2xl text-white">
    {#await conversation}
        loading
    {:then} 
        {conversation.customer_id}
    {/await}
    </p>
</div>
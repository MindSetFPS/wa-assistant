<script lang="ts">
    import {
        ArrowLeftOutline,
    } from 'flowbite-svelte-icons';
    import { Avatar } from 'flowbite-svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    export let hidden: Boolean;

</script>

<div class="flex items-center bg-blue-400 py-4 pl-2 align-middle">
    <ArrowLeftOutline
        size="xl"
        class="mx-2 rounded-full p-2
        text-black hover:bg-slate-500 dark:text-white md:hidden"
        on:click={() => dispatch('backButtonClicked')}
    />
    <Avatar />
    <p class="ml-2 text-2xl text-white">Ernesto Sebastian</p>
</div>
<script lang="ts">
	import { Textarea, Alert, ToolbarButton, P } from 'flowbite-svelte';
	import { BarsSolid, PapperPlaneOutline } from 'flowbite-svelte-icons';
	import { Dropdown, DropdownItem } from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';
	import PrompSetupModal from './PrompSetupModal.svelte';
	const dispatch = createEventDispatcher();

	let placement: string = 'top';
	// export let chatHistory: string[];
	let prompt: string;
	let modalIsOpen: boolean = false;
</script>

<PrompSetupModal {modalIsOpen} />

<form class="w-full">
	<label for="chat" class="sr-only">Your message</label>
	<Dropdown placement={"top"} triggeredBy="#dropdown">
		<DropdownItem on:click={() => dispatch('deleteChat')}>Reiniciar conversacion</DropdownItem>
		<DropdownItem on:click={() => (modalIsOpen = !modalIsOpen)}>Prompts</DropdownItem>
	</Dropdown>
	<Alert color="dark" class="px-1 py-2">
		<svelte:fragment slot="icon">
			<ToolbarButton color="dark" class="text-gray-500 dark:text-gray-400" id="dropdown">
				<BarsSolid class="h-5 w-5" />
				<span class="sr-only">Upload image</span>
			</ToolbarButton>
			<Textarea
				id="chat"
				class="mx-1"
				rows="1"
				placeholder="Your message..."
				bind:value={prompt}
				on:keypress={(e) => {
					if (e.key == 'Enter') {
						dispatch('newMessage', {
							prompt
						});
						prompt = ''.trim();
					}
				}}
			/>
			<ToolbarButton
				type="submit"
				color="blue"
				class="rounded-full text-primary-600 dark:text-primary-500"
				on:click={() => {
					dispatch('newMessage', {
						prompt
					});
					prompt = '';
				}}
			>
				<PapperPlaneOutline class="h-5 w-5 rotate-45" />
				<span class="sr-only">Send message</span>
			</ToolbarButton>
		</svelte:fragment>
	</Alert>
</form>

<script lang="ts">
	import { Textarea, Alert, ToolbarButton, P } from 'flowbite-svelte';
	import { BarsSolid, PapperPlaneOutline } from 'flowbite-svelte-icons';
	import { Dropdown, DropdownItem } from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let placement: string = 'top';
	// export let chatHistory: string[];
	let prompt: string;

</script>

<form class="w-full">
	<label for="chat" class="sr-only">Your message</label>
	<Dropdown {placement} triggeredBy="#dropdown">
		<DropdownItem on:click={() => dispatch("deleteChat")}>Reiniciar conversacion</DropdownItem>
		<DropdownItem>Settings</DropdownItem>
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
						console.log(e.key);
						// addMessage();
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
				class="text-primary-600 dark:text-primary-500 rounded-full"
				
			>
				<PapperPlaneOutline class="h-5 w-5 rotate-45" />
				<span class="sr-only">Send message</span>
			</ToolbarButton>
		</svelte:fragment>
	</Alert>
</form>

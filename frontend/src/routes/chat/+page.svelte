<script>
	let lang = 'ts';
	import { Textarea, Alert, ToolbarButton, P } from 'flowbite-svelte';
	import {
		PapperPlaneOutline,
		BarsSolid,
		ArrowLeftOutline,
		} from 'flowbite-svelte-icons';
	import { Avatar, Dropdown, DropdownItem } from 'flowbite-svelte';

	import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';

	let placement = 'top';
	let text = '';
	let prompt = '';
	let chatHistory = [];
	function askApi() {
		fetch('http://192.168.1.140:7861/prompt', {
			method: 'POST',
			body: JSON.stringify({
				max_tokens: 128,
				prompt: prompt,
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

	function addMessage() {
		askApi(prompt);
		chatHistory = [prompt, ...chatHistory];
		// chatHistory = chatHistory.reverse()
		console.log(chatHistory);
		prompt = '';
	}

	function keypress(e) {
		if (e.key == 'Enter') {
			console.log(e.key);
			addMessage();
			prompt = '';
		}
	}

	let hidden = false;
</script>

<div class="flex h-full">
	<SideBar {hidden} on:chatClicked={() => hidden = !hidden} />
	{#if !hidden}
		<div id="chat_view" class="absolute left-0 top-0 h-full w-full md:static">
			<div class="flex h-full w-full flex-col justify-between">
				<div class="flex items-center bg-blue-400 py-4 pl-2 align-middle">
					<ArrowLeftOutline
						size="xl"
						class="mx-2 rounded-full p-2
                        text-black hover:bg-slate-500 dark:text-white md:hidden"
						on:click={() => (hidden = !hidden)}
					/>
					<Avatar />
					<p class="ml-2 text-2xl text-white">Ernesto Sebastian</p>
				</div>
				<Chat {chatHistory} />
				<form class="w-full">
					<label for="chat" class="sr-only">Your message</label>
					<Dropdown {placement} triggeredBy="#dropdown">
						<DropdownItem>Dashboard</DropdownItem>
						<DropdownItem>Settings</DropdownItem>
						<DropdownItem>Earnings</DropdownItem>
						<DropdownItem slot="footer">Sign out</DropdownItem>
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
								on:keypress={(e) => keypress(e)}
							/>
							<ToolbarButton
								type="submit"
								color="blue"
								class="rounded-full text-primary-600 dark:text-primary-500"
								on:click={() => addMessage()}
							>
								<PapperPlaneOutline class="h-5 w-5 rotate-45" />
								<span class="sr-only">Send message</span>
							</ToolbarButton>
						</svelte:fragment>
					</Alert>
				</form>
			</div>
		</div>
	{/if}
</div>

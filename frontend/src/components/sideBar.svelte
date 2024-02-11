<script lang="ts">
	import {DarkMode,Sidebar,SidebarDropdownWrapper,SidebarGroup,SidebarItem,SidebarWrapper} from 'flowbite-svelte';
	import { ChartSolid, GridSolid, MailBoxSolid, UserSolid } from 'flowbite-svelte-icons';
	import { createEventDispatcher } from 'svelte';
	import { sineIn } from 'svelte/easing';
	import supabase from '$lib/supabaseClient';
	import type { Tables } from '$lib/supabase';
	import { page } from '$app/stores';

	$: activeUrl = $page.url.pathname;

	let spanClass = 'flex-1 ms-3 whitespace-nowrap';
	let activateClickOutside = false;
	let backdrop = false;
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn
	};

	export let chats: Tables<'conversations'>[];
	chats = [];

	async function getConversations() {
		let { data: messages, error } = await supabase.from('conversations').select('customer_id');
		if (messages) {
			chats = messages;
		}

		if (error) {
			console.log(error);
		}
	}

	getConversations();

	const dispatch = createEventDispatcher();
</script>

<div class="h-full w-full list-none md:w-auto">
	<Sidebar class="h-full w-full" {activeUrl}>
		<SidebarWrapper class="h-full w-full">
			<SidebarDropdownWrapper label="Navegacion">
				<SidebarItem label="Dashboard">
					<svelte:fragment slot="icon">
						<ChartSolid
							class="ml-6 h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>

				<SidebarItem label="Kanban" {spanClass}>
					<svelte:fragment slot="icon">
						<GridSolid
							class="ml-6 h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<svelte:fragment slot="subtext">
						<span
							class="ms-3 inline-flex items-center justify-center rounded-full bg-gray-200 px-2 text-sm font-medium text-gray-800 dark:bg-gray-700 dark:text-gray-300"
						>
							Pro
						</span>
					</svelte:fragment>
				</SidebarItem>

				<SidebarItem label="Inbox" {spanClass}>
					<svelte:fragment slot="icon">
						<MailBoxSolid
							class="ml-6 h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<svelte:fragment slot="subtext">
						<span
							class="text-primary-600 bg-primary-200 dark:bg-primary-900 dark:text-primary-200 ml-6 ms-3 inline-flex h-3 w-3 items-center justify-center rounded-full p-3 text-sm font-medium"
						>
							3
						</span>
					</svelte:fragment>
				</SidebarItem>

				<SidebarItem label="Modo oscuro" active={true}>
					<svelte:fragment slot="icon">
						<!-- <UserSolid class="ml-6 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" /> -->
						<DarkMode btnClass="ml-6" />
					</svelte:fragment>
				</SidebarItem>
			</SidebarDropdownWrapper>

			<SidebarGroup>
				<SidebarItem label="Chats" active={activeUrl === '/docs/components/sidebar'}>
					<svelte:fragment slot="icon">
						<UserSolid
							class=" h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
					{#each chats as chat}
					<SidebarItem
					label={chat.customer_id}
					on:click={() => dispatch('chatClicked', { chatId: chat.customer_id })}
					>
					<svelte:fragment slot="icon">
						<UserSolid
						class="ml-6 h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				{/each}
			</SidebarGroup>
		</SidebarWrapper>
	</Sidebar>
</div>

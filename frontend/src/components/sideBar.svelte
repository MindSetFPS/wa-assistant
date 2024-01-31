<script>
  import { DarkMode, Sidebar, SidebarBrand, SidebarCta, SidebarDropdownItem, SidebarDropdownWrapper, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
  import { ChartPieSolid, ShoppingCartSolid, GridSolid, MailBoxSolid, UsersSolid, BagSolid, ArrowRightToBracketSolid, FileEditSolid, UserSolid } from 'flowbite-svelte-icons';
  import { sineIn } from 'svelte/easing';
  let activateClickOutside = false;
  let backdrop = false;
  let spanClass = 'flex-1 ms-3 whitespace-nowrap';
  import { page } from '$app/stores';
  let transitionParams = {
    x: -320,
    duration: 200,
    easing: sineIn
  };
  $: activeUrl = $page.url.pathname;
  export let chats = ["juan", "pepe", "tono"]
  export let hidden;
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();
</script>

<div class="w-full md:w-auto h-full list-none" >
  <Sidebar class="w-full h-full" {activeUrl}>
    <SidebarWrapper class="w-full h-full" >
      <SidebarDropdownWrapper label="Navegacion">
        
        <SidebarItem label="Dashboard">
          <svelte:fragment slot="icon">
            <ChartPieSolid class="ml-6 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
          </svelte:fragment>
        </SidebarItem>
        
        <SidebarItem label="Kanban" {spanClass}>
          <svelte:fragment slot="icon">
            <GridSolid class="ml-6 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
          </svelte:fragment>
          <svelte:fragment slot="subtext">
            <span class="inline-flex justify-center items-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-200 rounded-full dark:bg-gray-700 dark:text-gray-300"> Pro </span>
          </svelte:fragment>
        </SidebarItem>

        <SidebarItem label="Inbox" {spanClass}>
          <svelte:fragment slot="icon">
            <MailBoxSolid class="ml-6 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
          </svelte:fragment>
          <svelte:fragment slot="subtext">
            <span class="ml-6 inline-flex justify-center items-center p-3 ms-3 w-3 h-3 text-sm font-medium text-primary-600 bg-primary-200 rounded-full dark:bg-primary-900 dark:text-primary-200"> 3 </span>
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
            <UserSolid class=" w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
          </svelte:fragment>
        </SidebarItem>

        {#each chats as chat}
          <SidebarItem label={chat} on:click={ () => dispatch('chatClicked')}>
            <svelte:fragment slot="icon">
              <UserSolid class="ml-6 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            </svelte:fragment>
          </SidebarItem>
        {/each}
      </SidebarGroup>

    </SidebarWrapper>
  </Sidebar>
  </div>
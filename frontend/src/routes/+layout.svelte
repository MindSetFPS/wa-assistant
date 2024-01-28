<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { page } from '$app/stores';
  import { DarkMode } from 'flowbite-svelte';

    $: activeUrl = $page.url.pathname;
</script>

<div class="w-screen flex flex-col h-full" >
  <Navbar class="h-[80px]">
    <NavBrand href="/">
      <img src="" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
    </NavBrand>
    <NavHamburger />
    <NavUl {activeUrl}>
      <NavLi href="/">Home</NavLi>
      <NavLi href="/setup">Setup</NavLi>
      <NavLi href="/chat">chat</NavLi>
      <NavLi href="/docs/components/alert">Alert</NavLi>
      <NavLi href="/docs/components/avatar">Avatar</NavLi>
      <NavLi> <DarkMode /> </NavLi>
    </NavUl>
  </Navbar>
  
  <div class="container mx-auto px-2 md:px-36 relative h-full" id="cont" >
    <!-- <div class="block sm:hidden" >base</div>
    <div class="hidden sm:block md:hidden" ></div>
    <div class="hidden lg:block xl:hidden" ></div>
    <div class="hidden md:block lg:hidden" ></div>
    <div class="hidden xl:block 2xl:hidden" ></div>
    <div class="hidden 2xl:block" ></div> -->
    <slot></slot>
  </div>
</div>

<style>


  #cont {
    height: calc(100vh - 80px);
  }



</style>
<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { page } from '$app/stores';
  import { DarkMode } from 'flowbite-svelte';

    $: activeUrl = $page.url.pathname;
</script>

<Navbar>
    <NavBrand href="/">
      <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
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

<div class="container mx-auto px-2 md:px-36">

  <div class="visible sm:invisible" >base</div>
  <div class="invisible sm:visible md:invisible" ></div>
  <div class="invisible md:visible lg:invisible" ></div>
  <div class="invisible lg:visible xl:invisible" ></div>
  <div class="invisible xl:visible 2xl:invisible" ></div>
  <div class="invisible 2xl:visible" ></div>

    <slot></slot>
</div>

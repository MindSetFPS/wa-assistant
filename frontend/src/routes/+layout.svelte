<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import "../app.pcss";
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

<div class="container mx-auto md:px-36">
    <slot></slot>
</div>

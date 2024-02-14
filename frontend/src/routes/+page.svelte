<script>
  import { Heading, P, Span } from 'flowbite-svelte';
  import { DeviceMockup, GradientButton, Button } from 'flowbite-svelte';
  import { ArrowRightSolid, GoogleSolid } from 'flowbite-svelte-icons';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { DarkMode } from 'flowbite-svelte';
  import { page } from '$app/stores';

  $: activeUrl = $page.url.pathname;

</script>

<div class="divide-y divide-neutral-50 ">

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

    <div>
      <Heading tag="h1" class="mb-4 text-3xl font-extrabold  md:text-7xl lg:text-8xl">
        <Span gradient class="text-4xl md:text-7xl">Tu Whatsapp vende </Span> <br class="hidden md:block" /> sin estar ahí.
      </Heading>
      <P class=" text-lg md:text-4xl ">Whatbot entiende tu negocio, productos y precios para atender a tus clientes y ayudandote a vender más.</P>
      <div class="flex justify-evenly md:justify-center my-2 w-full">
        
        <GradientButton class="w-full mr-1 py-4" color="green">
          Pruebalo ya <GoogleSolid size="xs" class="ml-2"/> 
        </GradientButton>
      
        <Button color="light" class="w-full ml-1">
          Comenzar <ArrowRightSolid class="ml-2" size="xs"/> 
        </Button>
      
      </div>
    </div>

  <div class="py-4">
    <DeviceMockup device="laptop">
      <img src="https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2015/01/82509-whatsapp-web-ya-esta-activo-fin-whatsapp-navegador.jpg?tf=3840x" class="dark:hidden h-[156px] md:h-[278px] w-full rounded-xl" alt="laptop example 1" />
      <img src="https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2015/01/82509-whatsapp-web-ya-esta-activo-fin-whatsapp-navegador.jpg?tf=3840x" class="hidden dark:block h-[156px] md:h-[278px] w-full rounded-lg" alt="laptop example 2" />
    </DeviceMockup>
  </div>

  <div class="py-4">
    <Heading tag="h2" class="text-2xl md:text-4xl font-bold" customSize="">
      Whatbot es capaz de conocer tu negocio al pie de la letra.
    </Heading>  
    <P>Unicamente llena una forma con informacion sobre tus productos, horarios, precios y ubicaciones.</P>
  </div>

  <div class="py-4">
    <Heading tag="h2" customSize="text-2xl font-bold">
      Privacidad garantizada.
    </Heading>
    <P>No almacenamos informacion privada de tus usuarios. Unicamente su numero de telefono para que puedas administrarlo desde nuestra plataforma.</P>
  </div>

  <div>
    <Heading tag="h2" customSize="text-2xl font-bold">
      Whatsapp en esteroides.
    </Heading>
    <P>Mejoramos substancialmente tu experiencia en Whatsapp. ¿Necesitas tomar el control de una conversacion? Hazlo en un click.</P>
  </div>
</div>

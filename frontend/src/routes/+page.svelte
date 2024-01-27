<script>
  import { Heading, P, Span } from 'flowbite-svelte';
  import { DeviceMockup, GradientButton, Button } from 'flowbite-svelte';
  import { ArrowRightSolid, GoogleSolid } from 'flowbite-svelte-icons';
</script>

<div class="divide-y divide-neutral-50 ">

    <div>
      <Heading tag="h1" class="mb-4 text-6xl font-extrabold  md:text-7xl lg:text-8xl">
        <Span gradient>Vende en Whatsapp</Span> <br /> sin estar ahí.
      </Heading>
      <P class="p-2 md: text-3xl">Whatbot atiende a tus clientes y te ayuda a vender más. Whatbot entiende tu negocio, productos y precios para que tu te enfoques en mejorar tus productos.</P>
      <div class="flex justify-evenly md:justify-center p-4">
        
        <GradientButton size="xl" class="transition-all mx-4" color="greenToBlue">Pruebalo ya <GoogleSolid class="w-3.5 h-3.5 ms-2 align-middle" /> </GradientButton>
        
        <Button size="xl" color="light" class="transition-all mx-4">Empieza ahora <ArrowRightSolid class="w-3.5 h-3.5 ms-2" /> </Button>
      
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
    <P>Mejoras a la experiencia de usuario en Whatsapp. ¿Necesitas tomar el control de una conversacion? Hazlo en un click.</P>
  </div>
</div>

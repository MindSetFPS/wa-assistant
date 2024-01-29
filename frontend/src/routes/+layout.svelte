<script>
  import "../app.pcss";

</script>

<div class="w-screen flex flex-col h-full" >

  
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

  /* #cont {
    height: calc(100vh - 80px);
  } */

</style>
<script>
	import { Heading, P, Span, Card } from 'flowbite-svelte';

	import { Auth } from '@supabase/auth-ui-svelte';
	import { ThemeSupa } from '@supabase/auth-ui-shared';
  import { onMount } from 'svelte';
  import { invalidate, goto, pushState } from '$app/navigation';

	export let data;
//   console.log(data.url)

let { supabase, session } = data
$: ({ supabase, session } = data)

$:    supabase.auth.onAuthStateChange(async (event, session) => {
  if (event === 'SIGNED_IN') await goto("/account")
})

onMount(() => {
  const { data } = supabase.auth.onAuthStateChange((event, _session) => {
    if(_session?.expires_at !== session?.expires_at) {
      invalidate('supabase:auth')
    }
  })
    
  return () => data.subscription.unsubscribe()
})

onMount( async () => {
  supabase.auth.onAuthStateChange( (event, session) => {
  if (event === 'SIGNED_IN') setTimeout( () => goto("/account"), 0) 
})
})


</script>


<Card class="flex w-full mx-auto mt-12 max-w-md" >
  <Heading tag="h1" class="mb-4">
    We invest in the <Span
      underline
      decorationClass="decoration-8 decoration-blue-400 dark:decoration-blue-600"
      >world’s potential</Span
    >
  </Heading>
  <P
    >Inicia sesión o registrate</P
  >

	<Auth
		supabaseClient={data.supabase}
		view="sign_in"
		redirectTo={`${data.url}/account`}
		providers={['google', 'facebook']}
		socialLayout="horizontal"
    showLinks={true}
		appearance={{ theme: ThemeSupa, style: { input: 'color: #fff' } }}
    theme="dark"
	/>
</Card>

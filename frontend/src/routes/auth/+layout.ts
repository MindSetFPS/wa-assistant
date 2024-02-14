// Create a new src/routes/+layout.ts file to handle 
// the session and the supabase object on the client-side.

// No puede cargar porque no tiene session
// Session viene de +layout.server.ts
// Sigue sin hacer nada

import { SUPABASE_ANON_API_KEY, SUPABASE_PROJECT_URL } from '$lib/constants'
import { createSupabaseLoadClient } from '@supabase/auth-helpers-sveltekit'

console.log("hit routes/auth/+layout.ts")


export const load = async ({ fetch, data, depends }) => {
  depends('supabase:auth')

  const supabase = createSupabaseLoadClient({
    supabaseUrl: SUPABASE_PROJECT_URL,
    supabaseKey: SUPABASE_ANON_API_KEY,
    event: { fetch },
    serverSession: data.session,
  })

  const {
    data: { session },
  } = await supabase.auth.getSession()

  return { supabase, session }
}
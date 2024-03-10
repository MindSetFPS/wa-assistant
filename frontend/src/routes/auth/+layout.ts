// Create a new src/routes/+layout.ts file to handle 
// the session and the supabase object on the client-side.

// No puede cargar porque no tiene session
// Session viene de +layout.server.ts
// Sigue sin hacer nada

import { PUBLIC_SUPABASE_API_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'
import { createSupabaseLoadClient } from '@supabase/auth-helpers-sveltekit'

console.log("hit routes/auth/+layout.ts")


export const load = async ({ fetch, data, depends }) => {
  depends('supabase:auth')

  const supabase = createSupabaseLoadClient({
    supabaseUrl: PUBLIC_SUPABASE_URL,
    supabaseKey: PUBLIC_SUPABASE_API_KEY,
    event: { fetch },
    serverSession: data.session,
  })

  const {
    data: { session },
  } = await supabase.auth.getSession()

  return { supabase, session }
}
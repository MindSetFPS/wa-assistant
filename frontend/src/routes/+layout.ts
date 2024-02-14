// Create a new src/routes/+layout.ts file to handle 
// the session and the supabase object on the client-side.





import { SUPABASE_ANON_API_KEY, SUPABASE_PROJECT_URL } from '$lib/constants'
import { createSupabaseLoadClient } from '@supabase/auth-helpers-sveltekit'

console.log("hit routes/+layout.ts")

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
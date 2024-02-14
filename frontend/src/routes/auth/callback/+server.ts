import { redirect } from "@sveltejs/kit";

console.log('hit routes/callback/+server.ts')
export const GET = async ({ url, locals: { supabase } }) => {
    const code = url.searchParams.get('code')

    if(code) {
        await supabase.auth.exchangeCodeForSession(code)
    }

    throw redirect(303, '/account')
}
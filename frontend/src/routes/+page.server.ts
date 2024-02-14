// Create a src/routes/+page.server.ts file that will return our website 
// url to be used in redirectTo at src/routes/+page/svelte.

import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({url, locals: { getSession }}) => {
    console.log("hit routes/+page.server.ts")
    const session = await getSession()

    // if the user is already logged in return them to the account page
    if(session) {
        throw redirect(303, '/account')
    }

    return { url: url.origin}
}
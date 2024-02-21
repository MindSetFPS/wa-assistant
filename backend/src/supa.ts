import { createClient } from '@supabase/supabase-js'
import dotenv from 'dotenv'
dotenv.config()

const supabase = createClient(process.env.PUBLIC_SUPABASE_URL!, process.env.PUBLIC_SUPABASE_API_KEY!)


async function getConversation(message_from: string) {
    const { data, error } = await supabase
        .from('conversations')
        .select('messages')
        .eq('customer_id', message_from)
        .single()

    if (data) {
        return data.messages
    }
    if (error) {
        console.log(error)
    }
}

export { supabase, getConversation }
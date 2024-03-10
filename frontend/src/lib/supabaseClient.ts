import { createClient } from '@supabase/supabase-js'
import type { Database } from './supabase';

import { PUBLIC_SUPABASE_API_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'

const supabase = createClient<Database>(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_API_KEY);

export default supabase;

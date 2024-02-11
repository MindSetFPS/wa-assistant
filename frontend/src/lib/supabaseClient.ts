import { createClient } from '@supabase/supabase-js'
import type { Database } from './supabase';

const supabase = createClient<Database>(
);

export default supabase;

<script>
    export let chatHistory;
    
</script>


<div class="bg-gray-600 flex flex-col-reverse overflow-y-scroll h-full px-4 " >    

    {#each chatHistory as chatMessage, i}
    <div 
        class="rounded-xl my-3 {(i + 1) % 2 == 0 ? 'ml-auto bg-green-400 dark:bg-green-600' : 'mr-auto bg-blue-400 dark:bg-blue-700'}"  >
        <!-- <img class="w-8 h-8 rounded-full" src="" alt="Jese"> -->
        <div 
            class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 rounded-e-xl rounded-es-xl "
        >
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
                <span class="text-sm font-semibold text-gray-900 dark:text-white">
                    {#if (i + 1) % 2 == 0}
                        Human
                    {:else}
                        Bot
                    {/if}
                </span>
                <span class="text-sm font-normal text-gray-500 dark:text-gray-400">{new Date().toLocaleTimeString()}</span>
            </div>
            <p class="text-sm font-normal py-2.5 text-gray-900 dark:text-white">{chatMessage}</p>
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Delivered</span>
        </div>    
    </div>
    {/each}

</div>
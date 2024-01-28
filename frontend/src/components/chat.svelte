<script>
    export let chatHistory;
    
</script>


<div class="bg-gray-600 flex flex-col-reverse overflow-y-scroll h-full" >    

    {#each chatHistory as chatMessage, i}
        <img class="w-8 h-8 rounded-full" src="" alt="Jese">
        <div class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
                <span class="text-sm font-semibold text-gray-900 dark:text-white">Bonnie Green</span>
                <span class="text-sm font-normal text-gray-500 dark:text-gray-400">11:46</span>
            </div>
            <p class="text-sm font-normal py-2.5 text-gray-900 dark:text-white">{chatMessage}</p>
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Delivered</span>
        </div>    
    {/each}

</div>
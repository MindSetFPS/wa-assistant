<script>
    let lang = 'ts'
    import { Textarea, Alert, ToolbarButton, P } from 'flowbite-svelte';
    import { ImageOutline, FaceGrinOutline, PapperPlaneOutline, BarsSolid, ChevronUpSolid } from 'flowbite-svelte-icons';
    import { Button, Dropdown, DropdownItem } from 'flowbite-svelte';

    import Chat from '../../components/chat.svelte';
	import SideBar from '../../components/sideBar.svelte';

    let placement = 'top'
    let text = "";
    let prompt = "";
    let chatHistory = [];
    function askApi() {
        fetch("http://192.168.1.140:7861/prompt", {
            method: "POST",
            body: JSON.stringify({
                max_tokens: 128,
                prompt: prompt,
                from: '999999999',
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "Access-Control-Allow-Origin" : '*'
            },
        })
            .then((response) => response.json())
            .then((data) => ( chatHistory = [data.answer, ...chatHistory]))
            .catch((error) => {
                //handle error
            });
    }

    function addMessage(){
        askApi(prompt)
        chatHistory = [prompt, ...chatHistory]
        // chatHistory = chatHistory.reverse()
        console.log(chatHistory)
        prompt = "";
    }

    function keypress(e){
        if(e.key == "Enter"){
            console.log(e.key)
            addMessage()
            prompt = "";
        }
    }
</script>

<!-- <SideBar /> -->
<div class="h-full flex flex-col justify-between">
    <Chat {chatHistory} />
    <form class="w-full" >
        <label for="chat" class="sr-only">Your message</label>
        <Dropdown {placement} triggeredBy="#dropdown">
            <DropdownItem>Dashboard</DropdownItem>
            <DropdownItem>Settings</DropdownItem>
            <DropdownItem>Earnings</DropdownItem>
            <DropdownItem slot="footer">Sign out</DropdownItem>
        </Dropdown>
        <Alert color="dark" class="px-1 py-2">
            <svelte:fragment slot="icon">
                <ToolbarButton color="dark" class="text-gray-500 dark:text-gray-400" id="dropdown">
                    <BarsSolid class="w-5 h-5" />
                    <span class="sr-only">Upload image</span>
                </ToolbarButton>
                <Textarea 
                    id="chat" 
                    class="mx-1" 
                    rows="1" 
                    placeholder="Your message..." 
                    bind:value={prompt} 
                    on:keypress={(e) => keypress(e)}
                />
                <ToolbarButton type="submit" color="blue" class="rounded-full text-primary-600 dark:text-primary-500"
                on:click={() => addMessage()}
                >
                <PapperPlaneOutline class="w-5 h-5 rotate-45" />
                <span class="sr-only">Send message</span>
            </ToolbarButton>
        </svelte:fragment>
    </Alert>
</form>
</div>
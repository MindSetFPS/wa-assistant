<script>
    import { Button } from "flowbite-svelte";
    
    let text = "";
    let a = 1;
    let b = 5;
    let total = 0;
    function askApi() {
        fetch("http://192.168.1.140:7861/prompt", {
            method: "POST",
            body: JSON.stringify({
                max_tokens: 128,
                prompt: 'hola',
                from: '999999999',
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "Access-Control-Allow-Origin" : '*'
            },
        })
            .then((response) => response.json())
            .then((data) => (answer = data.answer))
            .catch((error) => {
                //handle error
            });
    }

	async function add() {
		const response = await fetch('/api/add', {
			method: 'POST',
			body: JSON.stringify({ a, b }),
			headers: {
				'content-type': 'application/json'
			}
		});

		total = await response.json();
	}
</script>

<input type="text" name="prompt" id="prompt" placeholder="Escribe aqui.." />
<!-- <input type="number" bind:value={a}> +
<input type="number" bind:value={b}> =
{total} -->

<!-- <button on:click={add}>Calculate</button> -->
<Button on:click={() => askApi()}>
    Ask AI
</Button>

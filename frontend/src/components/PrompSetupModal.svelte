<script lang="ts">
	import { PlusSolid } from 'flowbite-svelte-icons';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
  import API_URL from '$lib/constants';

  export let modalIsOpen: boolean = false;
  let newContext: string;
	
  let botPersona: string;
  let botObjective: string;

  let questionsAndAnswers = [];

  function editContext(newContext: string) {
    newContext = botObjective + "\n" + botObjective; 
		fetch(API_URL + 'edit-context', {
			method: 'POST',
			body: JSON.stringify({
				newContext: newContext
			})
		});
	}

  function addQA(){
    questionsAndAnswers = [...questionsAndAnswers, {"question": '', "answer": ''}]
  }


</script>

<Modal bind:open={modalIsOpen} outsideclose>
	<form class="flex flex-col space-y-6" action="#">
		<h2 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">
			Cambia el comportamiento del bot.
		</h2>
		<Label class="space-y-2">
			<span>Personalidad: ¿Quien es el bot? ¿Cuales son sus actividades?</span>
			<Input type="text" name="email" placeholder="Eres un..." required />
		</Label>
		<Label class="space-y-2">
			<span>Objetivos: ¿Cual es el objetivo de bot? ¿Como sabe que ha logrado su tarea?</span>
			<Input type="text" name="password" placeholder="Tu objetivo es..." required />
		</Label>
		<Label>
			<span>Preguntas y respuestas comunes</span>
			<p>¿Como llego a su local?</p>
			<p>Tienes que caminar 5 cuatras</p>
			<Input class="my-2" type="text" name="password" placeholder="Pregunta..." required />
			<Input class="my-2" type="text" name="password" placeholder="Respuesta..." required />

      {#each questionsAndAnswers as QA, i }
      <Label>
        <span>
          Añade otra pregunta
        </span>
        <Input class="my-2" placeholder="Pregunta..." type="text" bind:value={questionsAndAnswers[i].question} />
        <Input class="my-2" placeholder="Respuesta..." type="text" bind:value={questionsAndAnswers[i].answer} />
      </Label>
      {/each}

			<Button size="xs" on:click={addQA}>
				<PlusSolid />
			</Button>
		</Label>
		<Button type="submit" class="w-full1">Guardar</Button>
	</form>
</Modal>

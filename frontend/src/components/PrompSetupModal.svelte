<script lang="ts">
	import { PlusSolid, QuoteSolid } from 'flowbite-svelte-icons';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
	import { API_URL } from '$lib/constants';
	import { context } from '$lib/store';

	export let modalIsOpen: boolean = false;

	let questionsAndAnswers: QA[] = [];

	type QA = {
		question: string;
		answer: string;
	};

	function updateContext() {
		fetch(API_URL + 'update-context', {
			method: 'POST',
			body: JSON.stringify({
				newContext: builtPrompt
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				'Access-Control-Allow-Origin': '*'
			}
		});
	}

	function addQA() {
		let pair: QA = {
			answer: "",
			question: ""
		};
		questionsAndAnswers = [...questionsAndAnswers, pair];
	}

	let builtPrompt: string = '';
	let botPersonality: string = '';
	let botObjective: string = "";
	let botGreeting: string="";

	function QAToString(questionsAndAnswers: QA[]){
		// In order to activate Svelte's reactivity, we have to mention the variable who's mutation will
		// trigger the update. By explicitly requiring an argument in function call, we effectively listen
		// to updates.
		let result: string = "";

		questionsAndAnswers.forEach(QA => {
			result = result + 'Pregunta: ' + QA.question + 'Respuesta: ' + QA.answer
		});

		return result;
	}
	$: builtPrompt = botPersonality +  '\n' + botObjective + botGreeting + QAToString(questionsAndAnswers);
</script>

<Modal bind:open={modalIsOpen} outsideclose>
	<form class="flex flex-col space-y-6" action="#">
		<h3>
			{$context}
		</h3>
		<h3>
			{builtPrompt}
		</h3>
		<h3>
			{#each questionsAndAnswers as QA}
				<div>
					<div>

						Pregunta: {QA.question}
					</div>
					<div>

						Respuesta: {QA.answer}
					</div>
				</div>
			{/each}
		</h3>
		<h2 class="text-xl font-medium text-gray-900 dark:text-white">
			Cambia el comportamiento del bot.
		</h2>
		<Label class="space-y-2">
			<span>Personalidad: ¿Quien es el bot? ¿Cuales son sus actividades?</span>
			<Input bind:value={botPersonality} type="text" name="persona" placeholder="Eres un..." required />
		</Label>
		<Label class="space-y-2">
			<span>Objetivos: ¿Cual es el objetivo de bot? ¿Como sabe que ha logrado su tarea?</span>
			<Input bind:value={botObjective} type="text" name="objective" placeholder="Tu objetivo es..." required />
		</Label>
		<Label class="space-y-2">
			<span>Saludi: Escribe un saludo personalizado</span>
			<Input bind:value={botGreeting} type="text" name="greeting" placeholder="¡Hola!" required />
		</Label>
		<Label>
			<span>Preguntas y respuestas comunes</span>
			<p>¿Como llego a su local?</p>
			<p>Tienes que caminar 5 cuatras</p>

			{#each questionsAndAnswers as QA, i}
				<Label>
					<span> Añade otra pregunta </span>
					<Input
						class="my-2"
						placeholder="Pregunta..."
						type="text"
						bind:value={questionsAndAnswers[i].question}
					/>
					<Input
						class="my-2"
						placeholder="Respuesta..."
						type="text"
						bind:value={questionsAndAnswers[i].answer}

					/>
				</Label>
			{/each}

			<Button size="xs" on:click={addQA}>
				<span> Nueva pregunta </span> <PlusSolid />
			</Button>
		</Label>
		<Button type="submit" class="w-full1" on:click={updateContext}>
			Guardar
		</Button>
	</form>
</Modal>

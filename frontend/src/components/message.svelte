<script lang="ts">
	export let message: string;
	export let className: string;
	export let name: string;
</script>

<div class="my-3 rounded-xl {className}">
	<!-- <img class="w-8 h-8 rounded-full" src="" alt="Jese"> -->
	<div
		class="leading-1 flex w-full max-w-[320px] flex-col rounded-e-xl rounded-es-xl border-gray-200 p-4"
	>
		<div class="flex items-center space-x-2 rtl:space-x-reverse">
			<span class="text-sm font-semibold text-gray-900 dark:text-white">
				<!-- {#if (i + 1) % 2 == 0}
					Human
				{:else}
					Bot
				{/if} -->
				{name}
			</span>
			<span class="text-sm font-normal text-gray-500 dark:text-gray-400"
				>{new Date().toLocaleTimeString()}</span
			>
		</div>
		<p class="text-sm font-normal text-gray-900 dark:text-white">{message}</p>
	</div>
</div>

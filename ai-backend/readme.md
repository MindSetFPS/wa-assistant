# Creating Dev Container

`docker run --runtime=nvidia -v ./.:/home/wa-assistant-ai-backend -p 7861:7860 -i -t -e"TERM=xterm-256color" wa-assistant-ai-backend:0.2`

# Run with Flask

`flask --app llm_server run --host=0.0.0.0 --port=7860`
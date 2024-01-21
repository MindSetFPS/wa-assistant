FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

RUN apt update -y && apt upgrade -y

RUN apt install python3 pip -y 

RUN pip install outlines Flask

RUN pip install openai
RUN pip install transformers datasets accelerate
RUN pip install llama-cpp-python
RUN pip install mamba_ssm
RUN pip install autoawq 

ENTRYPOINT [ "/bin/bash" ]
FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

RUN apt update -y && apt upgrade -y

RUN apt install python3 pip -y 

RUN pip install outlines Flask

ENTRYPOINT [ "/bin/bash" ]
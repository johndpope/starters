# syntax=docker/dockerfile:1
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime
RUN apt-get -y update && apt-get install -y git
WORKDIR /home/unweave
ADD ./requirements.txt ./requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ADD . .
CMD ["python", "main.py"]

FROM python:3.10.13-slim

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y curl && \
    curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh && \
    pip install poetry
RUN poetry install --no-dev

CMD ["poetry", "run", "server"]

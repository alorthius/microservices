# Lab 1: Microservices Basics


### Setup

- Host and ports configs are in the [json file](services_config.json)
- Install [requirements.txt](requirements.txt)


### Running

In the root project directory run each service:
- `python -m facade.main`
- `python -m log.main <port>`, where `port` is one of preconfigured.
- `python -m messages.main`

Send requests via `curl`:
- e.g. send GET request to the Facade:  
    `curl http://127.0.0.1:8000/`
- e.g. send POST request to the Facade:  
    `curl -d '{"msg":"facade"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/`


### Results

1. Send 10 GET requests to Facade:
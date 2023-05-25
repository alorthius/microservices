# Lab 3: Microservices using Hazelcast Distributed Map


### Setup

- Host and ports configs are in the [json file](services_config.json)
- Install [requirements.txt](requirements.txt)


### Running

In the root project directory run each service:
- `python -m facade.main`
- `python -m log.main <port>`, where `<port>` is one of preconfigured.
- `python -m messages.main <port>`, where `<port>` is one of preconfigured.

Send requests via `curl`:
- e.g. send GET request to the Facade:  
    `curl http://127.0.0.1:8000/`
- e.g. send POST request to the Facade:  
    `curl -d '{"msg":"facade"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/`
- simple [bash script](post_10.bash) to make 10 POST requests to Facade


### Results

1. Send 10 POST requests to Facade:  

- Send using simple [bash script](post_10.bash)    
![](https://i.imgur.com/3HtHQZo.png)


- Facade output:  
![](https://i.imgur.com/M06fGnJ.png)


- Each Logging's outputs:
![](https://i.imgur.com/fugFCcN.png)
![](https://i.imgur.com/s5E3X9Z.png)
![](https://i.imgur.com/gZx5S84.png)


- Each Message's outputs:
![](https://i.imgur.com/trGXdQ0.png)
![](https://i.imgur.com/nFhj6Mj.png)


2. Send GET to Facade `5` times:  
![](https://i.imgur.com/6JWDfDJ.png)

As we can see, the output is different, as the Message's instances have separate values and on GET we select a random instance.
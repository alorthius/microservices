# Lab 5: Microservices with Consul


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

1. Initialize consul via `consul agent -dev` and put hz map and queue names to consul using [init_consul.sh](init_consul.sh):  

![](https://i.imgur.com/D9Nzayj.png)

Consul info on `http://localhost:8500/`:  
![](https://i.imgur.com/VyArAUd.png)


2. Send 10 POST requests to Facade using simple [bash script](post_10.bash):

![](https://i.imgur.com/AOocU8Y.png)


- Facade output:  
![](https://i.imgur.com/txTfL5v.png)


- Each Logging's outputs:
![](https://i.imgur.com/PtLZZj1.png)
![](https://i.imgur.com/8baJJux.png)
![](https://i.imgur.com/edhamLt.png)


- Each Message's outputs:
![](https://i.imgur.com/yBt36bK.png)
![](https://i.imgur.com/IMNtyLx.png)


2. Send GET to Facade `5` times:  
![](https://i.imgur.com/vQnINea.png)

As we can see, the output is different, as the Message's instances have separate values and on GET we select a random instance.
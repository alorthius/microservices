# Lab 3: Microservices using Hazelcast Distributed Map


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
- simple [bash script](post_10.bash) to make 10 POST requests to Facade


### Results

1. Send 10 POST requests to Facade:  

- Send using simple [bash script](post_10.bash)  
![](https://i.imgur.com/lhwlNZX.png)  

- Facade output:  
![](https://i.imgur.com/ucq8TPR.png)  

- Each Logging's outputs:  
![](https://i.imgur.com/1xUwDNz.png)  
![](https://i.imgur.com/whiEAjf.png)  
![](https://i.imgur.com/57Ru6bI.png)  

2. Send GET to Facade:  
![](https://i.imgur.com/4l7eViN.png)  

3. Kill two Logging services (on ports 8002 and 8003) and send GET to Facade:  
![](https://i.imgur.com/OrW78m2.png)  

Facade output:  
![](https://i.imgur.com/BHc82nC.png)    

4. Sent again 10 POST requests to Facade:  
Facade output:  
![](https://i.imgur.com/thYr0RZ.png)

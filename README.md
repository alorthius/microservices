# Lab 1: Microservices Basics


### Setup

- Host and ports configs are in the [json file](services_config.json)
- Install [requirements.txt](requirements.txt)


### Running

In the root project directory run each service:
- `python -m facade.main`
- `python -m log.main`
- `python -m models.main`

Send requests via `curl`:
- e.g. send GET request to the Facade:  
    `curl http://127.0.0.1:8000/`
- e.g. send POST request to the Facade:  
    `curl -d '{"msg":"facade"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/`


### Results

1. Startup all the services

2. 
   1. Send GET to the `log`:
   ![img_2.png](img/img_2.png)

   2. Send POST to the `log`:
   ![img_3.png](img/img_3.png)

   3. Send GET to the `log`:
   ![img_4.png](img/img_4.png)

   4. Log output:
   ![img_8.png](img/img_8.png)

3. 
   1. Send GET to the `messages`:
   ![img_5.png](img/img_5.png)

   2. Send POST to the `messages` (as we should not implement it):
   ![img_6.png](img/img_6.png)

   3. Messages output:
   ![img_9.png](img/img_9.png)

4. 
   1. Send GET to the `facade`:
   ![img_7.png](img/img_7.png)

   2. Send POST to the `facade` 2 times:
   ![img_10.png](img/img_10.png)

   3. Send GET to the `facade`:
   ![img_11.png](img/img_11.png)![img_7.png](img/img_7.png)
   
   4. All services output:
   ![img_12.png](img/img_12.png)
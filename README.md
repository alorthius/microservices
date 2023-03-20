# Lab 2: Hazelcast basics

### Task 1

![](https://i.imgur.com/yfLaMYa.png)

- After shutting down first member:  
![](https://i.imgur.com/WQVgz24.png)

- After shutting down second member:  
![](https://i.imgur.com/Bm8KuQR.png)


### Task 2

- a. Raced:  
![](https://i.imgur.com/mW9m7VY.png)

- b. Pessimistic:  
![](https://i.imgur.com/edjB9f2.png)

- c. Optimistic:  
![](https://i.imgur.com/sazE1wS.png)


### Task 3

- The readers have no conflicts and all the read threads (2) stop after reading poison pill -1, which is added as the very last queue dummy node item:

![](https://i.imgur.com/dLujjiP.png)

- If only producer is writing the items to the queue without reading, the execution will be paused as we reach queue elements limit and don't pop the elements

# asyncTime
Calculating time with and without async
- By the results, I can say that GIL is working, doing the same work in 5 Threads than in main thread is not faster.
- But multiprocessing time differs. We can see that calculating not very hard calculations by multiprocessing is even slower, when actions - with rather big and hard calculations are faster. I provide you with three graphs.
- By the first graph we can see that multiprocessing is odd while working with small numbers.
- By the last graph we can see that multiprocessibg is faster than Threads with big numbers.
- Second graph just shows when the advantage goes from Threads to multiprocessing
## Results
- ![Alt text](graphic.png?raw=true "Nums")
- Threads are linear and multiprocessing time is not very trustful
- ![Alt text](graphicBIGNUM.png?raw=true "Big Nums")
- Threads are linear and multiprocessing time increase slower then thread
- ![Alt text](graphicVERYBIGNUM.png?raw=true "Very Big Nums")
- Here we can see advantage of multiprocessing rather than threads

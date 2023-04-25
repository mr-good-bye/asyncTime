# AsyncTime
Calculating time with and without async
- By the results, I can say that GIL is working, doing the same work in 6 Threads than in one is not faster.
- But multiprocessing time differs. We can see that calculating not very hard calculations by multiprocessing is even slower, but with rather big and hard calculations are faster.

## Results

- one     - No async
- t2      - Threading, 2 threads
- t6      - Threading, 6 threads
- mp_2    - Multiprocessing, 2 processes
- mp_6    - Multiprocessing, 6 processes
- async_6 - Asyncio, 6 threads

Here we can see that main thread, Threading and asyncio have the same time, when multiprocessing calculations are faster.

![Alt text](visual.png?raw=true "Full Graph")

```    'one'faster than 'one' by 1.0
     't2'faster than 'one' by 1.0035262095048139
     't6'faster than 'one' by 1.002758486863281
   'mp_2'faster than 'one' by 1.835098695624356
   'mp_6'faster than 'one' by 4.227536785628979
'async_6'faster than 'one' by 0.9837159203216934
```

So async is not really faster, even slower
threading has no opportunities in calculations
Multiprocessing is faster.

This picture shows, that multiprocessing have like equal calculation time for small-med numbers
, where others have the linear dependence

![Alt text](visual_low.png?raw=true "Low Graph")


> I would love to get your ideas in Issues/PRs/Discussions
> 
> Feel free to provide your opinion <3
> 
> @Nikita Trubitsyn

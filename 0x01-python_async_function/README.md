# Python - Async 
## Resources
### Notes:
1. async functions return coroutine objects. Those coroutines won't be executed until it's awaited or until it's wrapped inside a task object.

2. A Task is a way to schedule coroutines to run as soon as possible instead of waiting for each one.

3. `asyncio.run` will execute a coroutine and return the result (no async/await needed).

#### Read or watch:

* Async IO in Python: A Complete Walkthrough
* asyncio - Asynchronous I/O
* random.uniform
* https://www.youtube.com/watch?v=Qb9s3UiMSTA  

## Learning Objectives

At the end of this project, expected to be able to explain to anyone, without the help of Google:

* `async` and `await` syntax
* How to execute an async program with `asyncio`
* How to run concurrent coroutines
* How to create `asyncio` tasks
* How to use the `random` module

## Requirements
General

* A `README.md` file, at the root of the folder of the project, is mandatory
* All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All files should end with a new line
* All files must be executable
* The length of files will be tested using wc
* The first line of all files should be exactly `#!/usr/bin/env python3`
* code should use the `pycodestyle` style (version 2.5.x)
* All functions and coroutines must be type-annotated.
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## imp tasks:

### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```


### 1. **`asyncio.create_task`**

- **Purpose**: `create_task` is used to schedule a coroutine for execution without waiting for it to complete immediately. It allows the event loop to continue running other tasks while this one is executing in the background.

- **Example**: 
  ```python
  task = asyncio.create_task(my_coroutine())  # Schedule my_coroutine to run in the background
  ```

- **How it works**: When you call `create_task`, it creates a task object that will run the coroutine concurrently. This is important when you want to run multiple coroutines at once without blocking each other.

### 2. **`asyncio.gather`**

- **Purpose**: `gather` runs multiple coroutines concurrently and collects the results in the order they were passed.

- **Example**:
  ```python
  results = await asyncio.gather(wait_random(3), wait_random(2), wait_random(5))
  print(results)  # Output will be [delay_1, delay_2, delay_3], in the same order
  ```

- **How it works**: `gather` runs the given coroutines concurrently but collects their results in the same order they were provided. It does not wait for one to finish before starting the next, but it will return the results in the same order you called the coroutines.

### 3. **`asyncio.as_completed`**

- **Purpose**: `as_completed` returns an iterator of coroutines that yields as each one completes. This is different from `gather`, which returns results in the order the coroutines were provided. `as_completed` gives results in the order they finish.

- **Example**:
  ```python
  tasks = [wait_random(3), wait_random(2), wait_random(5)]
  for completed_task in asyncio.as_completed(tasks):
      result = await completed_task
      print(result)  # Output will be printed as each task finishes, not necessarily in order.
  ```

- **How it works**: This is useful when you want to handle results as soon as any of the tasks completes rather than waiting for all tasks to complete first. 

### 4. **Using `as_completed` with `create_task`**

- When you want to run tasks concurrently and collect the results as they complete (in the order of completion rather than submission), you can combine `create_task` and `as_completed`.

### Example: Using `create_task` and `as_completed`

Let's fix your example so it returns the list in the order that the coroutines complete (without using `sort()`):

```python
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    
    for task in asyncio.as_completed(tasks):  # Handle tasks as they complete
        result = await task
        results.append(result)
        
    return results

# Test code
print(asyncio.run(wait_n(5, 5)))
```

### Comparison of `gather` vs `as_completed`:

- **`gather`**: Waits for all tasks to complete and returns the results in the same order as the tasks were started.
  
  ```python
  results = await asyncio.gather(task1, task2, task3)
  ```

- **`as_completed`**: Yields each task's result as soon as it completes, allowing you to handle them in the order of completion, which is helpful when task durations vary.

  ```python
  for task in asyncio.as_completed([task1, task2, task3]):
      result = await task
  ```

### Key points:
- Use `create_task` to run a coroutine concurrently.
- Use `gather` when you want results in the order tasks are provided.
- Use `as_completed` when you want results as they complete, regardless of their order.

### Example to solve on your own:
1. Modify the code so it only prints the result when a task is completed.
2. Try using `asyncio.gather` and see the difference in behavior compared to `as_completed`.

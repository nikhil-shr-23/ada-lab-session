from memory_profiler import profile
import time 

def my_prgram():
    total = 0
    for i in range(100000000):
        total += i
    return total


start_time = time.time()
mem_usage= memmory+usage(my_program)
end_time = time.time()

print("Memory usage:", mem_usage)
print("Time taken:", end_time - start_time)
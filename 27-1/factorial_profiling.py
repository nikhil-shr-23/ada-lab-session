from memory_profiler import memory_usage
import time
import sys


sys.set_int_max_str_digits(0) 

def factorial_program(num):
    fact = 1
    if num < 0:
        return "no negative numvers"
    elif num == 0:
        return "factorial of 0 is 1"
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact


        

if __name__ == "__main__":
    try:
        print("number enter crow: ", end="", flush=True) 
        line = sys.stdin.readline()
        if not line:
            print("No input provided.")
            sys.exit(1)
        num = int(line.strip())
        
        print(f"\nProfiling factorial logic for input: {num}...")

        start_time = time.time()
        
        mem_usage, result = memory_usage((factorial_program, (num,), {}), max_usage=True, retval=True)
        
        end_time = time.time()

        if isinstance(result, str):
            print(result)
        else:
             print("factorial of", num, "is", result)

        print("\n" + "="*30)
        print(f"Memory usage: {mem_usage} MiB")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        print("="*30)
        
    except ValueError:
        print("Invalid input! Please enter an integer.")

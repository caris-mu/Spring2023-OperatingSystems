# Write code in any language which will write code to Multiply every value in a array with Random value between 0.1 to 0.9 
# Calculate the sum of the array in parallel and serial and compute the time difference. 
import random
import threading
import time

def run_single_thread(multiplied_arr):
    # Calculate the sum of the array 
    arr_sum = sum(multiplied_arr)
    # Print the results
    print("Single thread sum:", round(arr_sum))
    
def run_multi_thread(multiplied_arr, num_threads):
    # Shared value is actually in a arr_sum list
    arr_sum = [0]
    threadLock = threading.Lock()

    def multiply_and_sum(calc_arr, i, arr_sum):
        # Calculate the sum of the new array and store it in the result arr
        with threadLock:
            arr_sum[0] += sum(calc_arr)

    # Decide how many threads you want to use
    threads = []
    arr_size = len(arr)
    arr_size_per_thread = arr_size // num_threads

    # Decide task for each thread = decide input for each thread and init thread object
    for i in range(num_threads):
        t = threading.Thread(target=multiply_and_sum, args=(multiplied_arr[i * arr_size_per_thread : (i + 1) * arr_size_per_thread], i, arr_sum))
        threads.append(t)

    # Start threads.
    for t in threads:
        t.start()

    # Collect results from each thread.
    for t in threads:
        t.join()

    print("Multi threads sum:", round(arr_sum[0]))


if __name__ == "__main__":
    arr = [random.randint(1,100) for i in range(50000000)]

    # Generate a random value between 0.1 and 0.9
    random_val = round(random.uniform(0.1, 0.9), 2)

    # Multiply arr with the random value 
    multiplied_arr = [round(x * random_val, 2) for x in arr]

    # print("Original array:", arr)
    print("Random value:", random_val)
    # print("Multiplied array:", multiplied_arr)

    # Compute the time taken 
    start_time = time.time()

    run_single_thread(multiplied_arr)

    # Compute the time taken to execute the multiplication and sum in serial
    end_time = time.time()
    time_taken = end_time - start_time

    print("Single thread time:", time_taken)


    # Compute the time taken 
    start_time = time.time()
    run_multi_thread(multiplied_arr, num_threads=5)
    # Compute the time taken to execute the multiplication and sum in parallel threads
    end_time = time.time()
    time_taken = end_time - start_time

    # Print the results
    print("Multi threads time:", time_taken)

# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    next_free_time = [0] * n
    output = []
    for job_id in range(m):
        min_thread_id = 0
        for i in range(1, n):
            if next_free_time[i] < next_free_time[min_thread_id]:
                min_thread_id = 1
    result.append((min_thread_id, next_free_time[min_thread_id]))
    next_free_time[min_thread_id] += data[job_id]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_id, start_time in output:
        print(thread_id, start_time)



if __name__ == "__main__":
    main()

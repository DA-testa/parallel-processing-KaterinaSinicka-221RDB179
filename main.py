# python3

def parallel_processing(n, m, data):
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(i,0) for i in range(n)]
    output = []

    for job in range(m):
        thread = min(threads, key=lambda x: x[1])
        output.append((thread[0], thread[1]))
        threads[threads.index(thread)] = (thread[0],thread[1] + data[job])

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    output = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, start_time in output:
        print(thread, start_time)

if __name__ == "__main__":
    main()

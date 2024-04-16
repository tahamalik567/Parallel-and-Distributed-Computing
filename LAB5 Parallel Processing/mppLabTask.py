from multiprocessing import Pool
import multiprocessing
import time


# def f(x):
#     return x*x

# if __name__ == '__main__':
#     start = time.time()
#     pool = Pool(processes=4)
#     for x in range(10):
#         pool.apply(f, (x,))
#     pool.close()
#     pool.join()
#     end = time.time()
#     print(f"Execution time apply: {end - start:.4f} seconds")


# def f(x):
#     curr_proc = multiprocessing.current_process()
#     print(" ",x*x," is executing by : ",curr_proc.name)
# if __name__ == '__main__':
#     curr_proc = multiprocessing.current_process()
#     pool = Pool(processes=4)
#     for x in range(30000):
#         P = pool.map_async(f, (x,))
#         print ('\nHERE : process is :',curr_proc.name,"\n")
#         print ('\nMORE : process is :',curr_proc.name,"\n")
#         # r.wait()
#         print ('\nDONE process is :',curr_proc.name,"\n")


from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    for x in range(30000):
        pool.apply(f, (x,))
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time apply: {end - start:.4f} seconds")


def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    results = [pool.apply_async(f, (x,)) for x in range(30000)]
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time apply_async: {end - start:.4f} seconds")


    from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    results = pool.map(f, range(30000))
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time map: {end - start:.4f} seconds")


    from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    results = pool.map_async(f, range(30000))
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time map_async: {end - start:.4f} seconds")


from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    results = pool.starmap(f, [(x,) for x in range(30000)])
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time starmap: {end - start:.4f} seconds")


from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=4)
    results = pool.starmap_async(f, [(x,) for x in range(30000)])
    pool.close()
    pool.join()
    end = time.time()
    print(f"Execution time starmap_async: {end - start:.4f} seconds")


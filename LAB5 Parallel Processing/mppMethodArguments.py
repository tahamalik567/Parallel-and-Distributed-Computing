import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool

from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    # Create a Pool with 4 processes
    with Pool(4) as pool:
        # Issue a task to the process pool
        result = pool.apply(square, (10,))

    print(f"The square of 10 is: {result}")



def square(x):
    return x * x

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=4) as pool:
        result = pool.map(square, numbers)
    print("Squared numbers:", result)



from multiprocessing import Pool

def product(a, b):
    return a * b

if __name__ == '__main__':
    pairs = [(2, 3), (4, 5), (6, 7)]
    with Pool(processes=4) as pool:
        result = pool.starmap(product, pairs)
    print("Products:", result)
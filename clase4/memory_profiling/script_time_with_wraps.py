import time
from functools import wraps

value_to_print=1

# wraps nos permite que no se pierda el proposito de cada funcion al repetir con un decorador

def diff_time(func):
    @wraps(func)
    def wrappper():
        """This is a wrapper"""
        starttime = time.time()
        #print(starttime)
        func()
        end_time=time.time()
        #print(end_time)
        #return end_time-starttime
    return wrappper

@diff_time
def main():
    """This is the main function"""
    print(main.__name__)
    print(main.__doc__)
    for i in range(100):
        i
        #print(f"{value_to_print},corrida numero{i}")

if __name__=="__main__":
    main()
    

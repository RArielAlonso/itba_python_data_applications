import time

value_to_print=1

def diff_time(func):
    def wrappper():
        starttime = time.time()
        print(starttime)
        func()
        end_time=time.time()
        print(end_time)
        return end_time-starttime
    return wrappper

@diff_time
def main():
    for i in range(10000):
        i
        print(f"{value_to_print},corrida numero{i}")

if __name__=="__main__":
    print(main())
    

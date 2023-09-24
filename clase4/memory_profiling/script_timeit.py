import timeit

value_to_print=1

def main():
    for i in range(10):
        #print(value_to_print)
        value_to_print

if __name__=="__main__":
    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    for i in range(1000000):
        main()
    print("The time difference is :", timeit.default_timer() - starttime)
 

from functools import reduce
min = lambda x , y: x if x < y else y

def main():
    a = [55,66,77,88,999]
    b  = reduce(min , a)
    print("the smallest number is :",b)

if __name__ == "__main__":
    main()
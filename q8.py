num = lambda x : x if x % 3 == 0 and x % 5 == 0 else None

def main():
    a = [55,33,44,66,77,88,1,2,3,6,89,15,30,45,60]
    b = list(filter(num,a))
    print("final result is :",b) 


if __name__ =="__main__":
    main()
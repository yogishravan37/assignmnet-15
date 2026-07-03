from functools import reduce
sum = lambda x , y : x + y

def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    result = reduce(sum,a)
    print("the addition is : ",result)

if __name__ == "__main__":
    main()
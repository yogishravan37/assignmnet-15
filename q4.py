from functools import reduce

addition = lambda x , y: x + y

def main():
    data = [1,2,3,4,5,6,78,9]
    result = reduce(addition,data)
    print("sum of all numbers is :",result)

main()

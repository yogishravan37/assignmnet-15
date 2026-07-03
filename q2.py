check_even = lambda  x : x % 2 == 0

def main():
    a = [10,3,6,7,8,2,1,9]
    result = list(filter(check_even,a))
    print("result is : ",result)

if __name__ == "__main__":
    main()
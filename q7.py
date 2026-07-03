check = lambda x : x if x > 5 else None

def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = list(filter(check,a))
    print("final result is : ",b)

if __name__ == "__main__":
    main()

odd = lambda x: x % 2 != 0

def main():
    a = [1,2,3,4,5,6,7,8,8,9,10]
    b = list(filter(odd,a))
    print("odd numbers are :",b)

if __name__ == "__main__":
    main()
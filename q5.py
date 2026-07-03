from functools import reduce
max = lambda x, y: x if x > y else y

def main():
    a = [55,99,75,69,22,47]
    b = reduce(max,a)
    print("the maximum number is :",b)

if __name__ == "__main__":
    main()
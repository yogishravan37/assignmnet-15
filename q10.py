count = lambda x : x if x % 2==0  else None

def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = len(list(filter(count,a)))
    print("final result is :",b)

main()
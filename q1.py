sqr = lambda x: x*x

def main():
    a = [11,12,13,14,15]
    result = list(map(sqr,a))
    print("result is :",result)


if __name__=="__main__":
    main()
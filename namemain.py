def sum(a,b):
    print("__name__ : ",__name__)
    return a+b

if __name__ == "__main__":
    print("__name__ : ",__name__)
    sum = sum(5,6)
    print("Sum : ",sum)
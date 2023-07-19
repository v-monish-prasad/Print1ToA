def print1ToA(number):
    if number == 1:
        print(1, end=' ')
    else:
        print1ToA(number - 1)
        print(number, end=' ')


if __name__ == "__main__":
    A = int(input())

    print1ToA(A)
    print()

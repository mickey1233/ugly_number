def isugly(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        elif n % 3 == 0:
            n = int(n / 3)
        elif n % 5 == 0:
            n = int(n / 5)
        else:
            return False
    return True


def main():
    print(isugly(6))
    print(isugly(8))
    print(isugly(14))
    print(isugly(1))
    print(isugly(-123123))
    print(isugly(23524656))


if __name__ == "__main__":
    main()

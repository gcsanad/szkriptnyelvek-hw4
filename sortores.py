import sys
import random as r

UPTO = 100


def main():
    index = 9
    for i in range(UPTO):
        if i == index:
            print(r.randint(0, 9), end="\n")
            index += 10
        else:
            print(r.randint(0, 9), end="")
    print()

if __name__ == "__main__":
    main()
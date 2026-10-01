def elsoValtozat():
    return sum(range(1, 101))

def szamjegyekOsszege():
    osszeg = 0
    for i in range(1, 101):
        for o in str(i):
            osszeg += int(o)
    return osszeg



def main():
    print("Az 1-től 100-ig terjedő számok összege: ", elsoValtozat())
    print("A számjegyek összege: ", szamjegyekOsszege())

if __name__ == "__main__":
    main()
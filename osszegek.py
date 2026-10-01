def main():
    elsoSzazNegyzetosszege = sum(i ** 2 for i in range(1, 101))
    print(f"Az első száz szám négyzetének összege: {elsoSzazNegyzetosszege}")
    elsoSzazOsszegenekNegyzet = sum(range(1, 101)) ** 2
    print(f"Az első száz szám összegének négyzete: {elsoSzazOsszegenekNegyzet}")
    kulonbseg = elsoSzazOsszegenekNegyzet - elsoSzazNegyzetosszege
    print(f"A különbség: {kulonbseg}")

if __name__ == "__main__":
    main()
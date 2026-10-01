def gyemant(magassag):
    if magassag % 2 == 0:
        print("A gyémánt magassága páros szám, kérlek adj meg páratlan számot!")
    else:
        for i in range(1, magassag + 1, 2):
            print(" " * ((magassag - i) // 2) + "*" * i)
        for i in range(magassag - 2, 0, -2):
            print(" " * ((magassag - i) // 2) + "*" * i)

def main():
    magassag = int(input("Adja meg a gyémánt magasságát: "))
    gyemant(magassag)
    
if __name__ == "__main__":
    main()
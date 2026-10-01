def hangrendEldontes(szo):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    mely = False
    magas = False
    for betu in szo:
        if betu in MELY_MGHK:
            mely = True
        elif betu in MAGAS_MGHK:
            magas = True
    if mely and magas:
        return "Vegyes hangrendű"
    elif mely:
        return "Mély hangrendű"
    elif magas:
        return "Magas hangrendű"
    else:
        return "Nincs magánhangzó a szóban!"


def main():
    szo = input("Kérem a szót: ")
    eredmeny = hangrendEldontes(szo)
    print(f"A(z) '{szo}' szó hangrendje: {eredmeny}")

if __name__ == "__main__":
    main()
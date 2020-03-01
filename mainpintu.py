import pintu

if __name__ == "__main__":
    listnama = ["ilham","santi","ricca"]
    listketuk = [3,4,1]
    listwaktu = [3,4,12]

    listpintu = []

    for i in range(3):
        listpintu.append(pintu.pintu(listnama[i], listketuk[i], listwaktu[i]))

    for pintu in listpintu:
        pintu.buka()
        pintu.tutup()

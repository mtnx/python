baris = 0
kolom = 0
inputan = input("input : ")
batas = int(inputan)
x = ""

while baris < batas:
    kolom = 0
    kolom = kolom + baris
    while kolom < batas:
        x = x + " " + " "
        kolom = kolom + 1

    kolom = 0
    while kolom <= baris:
        x = x + "*" + " "
        kolom = kolom + 1


    x = x + "\n"
    baris = baris + 1
print(x)
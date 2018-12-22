baris = 0
inp = input("nilai : ")
batas = int(inp)
s = ""
print("\n")


while baris < batas:
    kolom = 0
    no = batas
    while kolom < batas:
        s = s + str(no) + " "
        kolom = kolom + 1
        no = no - 1
    s = s + "\n"
    baris = baris + 1
print(s)


# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1
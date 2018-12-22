a = 1
s = ""
x = 1

# baris loop
while a < 5:
    b = 0
    y = 1
    
    # kolom loop
    while b < 10:
        
        s = s + "[" + str(x) + "." + str(y) + "]" + " "
        b = b + 1
        y+= 1

    s = s + "\n"
    a = a + 1
    x+= 1

print(s)
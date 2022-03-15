print("""Road = a (up / down), s (left / right)
Grass = q
Barriers = w (0), e(90), r(180) t (270)
Turn barriers = y(0), u(90), i(180), o(270)
Turn = z(0), x(90), c(180), v(270)

Finish = n (up / down), m (left / right)""")


run = True
totallines = "{"
txt = """-1,-1,-1,-1,-1,-1,5,-1,-1,-1
-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
5,-1,5,12,2,2,2,2,14,-1
-1,-1,5,0,-1,-1,-1,-1,1,5
-1,-1,5,0,-1,-1,-1,-1,1,-1
-1,-1,5,0,-1,-1,-1,-1,1,-1
-1,-1,5,0,-1,-1,-1,-1,1,-1
-1,-1,5,0,-1,-1,-1,-1,17,-1
-1,-1,-1,5,-1,-1,-1,-1,5,-1
""".splitlines()

convert = {-1: 'q', 0: 'a', 1: 'a', 2: 's', 3:'s', 4:'w', 5:'e', 6:'r', 7:'t', 8:'y', 9:'u', 10:'i', 11:'0', 12:'z', 13:'x',14:'c',15:'v',16:'n',17:'n',18:'m',19:'m'}

for currentline in txt:
    
    
    currentlinestr = "{"
    for x in currentline:
        try:
            x1 = convert[int(x)]
        except:
            x1 = 'q'
        currentlinestr += f"'{x1}',"

    currentlinestr += "},"

    totallines += currentlinestr

totallines += "}"

print(totallines)
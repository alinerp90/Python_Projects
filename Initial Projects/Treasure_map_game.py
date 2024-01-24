line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print(" A1  A2  A3 \n B1  B2  B3  \n C1  C2  C3")
print("Hiding your treasure! X marks the spot.")
position = input().upper()


x2 = position[0] #letra a b c
x1 = int(position[1]) - 1  #numero 1 2 3

if x2 == "A":
    x2 = 0
elif x2 == "B":
    x2 = 1
else:
    x2 = 2

for m in map:
    map[x1][x2] = "X"

print(f"{line1}\n{line2}\n{line3}")

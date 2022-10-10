matrix=[
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
]
ans = []
lRow= len(matrix)
lCol=len(matrix[0])
print(lCol)
print(lRow)
seen = [[0 for i in range(lRow)] for j in range(lCol)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
    #->  v  <-  ^
x = 0
y = 0
di = 0

for i in range(lCol * lRow):
    ans.append(matrix[x][y])
    seen[x][y] = True
    # vad care este locul unde "ar trebui" sa merg
    cr = x + dr[di]
    cc = y + dc[di]
#verific sa fiu in bounds si sa nu fi vazut caracterul urmator conform directiei de mers
    if (0 <= cr and cr < lCol and 0 <= cc and cc < lRow and not (seen[cr][cc])):
        x = cr
        y = cc
#daca am iesit din bounds trebuie sa schimb directia
    else:
        #schimb directia de mers
        di = (di + 1) % 4
        #actualizez coloana si randul
        x += dr[di]
        y += dc[di]



print(ans)
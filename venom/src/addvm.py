s = open("final.bf").read().split('\n')[:-1]
j = [[i for i in j] for j in s]
for i in j:
    print(len(i))
x = 0
y = 0
d = 0
# right, left, down, up
d2 = [(1,0),(-1,0),(0,1),(0,-1)]
g = [0, 42, 0, 57, 0, 49, 0, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 72, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 191, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 87, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 157, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 222, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 212, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 69, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 43, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 44, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 174, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 252, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 74, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 148, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 6, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 228, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 22, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 4, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 105, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 59, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 186, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 87, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 137, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 206, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 54, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 8, 1, 0, 1, 0, 3, 1, 4, 1, 4, 3, 3, 1, 0, 1, 4, 3, 3, 7, 41, 1, 3, 3, 1, 5, 3, 2, 3, 2, 4, 1, 0, 1, 1, 5, 1, 2, 4, 9, 2, 0, 6]
ii = 0
a = False
while ii < len(g):
    if j[y][x] == '>':
        d = 0
    elif j[y][x] == '<':
        d = 1
    elif j[y][x] == 'v':
        d = 2
    elif j[y][x] == '^':
        d = 3
    elif j[y][x] == '"':
        a = not a
    elif a:
        j[y][x] = chr(g[ii])
        ii += 1
    x += d2[d][0]
    y += d2[d][1]
    print(x,y,ii,len(g))
print(j)
b = bytes('\n'.join([''.join(k) for k in j]),encoding='utf8')
s2 = open("final2.bf","wb").write(b)
j2 = []
for i in range(53):
    j3 = [0]*len(j2)
    j2 += [42^ord(j[(i*29)%53][(k*29)%53]) for k in range(53)]
print(j2)
open("final3.bf","w").write(str(j2)[1:-1])
print(j)
print(len(j2))
# a = 1
# b = 20
# print (a+b)

# Create matrix
mtx = []
x = 4
y = 5
for i in range (x):
    # print (i)
    r = []
    for j in range (y):
      # print (i, j)
      r.append (i**j)
      # print (r)
    mtx.append (r)


# Print matrix

for i in range (len (mtx)):
    # print (i, mtx[i])
    for j in range (len (mtx[i])):
        # print (i, j, mtx[i][j], end = '')
        # print(mtx[i][j], end='')
        # print(mtx[i][j], end=' ')
        print(mtx[i][j], end='\t')
    print ()




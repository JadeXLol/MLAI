x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

#for i in x:
    #print(i)

#for i in range(len(x)):
    #print(x[i])

xy = []

for i in range(len(x)):
    xy.append([x[i],[y[i]]])
print(xy)

print(f"x list is {x}, and y list is {y}")
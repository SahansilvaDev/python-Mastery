for x in range(1, 6):
    if x == 3:
        continue # skip the x = 3 iteration
    print(x)


print("----------------")

i =0
while i <5:
    i += 1
    if i == 3:
        continue
    print(i)

print("----------------")

for x in range(1, 6):
    if x == 3:
        break  # exit the loop when x is 3
    print(x)


print("----------------")

i =0
while i <5:
    i += 1
    if i == 3:
        break
    print(i)

print("----------------")


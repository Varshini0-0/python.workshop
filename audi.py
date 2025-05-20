audi = []
audi1 = []
for i in range(6):
    audi1.append(2)
audi2 = []
for i in range(10):
    audi2.append(2)
audi3 = []
for i in range(6):
    audi3.append(2)
audi.extend([audi1, audi2, audi3])
for index, matrix in enumerate(audi, start=1):
    print(f"\naudi {index}:")
    for row in matrix:
        print(row)
print(f"{audi1} {audi2} {audi3}")

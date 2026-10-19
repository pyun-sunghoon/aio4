"""
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8\n\n\n\n")

for dan in range(2,10):
    for i in range(1,10):
        print(f"{dan} x {i} = {2*i}", end="\t")
    print("")

for i in range(1,9):
    for dan in range(2,10):
        print(f"{dan} x {i} = {dan*i}", end="\t")
    print();
"""
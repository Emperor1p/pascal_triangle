from math import comb
num_rows = int(input("Enter the number of row you want: "))
print(f"The pascal triangle value {num_rows} is")
for row in range (num_rows):
    for col in range(row + 1):
        value = comb(row, col)

        print(value, end=" ")

    print()


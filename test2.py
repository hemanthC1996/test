rows = int(input("Enter the number of rows "))
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
start = int(input("Enter the range: "))
if start%2 == 0:
    start -= 1
for i in range(0,start*2):
    if i%2 != 0:
        print(i)
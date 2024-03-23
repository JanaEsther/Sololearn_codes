
n = int(input())

file = open("numbers.txt", "w+")
for i in range(1, n+1):
    file.write(f"\n{i}")
file.close()

file = open("numbers.txt", "r")
print(file.read())
file.close()

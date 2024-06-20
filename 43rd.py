n = int(input("Enter matrix size: "))
arr = [[0 for _ in range(n)] for _ in range(n)]
j = n - (n - 1)

for i in range(n):
    if j < n:
        arr[i][j] = 81
        j += 2
        if j >= n:
            j = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            print(" %c |" % chr(arr[i][j]), end="")
        else:
            print("   |", end="")
    print("\n" + "-" * (4 * n))

print("\nMirror image of matrix:\n\n")
for i in range(n-1, -1, -1):
    for j in range(n):
        if arr[i][j] != 0:
            print(" %c |" % chr(arr[i][j]), end="")
        else:
            print("   |", end="")
    print("\n" + "-" * (4 * n))

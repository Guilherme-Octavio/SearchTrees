import Search.Algoritimo as src


arr = [4,7,8,12,45,99,74,21]

n = 74

k = src.Procura(arr, n)

Linear = k.LinearSearch()
binary = k.BinarySearch()

if binary == True:
    print("\n Found")
else:
    print("\n Not Found")
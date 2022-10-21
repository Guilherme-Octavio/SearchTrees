class Procura:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def LinearSearch(self):
        for i in range(0, len(self.arr)):
            if self.arr[i] == self.n:
                return True
            else:
                continue
    
    def BinarySearch(self):
        self.arr.sort()
        l = 0   
        u = len(self.arr)-1

        while l <= u:
            m = (l+u)//2

            if self.arr[m] == self.n:
                return True
            else:
                if self.arr[m] < self.n:
                    l = m + 1
                else:
                    u = m - 1
        return False




class Solution:
    def select(self, arr, i):
        return self.selectionSort(arr, i)

    def selectionSort(self, arr, n):
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return arr


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()

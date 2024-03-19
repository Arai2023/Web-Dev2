N = int(input())
array = list(map(int, input().split()))

count_greater_than_previous = 0
for i in range(1, N):
    if array[i] > array[i - 1]:
        count_greater_than_previous += 1

print(count_greater_than_previous)

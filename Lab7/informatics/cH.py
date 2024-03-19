x = int(input())
divisors = [str(i) for i in range(1, x + 1) if x % i == 0]
print(" ".join(divisors))

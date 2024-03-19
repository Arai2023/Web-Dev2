
v = int(input())
t = int(input())

if v > 0:
    position = (v * t) % 109
else:
    position = 109 - ((-v) * t) % 109

print(position)

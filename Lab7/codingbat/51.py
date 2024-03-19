def squirrel_play(temperature, is_summer):
    if is_summer:
        return 60 <= temperature <= 100
    else:
        return 60 <= temperature <= 90

# Test cases
print(squirrel_play(70, False)) # True
print(squirrel_play(95, False)) # False
print(squirrel_play(95, True))  # True

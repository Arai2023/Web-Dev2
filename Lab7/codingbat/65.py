def cat_dog(string):
    count_cat = string.count('cat')
    count_dog = string.count('dog')
    return count_cat == count_dog

# Test cases
print(cat_dog('catdog'))        # True
print(cat_dog('catcat'))        # False
print(cat_dog('1cat1cadodog'))  # True

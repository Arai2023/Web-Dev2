def double_char(str):
    result = ''
    for char in str:
        result += char * 2
    return result

# Test cases
print(double_char('The'))        # 'TThhee'
print(double_char('AAbb'))       # 'AAAAbbbb'
print(double_char('Hi-There'))   # 'HHii--TThheerree'

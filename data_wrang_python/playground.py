

double = lambda x: x * 2
print(double(5))

add = lambda x, y: x + y
print(add(3,6))

print((lambda x, y: x + y)(3,4))

check = lambda x: "big" if x > 10 else "small"
print(check(3))

sign = lambda x: "positive" if x > 10 else "negative"
print(sign(-2))

numbers = [1,2,3,4,5]
result = map(lambda x: x * 2, numbers)
print(list(result))

def get_length(x):
    return len(x)
words = ["cat", "dog", "bird"]
result = map(get_length, words)
print(result)
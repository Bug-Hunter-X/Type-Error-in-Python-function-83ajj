def function(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

result = function(5, '10')
print(result)
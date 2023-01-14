def counter(function):
    def wrapper(*args, **kwargs):
        wrapper.count = 0
        for i in range(3):
            print(f"Iter #{wrapper.count + 1}")
            function(*args, **kwargs)
            wrapper.count += 1
            
    return wrapper

@counter
def square(*args, **kwargs):
    summa = 0
    for value in args:
        summa += value ** 2
    for key, value in kwargs.items():
        summa += value ** 2
        
    return print(summa)


square(1,2,3,messi = 5)

print(square.count)

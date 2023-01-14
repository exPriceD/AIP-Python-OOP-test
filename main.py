def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = 0
        for i in range(3):
            print(f"Iter #{wrapper.count + 1}")
            func(*args, **kwargs)
            wrapper.count += 1
            
    return wrapper

@counter
def square(*args, **kwargs):
    summa = 0
    for value in args:
        try:
            summa += value ** 2
        except:
            try:
                value = int(value)
                summa += value ** 2
            except TypeError:
                exit
                
    for key, value in kwargs.items():
        try:
            summa += value ** 2
        except:
            try:
                value = int(value)
                summa += value ** 2
            except TypeError:
                exit
        
    return print(summa)


square(1,1,"2", messi = "two")


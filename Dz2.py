# Напишите функцию принимающую на вход только ключевые параметры(kwargs) 
# и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def reverse_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(reverse_kwargs(rev=True, acc="YES", stroka=4))

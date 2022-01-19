# تابعی که عدد اول و عدد دوم و عملگر را میگیرد و نتیجه را پس می دهد
def calculate(number1, number2, operator):
    if operator == '+':
        return int(number1) + int(number2)
    elif operator == '-':
        return int(number1) - int(number2)
    elif operator == '*':
        return int(number1) * int(number2)
    elif operator == '/':
        return int(number1) / int(number2)
    else:
        return "من فقط چهار عمل رو بلدم!"
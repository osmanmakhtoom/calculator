# در اینجا دو تا ماژولی که برای اعتبارسنجی و محاسبه نوشتیم را به اسکریپت اضافه میکنیم
from modules import validators, calculator

if __name__ == '__main__':
    
    # عدد اول را میگیریم و کنترل میکنیم که عدد معتبر باشد
    number1 = input("عدد اول را وارد کنید: ")
    if not validators.validate_number(number1):
        print("عدد اول نامعتبر است")
        exit()
    
    # عدد دوم را میگیریم و کنترل میکنیم که عدد معتبر باشد
    number2 = input("عدد دوم را وارد کنید: ")
    if not validators.validate_number(number2):
        print("عدد دوم نامعتبر است")
        exit()
    
    # عملگر را میگیریم و کنترل میکنیم که معتبر باشد   
    operator = input("عملگر را وارد کنید: " + "مقادیر مجاز (+,-,*,/)")
    if not validators.validate_operator(operator):
        print("عملگر نامعتبر است")
        exit()
    
    # نتیجه را محاسبه کرده و خروجی را نمایش می دهیم
    print(calculator.calculate(number1, number2, operator))
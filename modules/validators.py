# تابعی که برای اعتبارسنجی اعداد نوشتیم
def validate_number(number):
    if number.isdigit():
        return True
    else:
        return False

# تابعی که برای اعتبارسنجی عملگرهای چهار عمل اصلی نوشتیم
def validate_operator(operator):
    if operator in ('+', '-', '*', '/'):
        return True
    else:
        return False
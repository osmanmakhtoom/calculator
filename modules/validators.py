def validate_number(number):
    if number.isdigit():
        return True
    else:
        return False
    
def validate_operator(operator):
    if operator in ('+', '-', '*', '/'):
        return True
    else:
        return False
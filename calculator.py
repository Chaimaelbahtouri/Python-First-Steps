#calculator 
def add(input):
    res = input[0]
    for num in input[1:]:
        res += num
    return res
def multiplication(input):
    res = 1
    for num in input:
        res *=num
    return res
def subtraction(input):
    res= input[0]
    for num in input[1:]:
        res -=num
    return res
def division(input):
    res = input[0]
    for num in input[1:]:
        if num == 0:
            return "Invalid: Division by zero"
        res /= num
    return res
def modulo(input):
    res = input[0]
    for num in input[1:]:
        if num == 0:
            return "Invalid: Modulo by zero"
        res %= num
    return res
# 2- get numbers
def took_numbers(slices_input):
    slices = []
    grp = slices_input.split(',')
    for check in grp:
        remove = check.strip()
        remove = check.strip()
        try:
            num = float(remove)
            if num.is_integer():
                num = int(num)
            slices.append(num)
        except ValueError:
            print("Invalid input", remove)
            return []
    return slices

print("select operation : '+','-','*','/','%'")
operations = {
    '+': add,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '%': modulo
}
while True :
    choice = input(" enter your choice ")
    if choice in ('+','-','*','/','%'):
        in_put = input("Enter numbers separated by comma : ")
        numbers = took_numbers(in_put)
        if numbers:
            result = operations[choice](numbers)
            print("Result:", result)
        else:
            print("your Operation is canceled correct your operation please")
    else :
        print("Please select one of the specified operations. ")



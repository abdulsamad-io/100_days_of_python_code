def add (num1,num2):
    return num1+num2
def sub (num1,num2):
    return num1-num2
def mul (num1,num2):
    return num1*num2
def div (num1,num2):
    return num1/num2

opr_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

a = float(input("Enter the fist number: "))

opr = input("Enter the operation: + , - , * or /  : ")

current_num = a

calc_ongoing = True

while calc_ongoing:
    current_opr = opr
    for i in opr_dict:
        if i == opr:
            b = float(input("Enter the second number: "))
            our_calc = opr_dict[i](current_num, b)
            print (our_calc)
            our_calc = current_num
            print (current_num)



    #     continue_check = input("do you wan to continue? (y/n): ")
    # if continue_check == "y":
    #     our_calc = current_num
    #     print (f'Your fist number is now  {current_num}')
    #     next_opr = input("Enter the operation: + , - , * or /  : ")
    #     current_opr = next_opr











import calculator_arts

print (calculator_arts.calc_logo)

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

a = float(input("***> Enter the fist number: "))

opr = input("***> Enter the operation: + , - , * or /  : ")

opr_list = ['+','-','*','/']

current_num = a

current_opr = opr

calc_ongoing = True

if opr in opr_list:
    while calc_ongoing:
        for i in opr_dict:
            if i == current_opr:
                b = float(input("***> Enter the second number: "))
                our_calc = opr_dict[i](current_num, b)
                print (f'{current_num} {current_opr} {b} = {our_calc}')
                current_num = our_calc
                #print (current_num)
                continue_check = input("***> Do you wan to continue? (y/n): ")
                if continue_check == "n":
                    calc_ongoing = False
                    print ("***> Thank you for using this program.")
                    print(calculator_arts.calc_exit)
                else:
                    print(calculator_arts.calc_logo)
                    print (f'***> Your fist number is now  {current_num}')
                    next_opr = input("***> Enter the operation: + , - , * or /  : ")
                    current_opr = next_opr
else:
    print ("***> Wrong operation. Thank you for using this program.")
    print (calculator_arts.calc_exit)











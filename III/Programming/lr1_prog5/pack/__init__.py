from . import calcParams as CP
from . import calcLogging as CL
from . import calcPrint as CPR

def quite():
    print('Вы хотите выйти? Да/Нет')
    choise = input()
    match choise:
        case "Да":
            exit()
        case "Нет":
            main_calc()
        case _:
            print('ERROR: Проверьте правильность введенных данных')
            quite()

global res
def calc(op1, op2, act):
    match act:
        case "+":
            r = op1 + op2
        case "-":
            r = op1 - op2
        case "*":
            r = op1 * op2
        case "/":
            try:
                r = op1 / op2
            except ZeroDivisionError:
                print('На ноль делать нельзя, попробуйте снова')
                main_calc()
        case "^x":
            r = op1 ** op2
        case "%":
            r = op1 % op2
        case _:
            print('Что-то пошло не так, попробуйте снова')
            main_calc()

    try:
        CP.load_params()
        res = CP.f1(r)
    except:
        print('Не удалось загрузить параметры')
        res = r
    CL.write_log(op1, op2, action=act, result=res)
    CPR.print_result(op1, op2, act, res)
    quite()
            
def main_calc():

    CPR.print_inter()
    
    act = input('Сперва выберите действие (введите символ), или напишите Q для выхода\n')
    if act == "Q":
        exit()
    else:
        print('Введите последовательно 2 числа (порядок важен)')

    try:
      op1, op2 = float(input()), float(input())
    except:
      print('ERROR: Проверьте правильность введенных данных')
      main_calc()
    
    calc(op1, op2, act)
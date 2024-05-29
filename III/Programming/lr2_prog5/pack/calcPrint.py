from prettytable import PrettyTable

def print_inter():
    
    functions = {'Сложение':'+', 'Вычитание':'-', 'Умножение':'*', 'Деление':'/', 'Возведение в степень':'^x', 'Деление с остатком':'%'}
    tableheader = list(functions.keys())
    tablevalues = list(functions.values())
    colums = len(tableheader)
    
    table = PrettyTable(tableheader)
    tablevalue_data = tablevalues[:]
    
    while tablevalue_data:
        table.add_row(tablevalue_data[:colums])
        tablevalue_data = tablevalue_data[colums:]
    print(table)


def print_result(op1, op2, act, res):

    tableheader = ['Num1','Operation', 'Num2', 'Result']
    tablevalue = [op1, act, op2, res]
    colums = len(tableheader)

    table = PrettyTable(tableheader)
    tablevalue_data = tablevalue[:]

    while tablevalue_data:
        table.add_row(tablevalue_data[:colums])
        tablevalue_data = tablevalue_data[colums:]
    print(table)
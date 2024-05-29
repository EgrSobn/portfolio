import configparser

# настройки из текстового файла
PARAMS = {'precision': None}


# обработка точности в число
def convert_precision(kwargs):

    s = kwargs
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0


# вывод результата с заданной точностью
def f1(args, precision='0.0001'):

    global PARAMS
    precision = PARAMS['precision']

    res = args

    ndigits = convert_precision(precision)
    res = round(res, ndigits)

    return res


# Считывание из текстового файла в словарь
def load_params():

    config = configparser.ConfigParser()
    config.read('./dev.ini')

    PARAMS['precision'] = config.get('settings', 'precision')

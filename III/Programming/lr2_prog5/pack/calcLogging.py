import datetime

# запись истории в файл
def write_log(*args, action=None, result=None, file='calc-history.log.txt', state = False):

    error = None
  
    now = datetime.datetime.today()
  
    try:
      
        f = open(file, mode='a', errors='ignore')

        f.write(
            f'time : {now.strftime("%Y.%m.%d - %H:%M:%S")} operation {action}: {args} = {result} \n'
        )     
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        
        try:
             with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f'time : {now.strftime("%Y.%m.%d - %H:%M:%S")} operation {action}: {args} = {result} \n')
        except PermissionError as e:
          error = e
    else:
        f.close()

    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')
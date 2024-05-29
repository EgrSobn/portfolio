# import os
# import concurrent.futures

# def search_file(directory, file_name, results):
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file_name in file:
#                 results.append(os.path.join(root, file))
#                 return

# def main():
#     directory = input("Введите путь к директории: ")
#     file_name = input("Введите имя файла для поиска: ")

#     results = []

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.submit(search_file, directory, file_name, results)

#     if results:
#         print("Файл найден:", results[0])
#     else:
#         print("Файл не найден.")


# if __name__ == '__main__':
#     main()

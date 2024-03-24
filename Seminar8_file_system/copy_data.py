from return_data_file import data_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)

    input_file = f'db/data_{nf}.txt'
    if nf == 1:
        output_file = f'db/data_2.txt'
    else:
        output_file = f'db/data_1.txt'

    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))


    # копирование строчки из одного файла в другой

    with open(input_file, 'r') as input_f, open(output_file, 'a') as output_f:
        lines = input_f.readlines()
        if number_row > 0 and number_row <= len(lines):
            output_f.write(lines[number_row - 1])
            print("Строка успешно скопирована.")
        else:
            print("Некорректный номер строки.")


    # перезапись файла с новой построчной номирацией

    with open(output_file, "r", encoding="utf-8") as file:
        data = file.readlines()
    for i, line in enumerate(data):
        data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(data)


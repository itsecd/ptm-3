from csv import reader


def read_csv_data(file_name: str) -> list:
    '''Чтение csv-файла и запись данных в список'''
    list_data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        csv_data = reader(file, delimiter=";")
        for row in csv_data:
            list_data.append(row)
    list_data.pop(0)
    return list_data


if __name__ == "__main__":
    file_name = "49.csv"
    print(read_csv_data(file_name))
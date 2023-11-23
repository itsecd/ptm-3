import csv


def read_csv(path: str) -> list:
    data = []
    try: 
        with open(path, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except Exception as err:
        print(f"Error reading of file:{err}")
    return data

if __name__ == "__main__":
    data = read_csv("9.csv")
    print(data)
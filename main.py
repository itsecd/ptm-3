import csv
import checksum


if __name__ == '__main__':
    research_data = []
    names = []
    with open('8.csv', 'r', encoding="UTF16") as csvfile:
        read_data = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in read_data:
            if count != 0:
                research_data.append(row)
            else:
                names = row
            count += 1

    rows_not_valid_data, valid_data = checksum.match_data(research_data, names)
        
    valid_data_to_csv = []       
    for i in range(len(valid_data['date'])):
        row = []
        for n in names:
            row.append(valid_data[n][i])
        valid_data_to_csv.append(row)

    with open('valid_data.csv', 'w', encoding='UTF16') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(names)
        for i in range(len(valid_data['date'])):
            writer.writerow(valid_data_to_csv[i])
            
    summa = checksum.calculate_checksum(rows_not_valid_data)
    checksum.serialize_result(8, summa)

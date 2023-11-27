import csv
import checksum


if __name__ == '__main__':
    research_data, names = checksum.read_csv('8.csv')
    rows_not_valid_data, valid_data = checksum.match_data(research_data, names)
        
    valid_data_to_csv = []       
    for i in range(len(valid_data['date'])):
        row = []
        for n in names:
            row.append(valid_data[n][i])
        valid_data_to_csv.append(row)

    checksum.write_to_csv(valid_data_to_csv, names, 'valid_data.csv')
            
    summa = checksum.calculate_checksum(rows_not_valid_data)
    checksum.serialize_result(8, summa)

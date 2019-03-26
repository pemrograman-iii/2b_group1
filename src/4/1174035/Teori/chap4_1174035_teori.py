#CSV Reader
import csv
with open('cobain.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        print(', '.join(row))

#CSV Writer
import csv
with open('cobain.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Eh coba'] * 5 + [' Coba'])
    spamwriter.writerow(['Isi', 'Isi2', 'Isi3'])
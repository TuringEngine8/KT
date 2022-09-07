import csv

def write(inp,result):
    with open('info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([inp,result])
 
def read():
    res = []
    with open('info.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            res.append(row)
    return res # res is a list of lists

def main():
    i = input("read or write (r/w)?")
    if i == "r":
        info = read()
        anger = input("anger level:")

if __name__ == '__main__':
    main()
    
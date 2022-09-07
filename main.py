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
        chance = 0
        info = read()
        # print(info)
        anger = input("anger level: ")
        for i in info:
            # print(i)
            if i[0] == anger:
                if i[1] == "1":
                    chance += 1
                elif i[1] == "0":
                    chance -= 1
        print(chance)
    if i =="w":
        anger = input("what anger level(1-10)? ")
        result = input("what result(0 or 1)? ")
        write(anger,result)

if __name__ == '__main__':
    main()
    
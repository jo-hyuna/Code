import pandas

trans = input("입력: ")
li = trans.split(':')
pw = []

def main():
    data = pandas.read_csv('D:/Projects/ap.txt', names=['key', 'value'])
    keyList = list(data["key"])
    valueList = list(data["value"])

    List = dict(zip(keyList, valueList))

    for i in li:
        for k, v in List.items():
            if i==v:
                print(k)

if __name__ == '__main__':
    main()
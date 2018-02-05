from csc131 import dictionaries


def main():
    print("Main")
    d = dictionaries.get_personal_data()
    print(d)
    for key in sorted(d.keys()):
        print("%s: %s" %(key, d[key]))
# prints the key then the value of that key^ in alphabetical order


if __name__ == '__main__':
    main()

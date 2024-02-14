import csv

with open("parametry.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    print("lista parametrów:")
    for i, line in enumerate(reader):
        print("\n")
        if i > 0:
            line = list(filter(None, line))
            for j in range(line.__len__()):
                print("p["+str(j)+"]="+str(line[j]))
            print("\n")



from sys import argv
assert isinstance(argv, object)

script, filename = argv

txt = open(filename)

cases = int(txt.readline())

def missingRow(textFile):
    answer = []
    grid = []
    rowstoread = int(txt.readline())*2

    for i in range(1, rowstoread):
        line = txt.readline().split()
        grid += list([x for x in line if x.isdigit()])

    for n in grid:
        if n not in answer:
            if grid.count(n) % 2 != 0:
                answer.append(n)

    answer.sort(key=int)

    return str(answer).strip('[]').replace("'", "").replace(",", "")

for i in range(1, int(cases)+1):
    print("Case #" + str(i) + ": " + missingRow(txt))



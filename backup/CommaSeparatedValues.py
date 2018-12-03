
import csv
reader = csv.DictReader(open('agent.log.csv'))

result = {}
for row in reader:
    key = row.pop('agent')
    if key not in result:
        result[key] = row
    else:
        result.update({key: row})


'''
d = dict.fromkeys(['agent', 'runtime'])
columns = ["date", "time", "agent", "empty", "runtime"]
with open('agent.log.csv', "r", newline="") as file:
    reader = csv.DictReader(file, fieldnames=columns, delimiter=delim)
    for row in reader:
        if not d[row["agent"]]:
            d[row["agent"]] = int(row["runtime"])
        elif d[row["agent"]]
'''
import json

with open('/Users/yiyingy/Downloads/CoreFrontend_develop-daily-triage-ie-windows2016_1-150-failed.json') as f:
    contents1 = f.readlines()

with open('/Users/yiyingy/Downloads/CoreFrontend_develop-daily-triage-ie-windows2016_150-301-failed.json') as f:
    contents2 = f.readlines()

contents = []
for i in contents1:
    contents.append(json.loads(i))
for i in contents2:
    contents.append(json.loads(i))


with open('/Users/yiyingy/Downloads/CoreFrontend_develop-daily-triage-ie-windows2016_1-301-failed.json', 'w') as f:
    for i in contents:
        f.write(json.dumps(i)+'\n')

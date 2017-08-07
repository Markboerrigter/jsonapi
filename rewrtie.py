import json
json_data=open('db.json').read()

data = json.loads(json_data)

newdata = {}

for x in data:
    print(x)
    if not x["Keuze 1"] in newdata:
        newdata[x["Keuze 1"]] = {}
    if not x["keuze 2"] in newdata[x["Keuze 1"]]:
        newdata[x["Keuze 1"]][x["keuze 2"]] = {}
    if not x["keuze 3"] in newdata[x["Keuze 1"]][x["keuze 2"]]:
        newdata[x["Keuze 1"]][x["keuze 2"]][x["keuze 3"]] = {}
    if not x["keuze 4"] in newdata[x["Keuze 1"]][x["keuze 2"]][x["keuze 3"]]:
        newdata[x["Keuze 1"]][x["keuze 2"]][x["keuze 3"]][x["keuze 4"]] = {}
    newdata[x["Keuze 1"]][x["keuze 2"]][x["keuze 3"]][x["keuze 4"]] = [[x["naam1"],x['prijs1'],x['foto1']],[x["naam2"],x['prijs2'],x['foto2']]]

with open('data.json', 'w') as fp:
    json.dump(newdata, fp)

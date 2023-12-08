import csv
import json
import os


class Decoder:
    def __init__(self):
        self.b = {}

    def chtenie_faila(self, adr):
        with open(adr, 'r') as f:
            r = []
            reader = csv.reader(f)
            for line in reader:
                r.append(line)
        r.pop(0)
        return r

    def sorterovka_poziciy(self, s):
        stolb = (109, 209, 119, 219, 137,
                 138, 237, 238, 155, 255,
                 165, 265, 174, 274)
        v = []
        b = {}
        for i in s:
            if i[0] not in v:
                v.append(i[0])
        for i in v:
            b[i] = []
            for j in s:
                if str(i) == str(j[0]):
                    if ((str(j[1]) not in b[i])
                            and (107 < j[1] < 175 or 207 < j[1] < 275)
                            and (j[1] not in stolb)):
                        b[i].append(str(j[1]))
            b[i] = " ,".join(b[i])
            self.b = b
        return self.b

    def csv_convert_to_json(self, adr, key1, key2):
        s = []
        for i in self.chtenie_faila(adr):
            t = i[0].split(";")
            s.append((t[key1-1], int(t[key2-1])))

        with open("text_json.json", "w") as f:
            try:
                f.write(json.dumps(self.sorterovka_poziciy(s), indent=3))
                print(os.path.abspath("text_json.json"))
            except FileNotFoundError:
                print("1111")

        with open("consolidatciya.html", "w") as f:
            f.writelines("<div class="'rect'""+">")

        with open("consolidatciya.html", "a") as f:
            for key in self.b.keys():
                f.writelines("<div class="'line'""+"><div><button>"+key+"</button>:      "+self.b[key]+"</div></div>")
        with open("consolidatciya.html", "a") as f:
                f.writelines('<script src="sckript.js"></script>')
        with open("consolidatciya.html", "a") as f:
            f.writelines("</div>")



































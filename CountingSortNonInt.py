import random


class Count(object):
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return "Id: "+str(self.id)+" Data: "+str(self.data)


arrId = []
arrData = []
objArr = []
for i in range(20):
    r = random.randint(0, 9)
    r1 = random.randint(0, 9)
    arrId.append(r)
    arrData.append(r1)
    c = Count(r, r1)
    objArr.append(c)

# for i in range(20):
#     print(arrId[i], arrData[i], objArr[i])

m = max(arrId)
print(m, end="\n\n")
k = [[] for i in range(m+1)]
for i in range(20):
    k[objArr[i].id].append(objArr[i])

output = []
for i in range(m+1):
    output.extend(k[i])

for i in output:
    print(i)

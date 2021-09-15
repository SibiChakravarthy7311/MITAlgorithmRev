import math

file1 = open('doc1.txt', 'r')
file2 = open('doc2.txt', 'r')

s1 = file1.read()
s2 = file2.read()

file1.close()
file2.close()

s1 = s1.split()
s2 = s2.split()

dict1 = {}
dict2 = {}

set1 = set(s1)
set2 = set(s2)

for i in set1:
    dict1[i] = 0
for i in set2:
    dict2[i] = 0

for i in s1:
    dict1[i] += 1
for i in s2:
    dict2[i] += 1

# print("Dict1:", dict1)
# print("Dict2:", dict2)
val1 = list(dict1.values())
val2 = list(dict2.values())

dict1mag = math.sqrt(sum(math.pow(val, 2) for val in val1))
dict2mag = math.sqrt(sum(math.pow(val, 2) for val in val1))

# print("Dict1mag:", dict1mag)
# print("Dict2mag:", dict2mag)

# count = 0
# dict1c = {}
# dict2c = {}
# for key in dict1:
#     if(dict2.get(key)):
#         count += 1
#         dict1c[key] = dict1[key]
#         dict2c[key] = dict2[key]
# print("count:", count)
# print("Dict1C:", dict1c)
# print("Dict2C:", dict2c)

dotProduct = sum(dict1[key]*dict2.get(key, 0) for key in dict1)
similarity = dotProduct/(dict1mag*dict2mag)

print("Similarity:", (similarity*100), "%")


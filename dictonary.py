myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
a = []
b = []
for c, d in myData.items():
  print("key:", c, "value:", d)
  a.append(c)
  b.append(d)
print("all keys: ", a)
print("all values ", b) 
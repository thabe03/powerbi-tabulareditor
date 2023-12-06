# Python program to read
# json file

import json

# Opening JSON file
f = open('powerbi.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
notWord = ["sum", "average","totalytd", "filter", "divide", "if", "sameperiod", "counta"]
for i in data["measures"]:
  isOk = False
  for j in notWord:
    if j in i["expression"].lower(): 
      isOk = True   
  if isOk == False:
    tmp = i["name"] + "=" + i["expression"]
    print(tmp)

# Closing file
f.close()
import requests
import base64
#Read the content in webside.txt, split it by line, and generate a list
with open('webside.txt','r') as f:
     webside = f.read().splitlines()
# Use request to get each URL in the list, decode the result with base64 and add it to the list txt
txt = []
for i in webside:
     r = requests.get(i)
     txt.append(base64.b64decode(r.text).decode('utf-8'))
# Deduplicate the txt list
txt = list(set(txt))
# Write the txt list to the file
with open('output.txt','w') as f:
     for i in txt:
         f.write(i+'\n')

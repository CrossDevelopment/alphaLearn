import json

def template(body):
    for e in body:
      print(json.dumps(e,separators=('[]')))
      

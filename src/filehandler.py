import simplejson

def fileWrite(name,data):
    f= open(name)
    simplejson.dump(data,f)
    f.close()
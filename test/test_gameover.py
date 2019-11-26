def test_gameover(h,v,half,inning):
    result = {
        "done": False,
        "h": h,
        "v": v,
        "half": half,
        "inning": inning,
        "check": False
    }
    if inning < 9:
        result["check"] = True
    elif half == "T":
        result["check"] = True
    elif h == v:
        result["check"] = True
    elif h != v and half == "Full":
        result["check"] = True
        result["done"] = True
    return(result)

x = test_gameover(3,1,"T",5)
y = test_gameover(3,1,"T",9)
z = test_gameover(3,1,"B",9)
a = test_gameover(3,4,"B",11)
b = test_gameover(3,4,"Full",11)
c = test_gameover(3,4,"T",11)
d = test_gameover(4,4,"B",11)
print (f'--- {x["h"] if True else "Yikes"}')
#print ( a, b, c, d, x, y, z )
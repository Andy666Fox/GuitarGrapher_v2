import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
skk.speed(300)
 
def sqrfunc(size):
    for i in range(20):
        skk.fd(size)
        skk.left(45 * 3.14)
        size = size + 5
 
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
    
    
    
    
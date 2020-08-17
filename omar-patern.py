import turtle 

t =turtle.Turtle() 

t.speed(10000)
count = 1 
u = 100 

while count < 100: 
    t.pencolor("green")
    t.left(30 + count/ 100)
    t.forward(u) 
    t.pencolor("blue")
    t.left(45+ count/100) 
    t.forward(u) 
    t.pencolor('red')
    t.left(120 + count/100)
    t.forward(u)
    count = count +1  
    u = u + 0.5 



input("hit enter to exit")
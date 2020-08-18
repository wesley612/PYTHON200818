import turtle

a = int(input("輸入的數字")) 
for i in range(a) :
    turtle.forward(100)
    turtle.right(360/a)
    
turtle.done()
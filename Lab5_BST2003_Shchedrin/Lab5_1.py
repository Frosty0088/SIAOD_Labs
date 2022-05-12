import time, turtle

cnt = 0

window=turtle.Screen()

alex=turtle.Turtle()
alex.speed(0)

def sierpinski(a,t,size):
    global cnt

    if a==0:
        for i in range(3):
            t.forward(size)
            t.left(120)

    else:
       sierpinski(a-1,t,size/2)
       t.forward(size/2)
       sierpinski(a-1,t,size/2)
       t.forward(size/2)
       t.left(120)
       t.forward(size/2)
       sierpinski(a-1,t,size/2)
       t.forward(size/2)
       t.left(120)
       t.forward(size)
       t.left(120)

    if a==0:
        cnt+=1


rec = int(input("Введите глубину: "))
prev_t = time.time()

sierpinski(rec,alex,300)
cur_t = time.time() - prev_t
print("Глубина рекурсии:", rec,  "\nВремя выполнения:",cur_t)

window.mainloop()
import turtle

t = turtle.Turtle()

for i in range(2):
  t.forward(75)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(75)
  i = i + 1


t.left(35)
t.forward(90)
t.left(112)
t.forward(90)
t.left(70)
t.forward(90)
t.left(110)
t.forward(90)

t.left(123)
t.forward(70)

i = 0
t.left(90)
for i in range(100):
  t.forward(2)
  t.left(5)
  i = i + 1

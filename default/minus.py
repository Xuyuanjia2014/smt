from z3 import *

x1 = 6
y1 = 10
res1 = 4

x2 = 8
y2 = 9
res2 = 1

m = Int('m')
n = Int('n')
i = Int("i")
j = Int("j")

locations = Array("locations", IntSort(), IntSort())
operators = Array("operators", IntSort(), IntSort())
operators2 = Array("operators2", IntSort(), IntSort())
s = Solver()
s.add(locations[0] == 1)
s.add(locations[1] == 25)
s.add(locations[2] == 87)

s.add(operators[0] == x1)
s.add(operators[1] == y1)
s.add(operators[2] == 0)

s.add(operators2[0] == x2)
s.add(operators2[1] == y2)
s.add(operators2[2] == 0)

index = 1
for a in [3,6,9]:
    if a == 3:
        s.add(Or(And(operators[a] == x1, locations[a] == locations[0]),
                 And(operators[a] == y1, locations[a] == locations[1]),
                 And(operators[a] == 0, locations[a] == locations[2])))
        s.add(Or(And(operators2[a] == x2, locations[a] == locations[0]),
                 And(operators2[a] == y2, locations[a] == locations[1]),
                 And(operators2[a] == 0, locations[a] == locations[2])))
    else:
        s.add(Or(And(operators[a] == x1, locations[a] == locations[0]),
            And(operators[a] == y1, locations[a] == locations[1]),
            And(operators[a] == 0, locations[a] == locations[2]),
            And(operators[a] == operators[a - 1], locations[a] == locations[a - 1])))

        s.add(Or(And(operators2[a] == x2, locations[a] == locations[0]),
                 And(operators2[a] == y2, locations[a] == locations[1]),
                 And(operators2[a] == 0, locations[a] == locations[2]),
                 And(operators2[a] == operators2[a - 1], locations[a] == locations[a - 1])))

    s.add(Or(And(operators[a+1] == x1, locations[a+1] == locations[0]),
        And(operators[a+1] == y1, locations[a+1] == locations[1]),
        And(operators[a+1] == 0, locations[a+1] == locations[2])))

    s.add(Or(And(operators2[a+1] == x2, locations[a+1] == locations[0]),
        And(operators2[a+1] == y2, locations[a+1] == locations[1]),
        And(operators2[a+1] == 0, locations[a+1] == locations[2])))

    if a == 9:
        s.add(And(operators[a + 2] == operators[a] - operators[a + 1],
                  locations[a + 2] == locations[a] + locations[a + 1]))

        s.add(And(operators2[a + 2] == operators2[a] - operators2[a + 1],
                  locations[a + 2] == locations[a] + locations[a + 1]))
    else:
        s.add(And(operators[a+2] == operators[a+1]+operators[a], locations[a+2] == locations[a+1] + locations[a]))
        s.add(And(operators2[a + 2] == operators2[a + 1] + operators2[a],
                  locations[a + 2] == locations[a + 1] + locations[a]))

s.add(operators[11] == res1)
s.add(operators2[11] == res2)
print(s.check())
model = s.model()
print(model)

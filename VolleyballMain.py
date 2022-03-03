import numpy as np

class Player:
    def __init__(self, name, rec, block, setting, hit, serve, mobil, loc):
        self.name = name
        self.rec = rec
        self.block = block
        self.setting = setting
        self.hit = hit
        self.serve = serve
        self.mobil = mobil
        self.loc = loc


ni = Player('Nick', 7, 5, 4, 7, 8, 5, -1)
bl = Player('Brandon L', 8, 8, 10, 8, 7, 9, -1)
ez = Player('Enzo', 5, 1, 3, 3, 6, 3, -1)
# mu = Player('Mucci', 8, 10, 8, 9, 8, 9, 180)
mu = Player('Mucci', 1, 1, 1, 1, 1, 1, 180)
st = Player('Stephen', 7, 8, 7, 8, 8, 6, 270)
sp = Player('Spencer', 7, 7, 8, 9, 8, 3, 0)
da = Player('Dawson', 1, 9, 2, 7, 5, 2, 90)

players = [ni, bl, ez, mu, st, sp, da]
field = [sp, da, mu, st]
bench = [ni, bl, ez]

# Receive, Block, Set, Hit, Serve, Mobility
weight0 = [1, 2, 4, 1, 1, 3]
weight90 = [4, 2, 1, 3, 1, 1]
weight180 = [3, 0, 1, 2, 4, 2]
weight270 = [4, 2, 1, 3, 1, 1]
benchWeight = [1, 1, 1, 1, 1, 1]


rotations = 7


def rotate(x):
    for y in x:
        y.loc += 90
        if y.loc > 270:
            y.loc = 0


def sumWeights(z, w):
    return z.rec * w[0] + z.block * w[1] + z.setting * w[2] + z.hit * w[3] + z.serve * w[4] + z.mobil * w[5]


def calcPositionSkill(playermat, weightmat):
    positionSkill = np.array([], dtype=int)
    for i in playermat:
        skill = sumWeights(i, weightmat)
        positionSkill = np.append(positionSkill, skill)
        # print(positionSkill)
    return positionSkill


pos0skill = calcPositionSkill(players, weight0)
pos90skill = calcPositionSkill(players, weight90)
pos180skill = calcPositionSkill(players, weight180)
pos270skill = calcPositionSkill(players, weight270)

while rotations:
    rotate(field)
    for i in field:
        if i.loc == 270:
            subspot = i.name
            subspotSkill = sumWeights(i, weight270)
    for j in bench:
        benchCompare = 0
        benchsub = sumWeights(j, weight270)
        benchsubname = ""
        if benchsub > benchCompare:
            benchsub = benchCompare
            benchsubname = j.name
    print("Best Bench Sub: ", benchsubname, "\n")
    if subspotSkill <= benchsub:
        print("Changed to: ", benchsubname, "\n")
        break
    else:
        print("No Change", subspot, "\n")

    rotations -= 1



class Player:
    def __init__(self, name, skill0, skill90, skill180, skill270, rec, block, setting, hit, serve, mobil, loc):
        self.name = name
        self.skill0 = skill0
        self.skill90 = skill90
        self.skill180 = skill180
        self.skill270 = skill270
        self.rec = rec
        self.block = block
        self.setting = setting
        self.hit = hit
        self.serve = serve
        self.mobil = mobil
        self.loc = loc


nick = Player("Nick", 0, 0, 0, 0, 7, 5, 4, 7, 8, 5, -1)
brandon = Player("Brandon", 0, 0, 0, 0, 8, 8, 10, 8, 7, 9, -1)
enzo = Player("Enzo", 0, 0, 0, 0, 5, 1, 3, 3, 6, 3, -1)
# mucci = Player("Mucci", 0, 0, 0, 0, 8, 10, 8, 9, 8, 9, 180)
mucci = Player("Mucci", 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 180)
stephen = Player("Stephen", 0, 0, 0, 0, 7, 8, 7, 8, 8, 6, 270)
spencer = Player("Spencer", 0, 0, 0, 0, 7, 7, 8, 9, 8, 3, 0)
dawson = Player("Dawson", 0, 0, 0, 0, 1, 9, 2, 7, 5, 2, 90)

players = [nick, brandon, enzo, mucci, stephen, spencer, dawson]
field = [spencer, dawson, mucci, stephen]
bench = [nick, brandon, enzo]

# Receive, Block, Set, Hit, Serve, Mobility
weight0 = [1, 2, 4, 1, 1, 3]
weight90 = [4, 2, 1, 3, 1, 1]
weight180 = [3, 0, 1, 2, 4, 2]
weight270 = [4, 2, 1, 3, 1, 1]
benchWeight = [1, 1, 1, 1, 1, 1]

rotations = 7


def sumWeights(z, w):
    return z.rec * w[0] + z.block * w[1] + z.setting * w[2] + z.hit * w[3] + z.serve * w[4] + z.mobil * w[5]


for i in players:
    i.skill0 = sumWeights(i, weight0)
    i.skill90 = sumWeights(i, weight90)
    i.skill180 = sumWeights(i, weight180)
    i.skill270 = sumWeights(i, weight270)
    # print(i.skill0)


def rotate(x):
    for y in x:
        y.loc += 90
        if y.loc > 270:
            y.loc = 0


def substitute(substitute_player, substitute_bench_player, bench_array, field_array):
    substitute_bench_player.loc = 270
    substitute_player.loc = -1
    bench_array_position = bench_array.index(substitute_bench_player)
    sub_array_position = field_array.index(substitute_player)
    container = field_array[sub_array_position]
    field_array[sub_array_position] = bench_array[bench_array_position]
    bench_array[bench_array_position] = container



while rotations:
    rotate(field)
    subspot_skill = 0
    sub_name = ""
    sub_player = dawson
    for j in field:
        if j.loc == 270:
            subspot_skill = j.skill270
            sub_name = j.name
            sub_player = j
    print("\nIdentified ", sub_name, " at sub position \nHis skill at sub position is: ", subspot_skill)

    best_bench_skill = 0
    best_bench_name = ""
    best_bench_player = enzo
    for k in bench:
        if k.skill270 > best_bench_skill:
            best_bench_skill = k.skill270
            best_bench_name = k.name
            best_bench_player = k
    print("Identified ", best_bench_name, " as best bench player \nHis skill at sub position is: ", best_bench_skill)
    if subspot_skill <= best_bench_skill:
        substitute(sub_player, best_bench_player, bench, field)
        print("Substituted ", best_bench_name, " for", sub_name, "\n")
        # break
    else:
        print("No Change", "\n")

    print("The field players are: ")
    for a in field:
        print(a.name)

    print("The bench players are: ")
    for b in bench:
        print(b.name)

    rotations -= 1


import random
import math
import matplotlib.pyplot as plt

def make_rand_theta():
    return random.randrange(360)

def make_rand_index():
    return random.randrange(5), random.randrange(5)

def init_vector(l):
    px = []
    py = []
    vx = []
    vy = []

    for y in range(5):
        for x in range(5):
            px.append(x)
            py.append(y)
            vx.append(round(math.cos(math.radians(l[4-y][x]))*0.5, 4))
            vy.append(round(math.sin(math.radians(l[4-y][x]))*0.5, 4))

    return px, py, vx, vy

def cal_vector(theta, s, vx, vy):
        vx[20-s[0]*5+s[1]] = round(math.cos(math.radians(theta))*0.5, 4)
        vy[20-s[0]*5+s[1]] = round(math.sin(math.radians(theta))*0.5, 4)


def init_array():
    l = [[0 for j in range(5)] for i in range(5)]

    for i in range(5):
        for j in range(5):
            l[i][j] = make_rand_theta()

    return l

def inner_product(a, b):
    if a >= b:
        return round(math.cos(math.radians(a-b)), 4)
    else:
        return round(math.cos(math.radians(b-a)), 4)

def monte_carlo_method(l, vx, vy):
    s = make_rand_index()
    theta = l[s[0]][s[1]]
    new_theta = make_rand_theta()
    sum_before = 0
    sum_after = 0
    if s[0] != 0:
        sum_before += inner_product(theta, l[s[0]-1][s[1]])
        sum_after += inner_product(new_theta, l[s[0]-1][s[1]])
    if s[0] != 4:
        sum_before += inner_product(theta, l[s[0]+1][s[1]])
        sum_after += inner_product(new_theta, l[s[0]+1][s[1]])
    if s[1] != 0:
        sum_before += inner_product(theta, l[s[0]][s[1]-1])
        sum_after += inner_product(new_theta, l[s[0]][s[1]-1])
    if s[1] != 4:
        sum_before += inner_product(theta, l[s[0]][s[1]+1])
        sum_after += inner_product(new_theta, l[s[0]][s[1]+1])
    if sum_before <= sum_after:
        l[s[0]][s[1]] = new_theta
        cal_vector(new_theta, s, vx, vy)


def main():
    l = init_array()
    px, py, vx, vy = init_vector(l)

    for j in range(9):
        plt.subplot(3, 3, j+1)
        plt.quiver(px, py, vx, vy, angles='xy', scale_units="xy", scale=1)
        plt.xlim(-1, 5)
        plt.ylim(-1, 5)
        plt.title(f'N = {1000+1000*(1/2*j+1)*(j-1)}')
        for i in range(1000*(j+1)):
            monte_carlo_method(l, vx, vy)

    print(l)

    plt.tight_layout()
    plt.savefig("exchange_interaction.png")
    plt.show()

if __name__ == "__main__":
    main()
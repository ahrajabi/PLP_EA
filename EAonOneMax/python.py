import time
import random
import copy

def OneMaxFitness(point):
    cnt = 0
    for bit in point:
        if bit == 1:
            cnt += 1
    return cnt

print(OneMaxFitness([0,1,1,0,1]))

def Mutation(point, prob):
    n = len(point)
    new_point = copy.copy(point)
    for item in range(n):
        if random.random() < prob:
            new_point[item] = 1-new_point[item]
    return new_point

print(Mutation([0,1,0,1], 1))


def ea(n, iter_number):
    point = [random.choice([0,1]) for i in range(n)]
    point_value = OneMaxFitness(point)

    for iter in range(iter_number) :
        new_point = Mutation(point, 1.0/n)
        new_point_value = OneMaxFitness(new_point)

        if new_point_value >= point_value:
            # print "A better point with the fitness is found.",str(new_point_value)
            point = new_point
            point_value = new_point_value
            if point_value == n:
                # println("The best point is found.")
                return True

def benchmark(tries):
    max_iter = 10000
    for n in [100, 1000, 10000]:
        time_sum = 0
        for t in range(tries):
            t1 = time.time()*1000
            ea(n, max_iter)
            t2 = time.time()*1000
            time_sum += (t2-t1)
        took = time_sum*0.1/tries
        print "Python solves OneMax of size %d in %d ms."%(n, took)

benchmark(10)

using Random

function OneMaxFitness(point)
    cnt = 0
    for bit in point
        if bit == true
            cnt += 1
        end
    end
    cnt
end

function Mutation(point, prob)
    n = length(point)
    new_point = copy(point)
    for item in 1:n
        if rand() < prob
            new_point[item] = 1-new_point[item]
        end
    end
    new_point
end


function ea(n, iter_number)
    point = bitrand(n)
    point_value = OneMaxFitness(point)

    for iter in 1:iter_number
        new_point = Mutation(point, 1/n)
        new_point_value = OneMaxFitness(new_point)

        if new_point_value >= point_value
            # println("A better point with the fitness $new_point_value is found.")
            point = new_point
            point_value = new_point_value
            if point_value == n
                # println("The best point is found.")
                return true
            end
        end
    end
end

function benchmark(tries)
    max_iter = 10000000000
    for n in [100, 1000, 10000]
        time_sum = 0
        for t in tries
            t1 = time_ns()
            ea(n, max_iter)
            t2 = time_ns()
            time_sum += (t2-t1)
        end
        took = time_sum/tries
        println("Julia solves OneMax of size $n in $took ns." )
    end
end

benchmark(100)

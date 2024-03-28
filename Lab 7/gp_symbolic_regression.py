import operator
import math
import random
import numpy as np
from deap import algorithms, base, creator, tools, gp


def protected_division(numerator, denominator):
    if denominator == 0:
        return 1
    return numerator / denominator


def eval_fitness_symb_regression(indiviual, points):
    func = toolbox.compile(expr=indiviual)
    mean_square_error = [
        (func(x) - (x**4 + x**3 + x**2 + x)) ** 2 for x in points
    ]
    return (math.fsum(mean_square_error) / len(points),)


def create_toolbox():
    pset = gp.PrimitiveSet("MAIN", 1)
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protected_division, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))
    pset.renameArguments(ARG0="x")

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

    global toolbox
    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    toolbox.register(
        "evaluate",
        eval_fitness_symb_regression,
        points=[x / 10.0 for x in range(-10, 10)],
    )
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    toolbox.decorate(
        "mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17)
    )
    toolbox.decorate(
        "mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17)
    )

    return toolbox


def get_statistics():
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)
    return mstats


def main():
    random.seed(7)
    toolbox = create_toolbox()
    population = toolbox.population(n=450)
    hall_of_fame = tools.HallOfFame(1)

    probab_crossover = 0.4
    probab_mutate = 0.2
    number_gen = 10

    algorithms.eaSimple(
        population,
        toolbox,
        probab_crossover,
        probab_mutate,
        number_gen,
        stats=get_statistics(),
        halloffame=hall_of_fame,
        verbose=True,
    )
    print("=" * 50)
    print("Best individual:", hall_of_fame[0])


if __name__ == "__main__":
    main()

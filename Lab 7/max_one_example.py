import random
from deap import base, creator, tools


def Evalfunc(i):
    targetSum = 15
    return (len(i) - abs(sum(i) - targetSum),)


def create_toolbox(nbits):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register(
        "individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, nbits
    )
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", Evalfunc)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    return toolbox


if __name__ == "__main__":
    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing, probab_mutating = 0.5, 0.2
    num_generations = 10

    print("Evolution process starts")
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit
    print("Evaluated", len(population), "individuals")

    for g in range(num_generations):
        print("=" * 50)
        print("- Generation", g)
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < probab_crossing:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < probab_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_individuals = [i for i in offspring if not i.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_individuals)

        for i, fit in zip(invalid_individuals, fitnesses):
            i.fitness.values = fit
        print("Evaluated", len(invalid_individuals), "individuals")

        population[:] = offspring

        fits = [i.fitness.values[0] for i in population]
        length = len(population)
        mean = sum(fits) / length
        sum_2 = sum(x * x for x in fits)
        std = abs(sum_2 / length - mean**2) ** 0.5
        print("Min =", min(fits), ", Max =", max(fits))
        print("Average =", round(mean, 2), ", Standard deviation =", round(std, 2))
    print("- Evolution ends")
    bestInd = tools.selBest(population, 1)[0]
    print("\nBest individual:\n", bestInd)
    print("Number of ones:", sum(bestInd))

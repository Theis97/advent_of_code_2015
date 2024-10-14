import common.graph
from typing import Callable


def get_total_distance(g: common.graph,
                       current_city: str,
                       unvisited_cities: list,
                       total_distance: int,
                       optimization_func: Callable):
    if len(unvisited_cities) == 1:
        return total_distance + g.graph[current_city][unvisited_cities[0]]
    else:
        lengths: list[int] = []
        for city in unvisited_cities:
            new_unvisited_cities = unvisited_cities.copy()
            new_unvisited_cities.remove(city)
            lengths.append(
                get_total_distance(
                    g,
                    city,
                    new_unvisited_cities,
                    total_distance + g.graph[current_city][city],
                    optimization_func))
        return optimization_func(lengths)


if __name__ == '__main__':
    file = open("input.txt")

    distances = common.graph.Graph()
    cities: set = set()

    # Build a graph of cities and the distances between each of them
    for line in file:
        words = line.split()

        if words[0] in cities:
            distances.add_edge(words[0], words[2], int(words[4]))
        else:
            distances.add_vertex(words[0])
            distances.add_edge(words[0], words[2], int(words[4]))

        if words[2] in cities:
            distances.add_edge(words[2], words[0], int(words[4]))
        else:
            distances.add_vertex(words[2])
            distances.add_edge(words[2], words[0], int(words[4]))

        cities.add(words[0])
        cities.add(words[2])

    short_distances = []
    long_distances = []
    for key, value in distances.graph.items():
        unvisited_cities = cities.copy()
        unvisited_cities.remove(key)
        short_distances.append(get_total_distance(distances, key, list(unvisited_cities), 0, min))
        long_distances.append(get_total_distance(distances, key, list(unvisited_cities), 0, max))

    print(f'Shortest route length: {min(short_distances)}')
    print(f'Longest route length: {max(long_distances)}')



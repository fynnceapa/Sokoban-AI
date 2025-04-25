from sokoban.map import Map
from search_methods.beam_search import BeamSearch
import math


def manhattan_heuristic(map: Map) -> int:
    """
    Heuristic function for Sokoban.
    Calculates the Manhattan distance between boxes and their closest targets.
    """
    total_distance = 0
    for box in map.boxes.values():
        for target in map.targets:
            distance = abs(box.x - target[0]) + abs(box.y - target[1])
            total_distance += distance
    return total_distance

def euclidian_heuristic(map: Map) -> int:
    total_distance = 0
    for box in map.boxes.values():
        for target in map.targets:
            distance = math.sqrt((box.x - target[0])**2 + (box.y - target[1])**2)
            total_distance += distance
    return total_distance


class Solver:

    def __init__(self, map: Map) -> None:
        self.map = map

    def solve(self):
        return BeamSearch(self.map, 5, 10000, euclidian_heuristic).search()

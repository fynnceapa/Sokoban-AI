import heapq
from sokoban.map import Map
from sokoban.moves import *

from typing import List, Callable, Set, Tuple
import random

class BeamSearch:
    def __init__(self, map: Map, width: int, max_iter: int = 10000, heuristic: Callable[[Map], int] = None):
        self.map = map
        self.width = width
        self.max_iter = max_iter
        self.heuristic = heuristic if heuristic else lambda x: 0
        self.visited = set()
    
    def search(self) -> Tuple[List[Map], int, int]:
        beam = [(self.map, [self.map])]
        total_pushes = 0
        total_pulls = 0
        iteration_count = 0
        while beam:
            next_beam = []
            for node, path in beam:
                if node.is_solved():
                    return path, total_pushes, total_pulls
                for successor in node.get_neighbours():
                    state_str = str(successor)
                    if state_str not in self.visited:
                        self.visited.add(state_str)
                        next_beam.append((successor, path + [successor]))
                        total_pushes += successor.push_count
                        total_pulls += successor.undo_moves
            if next_beam:
                next_beam.sort(key=lambda x: self.heuristic(x[0]))
                next_beam = next_beam[:self.width]
                beam = next_beam
            else:
                beam = []
            iteration_count += 1
            if iteration_count >= self.max_iter:
                break
        return [], total_pushes, total_pulls
       
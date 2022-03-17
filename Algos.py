from collections import deque
from heapq import heappop, heappush
from math import inf


class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.huristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost=1, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, cost, True)

    def set_huristics(self, huristics={}):
        self.huristics = huristics

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def cost(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except:
            return inf

    def depth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.append(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print();
            return came_from
        else:
            print('No path from {} to {}'.format(start, goal))

    def breadth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.appendleft(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print();
            return came_from
        else:
            print('No path from {} to {}'.format(start, goal))

    def uniform_cost_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str((0, start))))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost, node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print();
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf

    def greedy_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {
            start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (self.huristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print();
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf

    def a_star_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {
            start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + self.huristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print();
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else:
            print(goal, end='');
            return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)


graph = Graph(directed=True)
#   For unweighted graphs:
#   Adding edges:
#       Use the function add_edge: graph.add_edge(Node1, Node2)
#   Defining start and goal:
#       start, goal = source, target
#   Tracing the path:
#       traced_path = graph."Algorithm function call"(start, goal)
#   Printing the path:
#       if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal);print()

#   For weighted uninformed graphs:
#   Adding edges:
#       Use the function add_edge: graph.add_edge(Node1, Node2, weight)
#   Defining start and goal:
#       start, goal = source, target
#   Tracing the path:
#       traced_path, cost = graph."Algorithm function call"(start, goal)
#   Printing the path:
#       if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal); print('\nCost:', cost)

#   For informed graphs:
#   Adding edges:
#       Use the function add_edge: graph.add_edge('Node1', 'Node2', weight)
#   Adding heuristics:
#       use the function set_huristics: graph.set_huristics({'Node1' : heuristic, 'Node2' : heuristic, etc}
#   Defining start and goal:
#       start, goal = source, target
#   Tracing the path:
#       traced_path, cost = graph."Algorithm function call"(start, goal)
#   Printing the path:
#       if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal); print('\nCost:', cost)

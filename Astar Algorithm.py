#QUESTION 3: 2019A7PS1207H 2019A7PS0003H

from collections import deque
 
class Graph:
    def __init__(self, list_adjac):
        self.list_adjac = list_adjac
 
    def neighbours(self, v):
        return self.list_adjac[v]
 
    # heuristic h() given in question
    def h(self, n):
        H = {
            'Perseverance': 550,
            'ChkPt-1': 550,
            'ChkPt-2': 450,
            'ChkPt-3': 510,
            'ChkPt-4': 325,
            'ChkPt-5': 415,
            'ChkPt-6': 235,
            'ChkPt-7': 455,
            'ChkPt-8': 400,
            'ChkPt-9': 325,
            'ChkPt-10': 240,
            'ChkPt-11': 170,
            'ChkPt-12': 205,
            'Jezero': 0
        }
 
        return H[n]
 
    def algorithm(self, start, stop):
        list_open = set([start]) #open_list beings with start, 
        list_closed = set([]) #all nodes which have been visited 
        dist = {} #distance from start to other nodes
        dist[start] = 0
        adjac_map = {} #adjac mapping of nodes
        adjac_map[start] = start
 
        while len(list_open) > 0:
            n = None
            for v in list_open:
                if n == None or dist[v] + self.h(v) < dist[n] + self.h(n): #node with least f() = g() + h()
                    n = v
            if n == None: #cannot find
                print('Path does not exist!')
                return None
            if n == stop: #start again from starting
                reconst_path = []
                while adjac_map[n] != n:
                    reconst_path.append(n)
                    n = adjac_map[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            for (m, weight) in self.neighbours(n):
                if m not in list_open and m not in list_closed: #node not in open-list and closed-list 
                    list_open.add(m) #add to open-list
                    adjac_map[m] = n #find its adjac-mapping
                    dist[m] = dist[n] + weight
 
                else:
                    if dist[m] > dist[n] + weight: #is it quicker to visit n
                        dist[m] = dist[n] + weight
                        adjac_map[m] = n
 
                        if m in list_closed: #if it was in closed-list, move to open-list
                            list_closed.remove(m)
                            list_open.add(m)
 
            list_open.remove(n)
            list_closed.add(n) #move n to closed-list

        print('Path does not exist!')
        return None

#From given in the question g()
list_adjac = {
    'Perseverance': [('ChkPt-7', 77), ('ChkPt-9', 142), ('ChkPt-1', 120)],
    'ChkPt-1': [('ChkPt-2', 113)],
    'ChkPt-2': [('ChkPt-3', 72)],
    'ChkPt-3': [('ChkPt-4', 77)],
    'ChkPt-4': [('ChkPt-5', 122)],
    'ChkPt-5': [('ChkPt-6', 126)],
    'ChkPt-6': [('ChkPt-12', 148), ('ChkPt-11', 140)],
    'ChkPt-7': [('ChkPt-8', 71)],
    'ChkPt-8': [('ChkPt-9', 122)],
    'ChkPt-9': [('ChkPt-10', 111), ('ChkPt-12', 82)],
    'ChkPt-10': [('Jezero', 213)],
    'ChkPt-11': [('Jezero', 105)],
    'ChkPt-12': [('ChkPt-11', 99)],
}
graph1 = Graph(list_adjac)
graph1.algorithm('Perseverance', 'Jezero')
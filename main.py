import node_object
from graph_creator import create_graph


#Main code of the program, find the shortest route from start to end node using the A* algorithm implementation
open_list = []
closed_list = []

graph = create_graph("generated30-1.cav")

graph[0].set_h(graph[-1])
graph[0].set_f()
open_list.append(graph[0])

for node in open_list:
	current = open_list.pop()
	closed_list.append(current)
	if current.children:
		for child in current.children:
			if closed_list.count(graph[child - 1]) > 0:
				print("Already closed!")
				continue
			elif open_list.count(graph[child - 1]) > 0:
				print("Already open")
				for cave in open_list:
					if(cave.index == graph[child - 1].index):
						if graph[child - 1].g < cave.g:
							cave.parent = current
							cave.set_g
							cave.set_f
							open_list.sort(key = lambda x: x.f, reverse=True)
							continue
			else:
				print("Not on open list")
				graph[child-1].set_g
				graph[child-1].set_h
				graph[child-1].set_f
				open_list.append(graph[child-1])
				open_list.sort(key = lambda x: x.f, reverse=True)
	else:
		continue
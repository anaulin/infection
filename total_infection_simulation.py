# -*- coding: utf-8 -*-

import infection
import matplotlib.pyplot as plt
import networkx as nx
import random


def create_fake_graph():
  graph = nx.Graph()
  nodes = range(1, 100)
  graph.add_nodes_from(nodes)
  # 10 random nodes will be "coaches".
  coaches = random.sample(nodes, 10)
  # Each coach gets 8 random students. A coach can be a student too.
  for coach in coaches:
    students = random.sample(nodes, 8)
    for student in students:
      graph.add_edge(coach, student)
  return graph


if __name__ == '__main__':
  # Creates a fake random graph, totally infects it and visualizes the results.
  graph = create_fake_graph()
  infection_source = random.sample(graph.nodes(), 1)
  infected = infection.total_infection(graph, infection_source[0])
  not_infected = list(set(graph.nodes()) - set(infected))

  pos = nx.spring_layout(graph)
  nx.draw_networkx_nodes(graph, pos, nodelist=infected, node_color='r')
  nx.draw_networkx_nodes(graph, pos, nodelist=not_infected, node_color='g')
  nx.draw_networkx_edges(graph, pos)
  plt.axis('off')
  plt.show()

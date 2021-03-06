# -*- coding: utf-8 -*-

import argparse
import infection
import networkx as nx
import random


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--num_nodes', help='Number of nodes in the graph.',
      default=100)
  args = parser.parse_args()

  # Creates a fake random graph, and totally infects it from a random node.
  graph = infection.create_random_khan_graph(int(args.num_nodes))
  infection_source = random.choice(graph.nodes())
  infected = infection.total_infection(graph, infection_source)
  infection.display_infected_graph(graph, infected)

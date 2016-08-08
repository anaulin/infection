# -*- coding: utf-8 -*-

import argparse
import infection
import networkx as nx


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--num_nodes', help='Number of nodes in the graph.',
      default=100)
  parser.add_argument('--limit', help='Number of nodes in the graph.',
      default=50)
  args = parser.parse_args()

  graph = infection.create_random_khan_graph(int(args.num_nodes))
  infected = infection.limited_infection(graph, int(args.limit))
  infection.display_infected_graph(graph, infected)

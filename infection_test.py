# -*- coding: utf-8 -*-

import infection
import networkx as nx
import unittest

class TestInfection(unittest.TestCase):
  def test_total_infection_all_connected(self):
    # A graph where all nodes are connected.
    graph = nx.Graph()
    nodes = [1, 2, 3, 4, 5]
    graph.add_nodes_from(nodes)
    graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

    # Infecting from any node should infect the whole graph.
    for i in nodes:
      infected = infection.total_infection(graph, i)
      self.assertItemsEqual(nodes, infected)

  def test_total_infection_disconnected(self):
    # A graph with no edges.
    graph = nx.Graph()
    nodes = [1, 2, 3, 4, 5]
    graph.add_nodes_from(nodes)

    # Infecting from any node should just infect itself.
    for i in nodes:
      infected = infection.total_infection(graph, i)
      self.assertItemsEqual([i], infected)

  def test_total_infection_with_cycle(self):
    # A graph with a cycle in it. There are no disconnected nodes.
    graph = nx.Graph()
    nodes = [1, 2, 3, 4, 5]
    graph.add_nodes_from(nodes)
    graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 2), (4, 5)])

    # Infecting from any node should infect the whole graph.
    for i in nodes:
      infected = infection.total_infection(graph, i)
      self.assertItemsEqual(nodes, infected)


if __name__ == '__main__':
  unittest.main()

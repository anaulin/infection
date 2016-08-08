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


  def test_limited_infection_disconnected(self):
    # A graph with no edges. Precise limit is always possible.
    graph = nx.Graph()
    nodes = range(1,10)
    graph.add_nodes_from(nodes)

    for i in nodes:
      infected = infection.limited_infection(graph, i)
      self.assertEqual(i, len(infected))


  def test_limited_infection_bad_limit_raises(self):
    # A graph with 1 node
    graph = nx.Graph()
    graph.add_node(1)

    self.assertRaises(ValueError, infection.limited_infection, graph, 2)


  def test_limited_infection_caveman_graph(self):
    # A caveman graph has a bunch of cliques of the same size.
    # We can only approximate the limit by the size of the cliques.
    graph = nx.caveman_graph(10, 3)  # 10 cliques of size 3

    # 9 is multiple of 3, we can do match this limit precisely.
    infected = infection.limited_infection(graph, 9)
    self.assertEqual(9, len(infected))

    # 10 is not a multiple of 3. We'll approximate with the next multiple of 3.
    infected = infection.limited_infection(graph, 10)
    self.assertEqual(12, len(infected))


if __name__ == '__main__':
  unittest.main()

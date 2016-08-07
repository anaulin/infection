# -*- coding: utf-8 -*-

import networkx as nx

def total_infection(graph, root_user):
  """Returns all infected nodes of the graph, with infection starting at the
  given root_user.

  Args:
    graph (networkx.Graph): Graph to infect. Nodes are assumed to be integers,
    representing a user id.
    root_user (int): Node id of the user to use as the root of the infection.

  Returns:
    list of int: The nodes (or users) that were infected.
  """
  infected = _recursively_infect(graph, root_user, {})
  return infected.keys()

def _recursively_infect(graph, node, infected):
  """A recursive graph infection implementation.

  Uses a dictionary to keep track of already infected nodes. A dictionary makes
  the lookup of a new node in the dictionary more efficient than if we used a
  list.

  Args:
    graph (nx.Graph): The graph to infect.
    node (int): The node to use as the root of the infection.
    infected (dict{int: bool}): Dictionary with already infected nodes.

  Returns:
     dict{int: bool}: A dictionary containing only nodes that were infected.
  """
  # If we've infected this node earlier, then we have a cycle in the graph
  # and can stop this branch of the infection here.
  if node in infected:
    return infected

  # Record current node as infected.
  infected[node] = True

  # Infect all neighbors of the current node, if any.
  neighbors = graph.neighbors(node)
  for neighbor in neighbors:
    _recursively_infect(graph, neighbor, infected)

  return infected

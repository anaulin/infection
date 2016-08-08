# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
import random

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


def limited_infection(graph, limit):
  """Infects a section of the given graph, attempting to match the given
  limit as closely as possible.

  Args:
    graph (nx.Graph): The graph to infect.
    limit (int): Desired number of nodes to infect.

  Returns:
    list of int: Nodes infected.

  Raises:
    ValueError if the desired limit is larger than the total size of the graph
  """
  nodes = graph.nodes()
  if limit > len(nodes):
    raise ValueError("Desired limit is bigger than total node count.")

  infected = {}
  for node in nodes:
    if len(infected.keys()) >= limit:
      # We have infected enough nodes. Stop.
      break

    if node in infected:
      # We've already infected a sub-graph containing this node. Skip.
      continue

    # Infect whatever part of the graph is connected to this node.
    infected = _recursively_infect(graph, node, infected)

  return infected.keys()


def _recursively_infect(graph, node, infected):
  """A recursive graph infection implementation. Infects all nodes reachable
  from the given node.

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


def create_random_khan_graph(node_count):
  """Returns a randomly created graph that approximates the Khan Academy user
  graph.

  Note that the shape of this graph is based entirely on conjecture, and not
  on any actual knowledge of the Khan Academy user base.

  This function creates a graph with the following assumptions:
    * Some of the users are assembled in classrooms of size 10 to 20.
    * Each classroom has 1 "teacher" (i.e. a node that is connected to all the
      other nodes belonging to that classroom).
    * A teacher might have more than one class. This is chosen at random.
    * A student might belong to more than one class.
    * Some of the users are independent learners -- they are not connected to
      anyone else on the graph.
    * About 50% of the users are in classrooms, and 50% are independent learners.
      These percentages are only approximated by the creation algorithm.

  Args:
    node_count (int): Desired number of total nodes in the graph.

  Returns:
    nx.Graph: A randomly-created graph with node_count nodes.

  Raises:
    ValueError: If a negative node_count is requested.
  """
  if node_count < 0:
    raise ValueError("Can't produce graph with negative node_count.")

  graph = nx.Graph()
  nodes = range(1, node_count + 1)
  graph.add_nodes_from(nodes)

  classroom_users = 0
  while classroom_users < node_count/2:
    # Make a random classroom with a random size, teacher and students.
    size = min(random.randrange(10, 20), node_count)
    teacher = random.choice(nodes)
    students = random.sample(nodes, size)
    for student in students:
      graph.add_edge(teacher, student)
    classroom_users += size

  return graph


def display_infected_graph(graph, infected):
  """Displays the given graph with the infected nodes in a different color.

  This function will open a plot on the screen. Execution halts until the user
  closes the window with the plot.

  Args:
    graph (nx.Graph): Graph to display.
    nodes (list of int): Nodes in the graph which are "infected".
  """
  not_infected = list(set(graph.nodes()) - set(infected))

  pos = nx.spring_layout(graph)
  nx.draw_networkx_nodes(graph, pos, nodelist=infected, node_color='r')
  nx.draw_networkx_nodes(graph, pos, nodelist=not_infected, node_color='g')
  nx.draw_networkx_edges(graph, pos)
  plt.axis('off')
  plt.show()

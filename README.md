# infection

## Overview

Python implementation of `total_infection` and `limited_infection` functions, to
propagate a property through a graph, given a root node.

Written in response to Khan Academy's "Limited Infection" take-home interview
project. See [document](https://docs.google.com/document/d/1NiKv-MjULOFyyc8f5w8R_EqvuPJ10wJVJgZhtTK9VKc/edit#) for detailed specification.

Uses the `networkx` library for graph representation, manipulation and
visualization.

## Installation and testing

To install the required dependencies:

```bash
$ pip install -r requirements.txt
```

To run the tests:

```bash
$ python infection_test.py
```

## Visualization

Simulation programs are provided to visualize the effects of these two
infection methods on a randomly generated graph.

The random graph is intended to be of a shape roughly similar to what I imagine
the Khan Academy user graph to be: a number of "classrooms", with one teacher
coaching a few students, and a large number of individual learners,
not connected to any other node in the graph.

The shape of this randomly created graph is based entirely on conjecture, and
not on any actual knowledge of the Khan Academy user base. For details on the
underlying assumptions made, see the docstring of `create_random_khan_graph`
in `infection.py`.

### Total infection

To run the `total_infection` visualization:

```bash
$ python total_infection_simulation.py
```

It defaults to 100 nodes, but the count can be adjusted using the
optional `--num_nodes` argument:

```bash
$ python total_infection_simulation.py --num_nodes=<num_nodes_desired>
```

### Limited infection

To run the `limited_infection` visualization:

```bash
$ python limited_infection_simulation.py
```

It defaults to 100 nodes and a limit of 50, but these numbers can be controlled
with the optional `--num_nodes` and `--limit` arguments:

```bash
$ python limited_infection_simulation.py \
  --num_nodes=<num_nodes_desired> \
  --limit=<limit>
```

## Implementation details and discussion

### Total infection

The `total_infection` function is implemented as a recursive traversal of the
graph, starting at the given node.

It keeps track of already visited nodes in order to avoid an infinite loop if
the graph contains a cycle. Keeping track of visited nodes also allows for a
more efficient implementation, since we don't visit a given sub-graph more than
once.

This implementation assumes that we can hold the entire graph in memory, and
that we will not have a stack overflow problem. This might not be true in
practice, if the user base is very large.

### Limited infection

The `limited_infection` implementation iterates over the graph nodes infecting
their subgraphs, until a number of nodes equal to or larger than the requested
`limit` has been infected. It uses the same sub-graph infection algorithm used
to implement `total_infection`, and keeps track of previously infected nodes.

This greedy algorithm does not guarantee an infection optimally close to the
requested `limit`, but is in practice probably good enough for the shape of
the graph that I imagine the Khan Academy user base to have. I am assuming the
Khan graph to be composed of many small sub-graphs and isolated nodes.

An advantage of this implementation over other possibilities is that it fully
infects connected nodes, which ensures that no pair in a coaching relationship
will see a different version of the site.

For a general graph, this implementation could do very poorly. For example, in
a typical social media graph, with super-influencers connected to large swaths
of network, this greedy algorithm will tend to overshoot the requested limit by
a large amount.

In a graph with paths between all nodes, the entire graph would become infected.
In this case the chosen implementation would be completely unusable as a way of
choosing candidates for an A/B test.

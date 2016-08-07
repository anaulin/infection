# infection

## Overview

Python implementations of `total_infection` and `limited_infection` functions, to
propagate a property (or infection) through a graph, given a root node.

Uses the `networkx` library for graph representation, manipulation and
visualization.

This library expects the complete graph to be loaded in memory. This obviously
might not work for a large enough user base. In that case, more complicated
distributed implementations will be necessary.

## Visualization

A simulation example is provided to visualize the effects of these two
infection methods on a randomly generated graph, with a random source of
infection.

The random graph is intended to be of a shape roughly similar to what I imagine
the Khan Academy user graph to be: a number of "classrooms", with one teacher
coaching a few students, and a large number of individual learners,
not connected to any other node in the graph.

To run the visualization example:

```bash
$ python total_infection_simulation.py
```

## Installation and usage
To install the required dependencies:

```bash
$ pip install -r requirements.txt
```

To run the tests:

```bash
$ python infection_test.py
```

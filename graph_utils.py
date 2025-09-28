#!/usr/bin/env python3

# BSD 3-Clause License
# 
# Copyright (c) 2025, Stan Baek
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Author: Stan Baek
# Date Created: Sep 24, 2025
# Last Modified: Sep 24, 2025
# Description: Implementations of the dijkstra's algorithm.

# Required: 
# pip install networkx    

import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generate_random_weighted_graph(num_nodes=4, edge_prob=0.3, weight_range=(1, 10), seed=None) -> np.ndarray:
    """
    Generate a random weighted graph with numeric node labels.
    Plot it and return adjacency matrix and adjacency list.

    Parameters:
    num_nodes (int): Number of nodes
    edge_prob (float): Probability of edge creation between nodes (0 to 1)
    weight_range (tuple): Range of edge weights (min, max)
    seed (int): Random seed for reproducibility

    Returns:
    adj_matrix (numpy.ndarray): Weighted adjacency matrix
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    # Generate random graph
    G = nx.erdos_renyi_graph(n=num_nodes, p=edge_prob, seed=seed)


    # Assign random weights to edges
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(weight_range[0], weight_range[1])

    # Weighted adjacency matrix
    nodes = sorted(G.nodes())
    adj_matrix = nx.to_numpy_array(G, nodelist=nodes, weight="weight", dtype=int)

    return adj_matrix


def draw_graph_with_path(G, source, target):
    """
    Draw the graph and highlight the shortest path between source and target.
    """
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Find shortest path using Dijkstra
    try:
        path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
        path_edges = list(zip(path, path[1:]))
    except nx.NetworkXNoPath:
        path = []
        path_edges = []

    # Draw base graph
    plt.figure(figsize=(7, 7))
    nx.draw(G, pos, with_labels=True, node_color="lightgreen",
            node_size=700, edge_color="gray", font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight shortest path (if exists)
    if path:
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="yellow")
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

        plt.title(f"Shortest Path from {source} to {target}: {path}")
    else:
        plt.title(f"No Path from {source} to {target}")

    plt.show()
        

def test_dijkstra(adj_matrix: np.ndarray, path: list[int], source: int, target: int, show_graph: bool = True) -> None:
    """
    Test the dijkstra algorithm
    """
    print(f"Your shortest path from {source} to {target}:")
    print(path)
     
    # Create graph from adjacency matrix
    G = nx.from_numpy_array(adj_matrix)
    try:
        shortest_path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
    except nx.NetworkXNoPath:
        shortest_path = []   # or None, depending on what you want
    print(f"Correct shortest path from {source} to {target}:")
    print(shortest_path)

    if path == shortest_path:
        print("Your implementation is correct!")
    else:
        print("Your implementation is incorrect.")
            
    # Draw graph and shortest path between node 1 and node 6
    if show_graph:
        draw_graph_with_path(G, source=source, target=target)   
        
        
if __name__ == "__main__":
    pass
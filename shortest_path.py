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
# Last Modified: Sep 28, 2025
# Description: Implementations of the dijkstra's algorithm.

# Required: 
# pip install networkx    


import numpy as np
from graph_utils import generate_random_weighted_graph, test_dijkstra

    
def dijkstra(adj_matrix: np.ndarray, source: int, target: int) -> list[int]:
    
    num_nodes = adj_matrix.shape[0]
    L = [float('inf')] * num_nodes
    L[source] = 0
    pred = [None] * num_nodes
    S = set()

    while target not in S:
        # Use the Pseudo code from L16 S14 as a guide
        # TODO: Write your code here


        # If no reachable node remains, return empty path
        if u is None or L[u] == float('inf'):
            return []
               
        # Mark node as visited               
        S.add(u)

        # TODO: Write your code here
        for v in range(num_nodes):







    # Reconstruct path from target back to source
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = pred[current]

    path.reverse()
    return path if path and path[0] == source else []


def main() -> None:     
    """
    Runs multiple test cases to validate Dijkstra's algorithm implementation.
    Includes fixed examples and randomly generated graphs.
    """
    show_graph = True   # Toggle graph visualization
    
    ####################################################
    # DO NOT MODIFY the test cases below.
    ####################################################
    
    adj_matrix = np.array([
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ])

    path = dijkstra(adj_matrix, source=0, target=2)
    test_dijkstra(adj_matrix, path, source=0, target=2, show_graph=show_graph)
    print("\n")
    
    # Lecture example - L16 Slide 5
    adj_matrix = np.array([
        [0, 7, 9, 0, 14, 0],
        [7, 0, 10, 15, 0, 0],
        [9, 10, 0, 12, 2, 0],
        [0, 15, 12, 0, 0, 6],
        [14, 0, 2, 0, 0, 9],
        [0, 0, 0, 6, 9, 0]
    ])
    path = dijkstra(adj_matrix, source=0, target=5)
    test_dijkstra(adj_matrix, path, source=0, target=5, show_graph=show_graph)
    
    print("\n")
    
    # Lecture example - L16 Slide 20
    adj_matrix = np.array([
        [0, 4, 2, 0, 0, 0],
        [4, 0, 1, 5, 0, 0],
        [2, 1, 0, 8, 10, 0],
        [0, 5, 8, 0, 2, 6],
        [0, 0, 10, 2, 0, 3],
        [0, 0, 0, 6, 3, 0]
    ])
    path = dijkstra(adj_matrix, source=0, target=5)
    test_dijkstra(adj_matrix, path, source=0, target=5, show_graph=show_graph)
    print("\n")
    
    # Exercise 10.6.2
    adj_matrix = np.array([
        [0, 2, 3, 0, 0, 0],
        [2, 0, 0, 5, 2, 0],
        [3, 0, 0, 0, 5, 0],
        [0, 5, 0, 0, 1, 2],
        [0, 2, 5, 1, 0, 4],
        [0, 0, 0, 2, 4, 0]
    ])
    path = dijkstra(adj_matrix, source=0, target=5)
    test_dijkstra(adj_matrix, path, source=0, target=5, show_graph=show_graph)
    print("\n")
    
    # No path to target
    adj_matrix = np.array([
        [0, 2, 3, 0],
        [2, 0, 1, 0],
        [3, 1, 0, 0],
        [0, 0, 0, 0],
    ])
    path = dijkstra(adj_matrix, source=0, target=3)
    test_dijkstra(adj_matrix, path, source=0, target=3, show_graph=show_graph)
    print("\n")
    
    # Random graph tests with fixed seed
    seed = 45
    adj_matrix = generate_random_weighted_graph(num_nodes=5, edge_prob=0.3, weight_range=(1, 8), seed=seed)
    path = dijkstra(adj_matrix, source=0, target=4)
    test_dijkstra(adj_matrix, path, source=0, target=4, show_graph=show_graph)
    print("\n")

    adj_matrix = generate_random_weighted_graph(num_nodes=8, edge_prob=0.3, weight_range=(1, 8), seed=seed)
    path = dijkstra(adj_matrix, source=1, target=4)
    test_dijkstra(adj_matrix, path, source=1, target=4, show_graph=show_graph)
    print("\n")

    adj_matrix = generate_random_weighted_graph(num_nodes=10, edge_prob=0.4, weight_range=(1, 8), seed=seed)
    path = dijkstra(adj_matrix, source=4, target=6)
    test_dijkstra(adj_matrix, path, source=4, target=6, show_graph=show_graph)
    print("\n")

    adj_matrix = generate_random_weighted_graph(num_nodes=12, edge_prob=0.5, weight_range=(1, 8), seed=seed)
    path = dijkstra(adj_matrix, source=3, target=7)
    test_dijkstra(adj_matrix, path, source=3, target=7, show_graph=show_graph)
    print("\n")

    adj_matrix = generate_random_weighted_graph(num_nodes=15, edge_prob=0.2, weight_range=(1, 8), seed=seed)
    path = dijkstra(adj_matrix, source=11, target=14)
    test_dijkstra(adj_matrix, path, source=11, target=14, show_graph=show_graph)
    print("\n")


if __name__ == "__main__":
    main()
    
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
# Date Created: Sep 6, 2025
# Last Modified: Sep 6, 2025
# Description: Implementations of linear search and binary search algorithms.

import random


def linear_search(sequence: list[int], target: int) -> int:
    """
    Perform linear search on an array to find the index of the target value.

    Parameters:
    sequence (list): A list of integers.
    target: The element to search for in the sequence.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    
    # Ensure indexing starts from 0 in Python.
    # For the length of the sequence, use len(sequence).
    
    index = 0
    while index < len(sequence) and sequence[index] != target:
        index += 1

    if index < len(sequence):
        return index
    return -1


def binary_search(sequence: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    sequence (list): A list of sorted integers.
    target: The element to search for in the sequence.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
 
    # Write your code here based on the pseudocode provided in Lecture 11 Slide 11.
    # Ensure indexing starts from 0 in Python.
    # For the length of the sequence, use len(sequence).
    return 0  # Replace this line with your implementation.


def test() -> None:
    """
    Test the searching algorithms with random data.
    """

    num_elemts = 20
    range_elemts = 25

    print("Linear Search:")
    for _ in range(5):
        seq = random.sample(range(1, range_elemts + 1), num_elemts)
        target = random.randint(1, range_elemts + 1)
        print(seq)
        result = linear_search(seq, target)
        print(f"Element {target} found at index: {result}" if result != -1 else f"Element {target} not found.")
        print()

    print("Binary Search:")
    for _ in range(5):
        seq = random.sample(range(1, range_elemts + 1), num_elemts)
        seq.sort()  # Binary search requires a sorted array
        target = random.randint(1, range_elemts + 1)
        print(seq)
        result = binary_search(seq, target)
        print(f"Element {target} found at index: {result}" if result != -1 else f"Element {target} not found.")
        print()


if __name__ == "__main__":
    test()
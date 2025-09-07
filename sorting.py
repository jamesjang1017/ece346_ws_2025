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
import time
import matplotlib.pyplot as plt


def bubble_sort(sequence: list[int]) -> None:
    """
    Perform bubble sort on an array to sort the elements in ascending order.

    Parameters:
    sequence (list): A list of integers.

    Returns:
    None: The input list is sorted in place.
    """
   
    # Ensure indexing starts from 0 in Python.
    # For the length of the sequence, use len(sequence).

    n = len(sequence)
    for i in range(n):
        for j in range(0, n-i-1):
            if sequence[j] > sequence[j+1]:
                # Swap if the element found is greater than the next element
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


def insertion_sort(sequence: list[int]) -> None:
    """
    Perform insertion sort on an array to sort the elements in ascending order.

    Parameters:
    sequence (list): A list of integers.

    Returns:
    None: The input list is sorted in place.
    """

    # Write your code here based on the pseudocode provided in Lecture 11 Slide 6.
    # Ensure indexing starts from 0 in Python.
    # For the length of the sequence, use len(sequence).


def test() -> None:
    """
    Test the searching algorithms with random data.
    """

    num_elemts = 10
    range_elemts = 30
    
    print("Bubble Sort:")
    for _ in range(5):
        seq = random.sample(range(1, range_elemts + 1), num_elemts)
        print(seq)
        bubble_sort(seq) # Python passes by object reference — it's pointer-like. Deal with it.
        print(seq)
        print()

    print("Insertion Sort:")
    for _ in range(5):
        seq = random.sample(range(1, range_elemts + 1), num_elemts)
        print(seq)
        insertion_sort(seq) # Python passes by object reference — it's pointer-like. Deal with it.
        print(seq)
        print()


def benchmark() -> None:
    """
    Benchmark the performance of sorting algorithms.
    """

    sizes = list(range(100, 3001, 100))
    bubble_times = []
    insertion_times = []

    for size in sizes:
        seq = random.sample(range(1, size * 10), size)

        start_time = time.time()
        bubble_sort(seq.copy())
        bubble_times.append(time.time() - start_time)

        start_time = time.time()
        insertion_sort(seq.copy())
        insertion_times.append(time.time() - start_time)

    plt.plot(sizes, bubble_times, label='Bubble Sort')
    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Benchmark')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test()
    # benchmark()
    
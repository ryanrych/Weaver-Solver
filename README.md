# Weaver-Solver
A Python program to solve the daily word game "Weaver".

It takes the list all of of their possible words (found in their source code) and creates an unweighted graph connecting words of "edit distance" equal to 1. It then uses a DFS based algorithm to find the shortest path on the graph, therefore solving the word puzzle.

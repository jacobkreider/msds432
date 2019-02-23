#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:28:15 2019

@author: jacob
"""
#%% [markdown]
## Implementing Dijkstra's algorithm

# We'll need three has tables- one for the graph network, one for
# costs, and one for parents

#%%
# We'll create the graph much like in chapter 6
# graph = {}
# graph["you] = ["alice", "bob", "claire"]

# We need to store both the neighbors and the cost of getting to that neighbor
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# Graph["start"] is a has table. Let's get the neighbors:
print(graph["start"].keys())

# We can also find the edge weights between these neighbors
print(graph["start"]["a"])
print(graph["start"]["b"])

#%%
# Adding the rest of the nodes and neighbors
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# The finish node has no neighbors:
graph["fin"] = {}

#%% [markdown]
#### Create a hash table to store the costs for each node

# We know the costs for a and b, but not the cost to get to fin, so we'll
# store that as infinity

#%%

# Storing costs for each node that we know, and infinity for what we don't

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#%%

# Create a hash table to store the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["b"] = None

# Last, we need an array to keep track of all processed nodes so we don't
# process them more than once

processed = []

#%% [markdown]
## Dijkstra's Algorithm

#%%
# function to find the lowest cost node, check neighboring costs, and updating
# the costs and parents to reflect the cheapest path

def findLowestCostNode(costs):
    lowestCost = float("inf")
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

#%%
# The algorithm
    
node = findLowestCostNode(costs) # Find lowest cost, unprocessed node
while node is not None: # While loop ends when all nodes have been processed
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Go through all neighors of node in question
        newCost = cost + neighbors[n] # Find cost to get to node through neighbor
        if costs[n] > newCost: # If it is cheaper this way
            costs[n] = newCost # update the cost to reflect this
            parents[n] = node # This node is now the parent of the neighbor
    processed.append(node) # mark the node as processed
    node = findLowestCostNode(costs) # Process the next node and loop
    
#%%


    

            

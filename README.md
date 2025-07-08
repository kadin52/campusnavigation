# University Campus Smart Navigation System

## Overview

This project aims to develop a smart navigation system specifically for a university campus. The system helps users find the shortest or most optimal paths to various campus locations, such as lecture halls, libraries, cafeterias, and administrative buildings. Routes are provided based on different criteria such as distance, time, and accessibility.

## Objectives

1. **Implement a Graph-Based Map of the Campus**  
   - Model the campus layout as a graph where locations (nodes) are connected by paths (edges) with attributes such as distance, estimated travel time, and accessibility features.

2. **Pathfinding Algorithms Implementation**  
   Utilize BFS, DFS, and Dijkstra's Algorithm to offer different routing options:
   - **BFS:** Find the shortest path by the number of edges (stops).
   - **DFS:** Explore all possible paths and potentially identify routes with specific characteristics (e.g., scenic routes that pass by certain landmarks).
   - **Dijkstra's Algorithm:** Determine the shortest path based on weighted criteria such as time or distance.

## Tasks and Roles

### Step 1: Graph Construction and Data Integration
- **Data Collection:**  
  Collect data regarding different campus paths, distances, and connectivity.
- **Modeling the Campus:**  
  Represent the campus as a graph using an appropriate data structure such as an adjacency list or adjacency matrix.

### Step 2: Algorithm Implementation (BFS and DFS)
- **BFS:**  
  Implement the Breadth-First Search algorithm to compute the shortest path by the number of stops.
- **DFS:**  
  Implement the Depth-First Search algorithm to explore all possible paths, enabling the identification of specific route characteristics (e.g., scenic routes).
- **Path Retrieval and Display:**  
  Develop functionality to retrieve and display paths identified by these algorithms.

### Step 3: Algorithm Implementation (Dijkstra’s Algorithm)
- **Weighted Shortest Path:**  
  Implement Dijkstra’s Algorithm to compute the shortest path based on edge weights such as distance or time.
- **Dynamic Inputs:**  
  Ensure the algorithm can handle dynamically changing inputs (e.g., temporarily unavailable paths or changing conditions).

### Step 4: User Interface and Accessibility Features
- **UI Development:**  
  Create a simple User Interface (UI) that allows users to select start and end points on the campus map.
- **Accessibility:**  
  Integrate accessibility features to enhance the user experience for all users.

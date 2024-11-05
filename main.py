
import googlemaps
import networkx as nx
import webbrowser

from tkinter import Button,Frame
import tkinter.simpledialog as simpledialog
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests, json

from google_maps import get_coordinates, calc_travel
from address import create_addresses
from manual_nodes import create_nodes
from debug import print_nodes, print_address
from algorithms import bfs_shortest_path,dijkstra,dfs_maze_solver


fig, ax = plt.subplots(figsize=(15, 20))

def display_nodes(nodes):

    ax.clear()
    image = img.imread("csufcampus.png")
    ax.imshow(image,extent=[0,1000,0,1000])


    for i, ((lon,lat),abbr) in nodes.items():
        ax.plot(lon,lat,'ro', markersize=10, color = 'purple')

    plt.show()

def highlight_path(path,nodes):
    for i in range(len(path)-1):
        lon1, lat1 = nodes[path[i]][0]  # Starting point coordinates (longitude and latitude)
        lon2, lat2 = nodes[path[i + 1]][0]  # Ending point coordinates (longitude and latitude)
        ax.plot([lon1, lon2], [lat1, lat2], 'go-', markersize=12)  # Plot the line segment with green markers
    plt.draw()  # Update the plot

def convert_abbr_to_index(abbr, manual_nodes):
    index = 0
    for i, ((lon, lat), node_abbr) in manual_nodes.items():
        if node_abbr == abbr:
            index = i
            return index

def convert_travel_info_to_adj_list(travel_info):
    adj_list = {}

    for (i, j), (travel_time, distance) in travel_info.items():
        if i not in adj_list:
            adj_list[i] = []
        if j not in adj_list:
            adj_list[j] = []
        adj_list[i].append(j)
        adj_list[j].append(i)
    return adj_list


def run_algorithm(algorithm, manual_nodes, adj_list):
    start_abbr = simpledialog.askstring("Input", "Enter starting node abbreviation:")
    end_abbr = simpledialog.askstring("Input", "Enter destination node abbreviation")

    start_index = convert_abbr_to_index(start_abbr, manual_nodes )
    end_index = convert_abbr_to_index(end_abbr, manual_nodes )

    print(f"{start_index} -> {end_index}")
    if start_index is None or end_index is None:# or start_index not in coordinates or end_index not in coordinates:
        print("invalid")
        return

    # start_node = adj_list.nodes[start_index]
    # end_node = adj_list.nodes[end_index]
    start_node = start_index
    end_node = end_index


    if algorithm == 'BFS':
        path = bfs_shortest_path(adj_list, start_node, end_node)

    elif algorithm == 'DFS':
        path = dfs_maze_solver(adj_list,start_node,end_node)

    print("Path:", path)

def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        lon, lat = int(event.xdata), int(event.ydata)
        current_nodes = create_nodes()
        node_id = max(current_nodes.keys()) + 1 if current_nodes else 0
        print(f"{node_id}: (({lon}, {lat}), 'Node{node_id}')")
    else:
        print("Click outside the plot area")

def main():
    global scale
    scale = 1.0


    # G = nx.Graph()
    # for i, coord in enumerate(coordinates):
    #     G.add_node(i, pos=(coord[1],coord[0]))
    # for (i, j), (travel_time, distance) in travel_info.items():
    #     G.add_edge(i, j, weight=distance)

    building_nodes = create_nodes()



    root = tk.Tk()
    root.title("Tkinterwindow")

    # frame = Frame(root)
    # frame.pack(fill="both",expand=True)
    # Button(root, text="Run BFS", command=lambda: run_algorithm('BFS', building_nodes, adj_list)).pack(side='left')
    # Button(root, text="Run DFS", command=lambda: run_algorithm('DFS', building_nodes, adj_list)).pack(side='left')
    # Button(root, text="Run Dijkstra").pack(side='left')


    display_nodes(building_nodes)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    cid = fig.canvas.mpl_connect('button_press_event',on_click)

    # Add buttons to zoom in and zoom out

    root.mainloop()

    print("bye")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()











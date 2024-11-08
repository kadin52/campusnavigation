

import networkx as nx

from tkinter import Button, Frame, messagebox

import tkinter.simpledialog as simpledialog
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as img

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from adjacency_list import create_adjacency_list, create_undirected_adjacency_list, calc_weights
from manual_nodes import create_nodes
from algorithms import bfs_shortest_path,dijkstra,dfs_maze_solver
from weights import  weights
from run_algorithms_help import convert_graph_to_adj_list,calc_distance,convert_abbr_to_index

fig, ax = plt.subplots(figsize=(15, 20))
original_xlim = ax.get_xlim()
original_ylim = ax.get_ylim()



def run_algorithm(algorithm, manual_nodes, adj_list,G):
    start_abbr = simpledialog.askstring("Input", "Enter starting node abbreviation:")
    end_abbr = simpledialog.askstring("Input", "Enter destination node abbreviation")

    start_index = convert_abbr_to_index(start_abbr, manual_nodes )
    end_index = convert_abbr_to_index(end_abbr, manual_nodes )

    print(f"{start_index} -> {end_index}")
    if start_index is None or end_index is None:#
        print("invalid")
        return


    start_node = start_index
    end_node = end_index



    if algorithm == 'BFS':
        path = bfs_shortest_path(adj_list, start_node, end_node)


    elif algorithm == 'DFS':

        path = dfs_maze_solver(adj_list,start_node,end_node)

    elif algorithm == 'Dijkstra':
         d,path = dijkstra(G,start_node,end_node)
       #d,path = dijkstra(adj_list, start_node,end_node)

    print("Path:", path)

    distance = int(calc_distance(G,path))
    time = distance / 1.2 / 60 #avg human walking, minutes
    show_path(G,path)
    messagebox.showinfo("Travel Info",
                f"Total distance: {distance} meters\n\n"
                        f"Time: {time: .2f} minute(s)")

def show_path(G,path):
    print("showpath")

    #pos = {node: (coords[0], coords[1]) for node, (coords, _) in create_nodes().items()}
    pos = {}
    node_colors = []
    edges_in_path = []
    nodes_pos = create_nodes()

    if not pos:
        for node, info in nodes_pos.items():
            coords,_ = info
            lon,lat = coords
            pos[node] = (lon,lat)
        nx.set_node_attributes(G, pos, 'pos')


    for node in G.nodes():
        if node in path:
            node_colors.append('green')
        else:
            node_colors.append('red')

    for i in range(len(path)-1):
        edge = (path[i],path[i+1])
        edges_in_path.append(edge)

    edge_colors = []
    edge_widths = []
    for i, j in G.edges():
        if (i, j) in edges_in_path or (j, i) in edges_in_path:
            edge_colors.append('green')
            edge_widths.append(2.0)
        else:
            edge_colors.append('red')
            edge_widths.append(1.0)

    #print over display_graph
    nx.draw_networkx(G, pos, node_size = 50, node_color=node_colors, edge_color=edge_colors,
                        width=edge_widths, with_labels=False)
    plt.draw()  # Refresh the plot to display the changes



def display_image():
    ax.clear()
    #image = img.imread("csufcampus.png")
    #image = img.imread("campusmap.png")
    image = img.imread("map.png")
    ax.imshow(image, extent=[0, 1000, 0, 1000])
    plt.draw()

def display_graph(G, nodes):
    pos = {}
    node_colors = []
    node_labels = {}
    for node, (coords, _) in nodes.items():
        x, y = coords
        pos[node] = (x, y)


    for _, (_,label) in nodes.items():
        if label == "pathing":
            node_colors.append("red")

        else:
            node_colors.append("gold")



    nx.draw_networkx(G, pos, node_size=50, node_color=node_colors,
                        with_labels=False, font_size=12,
                        width = 1, edge_color = 'red')
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos, edge_labels = edge_labels, font_size=7,
                                 bbox=dict(facecolor='none', edgecolor='none'))


#TS-TG dijkstra
def main():



    building_nodes = create_nodes()
    directional_adj_list = create_adjacency_list()
    adj_list = create_undirected_adjacency_list(directional_adj_list)
   # nond_adj_list = create_adjacency_list()
    weighted = calc_weights(adj_list, building_nodes)
    print(weighted)

    G = nx.Graph()
    for node in building_nodes:
        G.add_node(node)
    for node, neighbors in adj_list.items():
        #G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
           # print(f"{node} / {neighbor}")


    weights(adj_list,G)
    # for edge in G.edges(data=True):
    #     print(edge)

    root = tk.Tk()
    root.title("Tkinterwindow")

    frame = Frame(root)
    #frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
    frame.grid(row=0,column=0,sticky = "nsew")


    bfs_button = tk.Button(frame, text="BFS", command=lambda:
                    run_algorithm("BFS", building_nodes, adj_list,G),
                    bg='darkgrey')
    #bfs_button.pack(side=tk.RIGHT, pady = 10)
    bfs_button.grid(row=0,column=0,pady=10)

    dijkstra_button = tk.Button(frame, text="Dijkstra", command=lambda:
                                run_algorithm("Dijkstra", building_nodes, adj_list, G),
                                bg='darkgrey')
    #dijkstra_button.pack(side=tk.RIGHT, pady=10)
    dijkstra_button.grid(row=0,column=1,pady=10)

    dfs_button = tk.Button(frame, text="DFS", command=lambda:
                            run_algorithm("DFS", building_nodes, adj_list, G),
                           bg='darkgrey')
    #dfs_button.pack(side=tk.RIGHT, pady=10)
    dfs_button.grid(row=0,column=2,pady=10)


    reset_button = tk.Button(frame,text="reset", command=lambda:
                            zoom_out(G, building_nodes),
                                     bg='darkgrey')
    #reset_button.pack(side=tk.RIGHT, padx=10, pady=10)
    reset_button.grid(row=0, column=3, padx=10)

    display_image()
    display_graph(G, building_nodes)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().grid(row=1,column =0,columnspan=4,sticky="nsew")
    cid = fig.canvas.mpl_connect('button_press_event',on_click)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)



    fig.canvas.mpl_connect('scroll_event', zoom)

    root.mainloop()





def zoom_out(G,building_nodes):
    ax.set_xlim(original_xlim)
    ax.set_ylim(original_ylim)
    ax.clear()
    display_image()
    display_graph(G,building_nodes)
    fig.canvas.draw()


def zoom(event):

    if event.button =='up':
        scale = 1.2
    elif event.button =='down':
        scale = 0.9
    x, y = event.xdata, event.ydata
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    #center of the current view
    center_x = (x_max + x_min) / 2
    center_y = (y_max + y_min) / 2


    new_width = (x_max - x_min) / scale
    new_height = (y_max - y_min) / scale


    new_x_min = x - new_width/2
    new_x_max = x + new_width/2
    new_y_min = y - new_height/2
    new_y_max = y + new_height/2

    # Set new limits
    ax.set_xlim(new_x_min, new_x_max)
    ax.set_ylim(new_y_min, new_y_max)

    fig.canvas.draw()

node_index = max(create_nodes().keys())
def on_click(event):
    global node_index
    if event.xdata is not None and event.ydata is not None:
        lon, lat = int(event.xdata), int(event.ydata)

        print(f"{node_index}: (({lon}, {lat}), 'pathing'),")
    else:
        print("Click outside the plot area")
    node_index+=1




if __name__ == '__main__':
    main()





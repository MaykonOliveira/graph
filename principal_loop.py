import os

from models.Graph import Graph
from algorithms import ColorAlghoritms

graph = Graph(orientation=False)
color = ColorAlghoritms.Color()


def print_main_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add node")
    print("2. Add edge")
    print("3. Welsh Powell Apply")
    print("4. Plot graph")
    print("5. Exit")
    print(67 * "-")


loop = True

while loop:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_main_menu()
    choice = input("Enter your choice [1-5]: ")

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = input("Enter with the ID of the node: ")
        value = input("Enter with the value of the node: ")
        graph.add_node(id, value)

    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = input("Enter with the ID of the edge: ")
        start = input("Enter with the first node ID: ")
        end = input("Enter with the second node ID: ")
        weight = float(input("Enter with the weight of the edge: "))
        graph.add_edge(id, start, end, weight)
    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        map = color.welsh_powell(graph)
        graph.plot_graph(color_map=map)
    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        graph.plot_graph()
    elif choice == '5':
        loop = False
    else:
        input("Wrong option selection. Enter any key to try again..")
import os

from models.Graph import Graph
from algorithms import ColorAlghoritms
from algorithms.Floyd import Floyd
from algorithms.Dijkstra import Dijkstra

debug = False
graph = Graph(orientation=False)
color = ColorAlghoritms.Color()

def print_main_menu():
    print(25 * "-", "Graph atributes", 24 * "-")
    print("Debug: " + ("On" if debug else "Off"))
    print("Orientation: " + ("Oriented" if graph.orientation else "Non-Oriented"))
    print(30 * "-", "MENU", 30 * "-")
    print("1. Toggle Debug On/Off")
    print("2. Toggle Orientation/Non-Oriented")
    print("3. Add node")
    print("4. Add edge")
    print("5. Welsh Powell Apply")
    print("6. Floyd Apply")
    print("7. Dijkstra Apply")
    print("8. Plot graph")
    print("9. Exit")
    print(67 * "-")

loop = True

while loop:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_main_menu()
    choice = input("Enter your choice [1-9]: ")

    if choice == '1':
        debug = not debug

    elif choice == '2':
        graph.orientation = not graph.orientation

    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = input("Enter with the ID of the node: ")
        value = input("Enter with the value of the node: ")
        graph.add_node(id, value)

    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = input("Enter with the ID of the edge: ")
        start = input("Enter with the first node ID: ")
        end = input("Enter with the second node ID: ")
        weight = float(input("Enter with the weight of the edge: "))
        graph.add_edge(id, start, end, weight)

    elif choice == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        map = color.welsh_powell(graph)
        graph.plot_graph(color_map=map)

    elif choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        floyd = Floyd(graph, debug=debug)
        valid_keys = [key for node in graph.get_nodes() for key in node.get_key()]

        start = input("Enter the origin node ID: ")
        end = input("Enter the destiny node ID: ")

        while (start not in valid_keys) or (end not in valid_keys):
            print("Please input valid nodes ID")
            start = input("Enter the origin node ID: ")
            end = input("Enter the destiny node ID: ")

        minimum_distance = floyd.minimum_distance(start, end)
        print("Minimum distance betwen Node {} and Node {}: {}".format(start, end, minimum_distance))

        if minimum_distance != float("inf"):
            minimum_path = floyd.minimum_path(start, end)
            print("minimum path:" + str(minimum_path))
        input("Press any key to continue")

    elif choice == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        if any(edge.get_value() < 0 for node in graph.get_nodes() for edge in node.get_edges()):
            print("This graph has edge with negative value")
        else:
            valid_keys = [key for node in graph.get_nodes() for key in node.get_key()]

            start = input("Enter the origin node ID: ")
            end = input("Enter the destiny node ID: ")

            while (start not in valid_keys) or (end not in valid_keys):
                print("Please input valid nodes ID")
                start = input("Enter the origin node ID: ")
                end = input("Enter the destiny node ID: ")

            dijkstra = Dijkstra(graph, start, debug=debug)

            minimum_distance = dijkstra.minimum_distance(end)
            print("Minimum distance betwen Node {} and Node {}: {}".format(start, end, minimum_distance))

            if minimum_distance != float("inf"):
                minimum_path = dijkstra.minimum_path(end)
                print("minimum path:" + str(minimum_path))

        input("Press any key to continue")

    elif choice == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        graph.plot_graph()

    elif choice == '9':
        loop = False

    else:
        input("Wrong option selection. Enter any key to try again..")
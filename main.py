import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, simpledialog
from tkinter import font
import ast
from math import inf
from heapq import heappop, heappush
rt = Tk()
rt.title("AI searching algorithms")

# Create a Tkinter variable
tkvar = StringVar(rt)

# Dictionary with options
choices = sorted({'DFS', 'BFS', 'UCS', 'Greedy', 'A star'})
tkvar.set('DFS')  # set the default option

popupMenu = OptionMenu(rt, tkvar, *choices)
Label(rt, text="Choose a searching algorithm").grid(row=2, column=2)
popupMenu.grid(row=3, column=2)
Label(rt, text="Next step!").grid(row=4, column=2)
b2 = Button(rt, text='OK', command=rt.quit)
b2.grid(row=5, column=2)


# on change dropdown value
def change_dropdown(*args):
    global dropdown
    dropdown = str(tkvar.get())


# link function to change dropdown
tkvar.trace('w', change_dropdown)

rt.mainloop()

if dropdown == 'DFS':
    root = Tk()
    root.title('Input nodes')
    root.geometry("500x650")


    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        root.title(f'{name} - Textpad')


    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))


    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    open_button = Button(root, text="Open Text File", command=open_txt)
    open_button.pack(pady=20)

    save_button = Button(root, text="Save File", command=save_txt)
    save_button.pack(pady=20)

    root.mainloop()

    ROOT = Tk()

    ROOT.withdraw()
    source = simpledialog.askstring(title="Test",
                                    prompt="Enter the source:")

    G = nx.read_edgelist("DFS.txt", create_using=nx.DiGraph())
    plt.subplot(121)
    nx.draw_circular(G, with_labels=True, node_size=500, node_color='yellow')
    DFS = nx.depth_first_search.dfs_tree(G, source)
    plt.subplot(122)
    nx.draw_circular(DFS, with_labels=True, node_size=500, node_color='yellow')
    plt.show()

if dropdown == 'BFS':
    root = Tk()
    root.title('Input nodes')
    root.geometry("500x650")


    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        root.title(f'{name} - Textpad')


    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))


    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    open_button = Button(root, text="Open Text File", command=open_txt)
    open_button.pack(pady=20)

    save_button = Button(root, text="Save File", command=save_txt)
    save_button.pack(pady=20)

    root.mainloop()

    ROOT = Tk()
    ROOT.withdraw()
    source = simpledialog.askstring(title="Test",
                                    prompt="Enter the source:")

    G = nx.read_edgelist("BFS.txt", create_using=nx.DiGraph())
    plt.subplot(121)
    nx.draw_circular(G, with_labels=True, node_size=500, node_color='yellow')
    BFS = nx.breadth_first_search.bfs_tree(G, source)
    plt.subplot(122)
    nx.draw_circular(BFS, with_labels=True, node_size=500, node_color='yellow')
    plt.show()

if dropdown == 'UCS':
    root = Tk()
    root.title('Input nodes')
    root.geometry("500x650")


    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        root.title(f'{name} - Textpad')


    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))


    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    open_button = Button(root, text="Open Text File", command=open_txt)
    open_button.pack(pady=20)

    save_button = Button(root, text="Save File", command=save_txt)
    save_button.pack(pady=20)

    root.mainloop()

    ROOT = Tk()

    ROOT.withdraw()
    source = simpledialog.askstring(title="UCS",
                                    prompt="Enter the source:")
    target = simpledialog.askstring(title="UCS",
                                    prompt="Enter the target:")

    G = nx.read_edgelist('UCS.txt', data=[('Weight', int)])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='yellow')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=nx.get_edge_attributes(G, 'Weight'))
    RT = Tk()
    txt = Label(RT, text="UCS path is:")
    text = Label(RT, text=nx.shortest_path(G, source, target, weight='Weight'))
    txt.place(x=70, y=50)
    text.place(x=70, y=90)
    plt.show()

if dropdown == 'Greedy':
    root = Tk()
    root.title('Input nodes')
    root.geometry("500x650")


    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        root.title(f'{name} - Textpad')


    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))


    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    open_button = Button(root, text="Open Text File", command=open_txt)
    open_button.pack(pady=20)

    save_button = Button(root, text="Save File", command=save_txt)
    save_button.pack(pady=20)

    root.mainloop()

    ROOT = Tk()

    ROOT.withdraw()
    source = simpledialog.askstring(title="Greedy",
                                    prompt="Enter the source:")
    target = simpledialog.askstring(title="Greedy",
                                    prompt="Enter the target:")

    G = nx.read_edgelist('Greedy.txt', data=[('Weight', int), ('Heuristic', int)])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='yellow')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=nx.get_edge_attributes(G, 'Weight'))
    RT = Tk()
    txt = Label(RT, text="Greedy path is:")
    text = Label(RT, text=nx.shortest_path(G, source, target, weight='Heuristic'))
    txt.place(x=70, y=50)
    text.place(x=70, y=90)
    plt.show()

if dropdown == "A star":
    class Graph:
        def __init__(self, directed=True):
            self.edges = {}
            self.huristics = {}
            self.directed = directed

        def add_edge(self, node1, node2, cost=1, __reversed=False):
            try:
                neighbors = self.edges[node1]
            except KeyError:
                neighbors = {}
            neighbors[node2] = cost
            self.edges[node1] = neighbors
            if not self.directed and not __reversed: self.add_edge(node2, node1, cost, True)

        def set_huristics(self, huristics={}):
            self.huristics = huristics

        def neighbors(self, node):
            try:
                return self.edges[node]
            except KeyError:
                return []

        def cost(self, node1, node2):
            try:
                return self.edges[node1][node2]
            except:
                return inf

        def a_star_search(self, start, goal):
            found, fringe, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {
                start: None}, {start: 0}
            print('{:11s} | {}'.format('Expand Node', 'Fringe'))
            print('--------------------')
            print('{:11s} | {}'.format('-', str(fringe[0])))
            while not found and len(fringe):
                _, current = heappop(fringe)
                print('{:11s}'.format(current), end=' | ')
                if current == goal: found = True; break
                for node in self.neighbors(current):
                    new_cost = cost_so_far[current] + self.cost(current, node)
                    if node not in visited or cost_so_far[node] > new_cost:
                        visited.add(node);
                        came_from[node] = current;
                        cost_so_far[node] = new_cost
                        heappush(fringe, (new_cost + self.huristics[node], node))
                print(', '.join([str(n) for n in fringe]))
            if found:
                print();
                return came_from, cost_so_far[goal]
            else:
                print('No path from {} to {}'.format(start, goal));
                return None, inf

        path = []

        @staticmethod
        def print_path(self, came_from, goal):
            parent = came_from[goal]
            if parent:
                Graph.print_path(self, came_from, parent)
            else:
                self.path.append(goal)
            self.path.append("=>" + goal)

        def __str__(self):
            return str(self.edges)


    root = Tk()
    root.title('Input nodes')
    root.geometry("500x650")


    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        name = text_file
        name = name.replace("C:/gui/", "")
        name = name.replace(".txt", "")

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

        root.title(f'{name} - Textpad')


    def save_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))


    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
    my_text.pack()

    open_button = Button(root, text="Open Text File", command=open_txt)
    open_button.pack(pady=20)

    save_button = Button(root, text="Save File", command=save_txt)
    save_button.pack(pady=20)

    root.mainloop()

    graph = Graph(directed=True)
    s = nx.DiGraph()
    file = open("Astar heuristics.txt", "r")
    contents = file.read()
    graph.set_huristics(ast.literal_eval(contents))
    file.close()
    with open("Astar edges.txt") as f:
        line = f.readline()
        while line:
            stringlist = line.split()
            a = stringlist[0]
            b = stringlist[1]
            c = int(stringlist[2])
            graph.add_edge(a, b, c)
            s.add_edge(a, b, weight=c)
            line = f.readline()

    ROOT = Tk()

    ROOT.withdraw()
    source = simpledialog.askstring(title="Astar",
                                    prompt="Enter the source:")
    target = simpledialog.askstring(title="Astar",
                                    prompt="Enter the target:")
    pos = nx.spring_layout(s)
    nx.draw_networkx(s, pos, with_labels=True, node_size=1500, node_color="yellow")
    start, goal = source, target
    traced_path, cost = graph.a_star_search(start, goal)
    RT = Tk()
    RT.geometry("300x300")
    txt = Label(RT, text="Astar path is:")
    tx = Label(RT, text='Cost:')
    t = Label(RT, text=cost)
    graph.print_path(graph, traced_path, goal)
    stri = "Path is: "
    for i in Graph.path[1:]:
        stri = stri + i
    text = Label(RT, text=stri)
    text.place(x=70, y=90)
    txt.place(x=70, y=50)
    tx.place(x=70, y=130)
    t.place(x=120, y=130)
    plt.show()

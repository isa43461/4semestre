from graphviz import Digraph

g = Digraph('G', filename='hello')

g.edge('Hello', 'World')

g.view()
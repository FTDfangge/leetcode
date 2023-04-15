# -*- coding: utf-8 -*-
# @Time    : 2022-11-26 12:52 p.m.
# @Author  : qkzhong
# @FileName: adjacency2graph.py
# @Software: PyCharm
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def adjacency2graph(twoD_array: List[List[int]]):
    G = nx.Graph()
    Matrix = np.array(twoD_array)
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if twoD_array[i][j] >= 0:
                G.add_edge(i, j, weight=twoD_array[i][j])
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()

from mpl_toolkits.axes_grid.axislines import SubplotZero
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib import rc
import random
from sympy.solvers import solve
from sympy import *
from django.shortcuts import render
import io, base64, urllib


def plot_graph(a=-3, b=-5):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(True)
    uri0 = render_chart(plt)
    plt.text(-2.5, 2.25, "A", weight="bold")
    plt.plot(-1.9, 2, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
    uri1 = render_chart(plt)
    plt.text(-0.3, 2.7, "B", weight="bold")
    plt.plot(-0.25, 2.4, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
    uri2 = render_chart(plt)
    point1 = [-1.9, 2]
    point2 = [2.1, 2.8]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'red', linestyle="-")
    plt.plot(2.1, 2.8, marker="x", markersize=10, markeredgecolor="red", markerfacecolor="red")
    uri3 = render_chart(plt)
    plt.text(2.5, 2.8, "P", weight="bold", color="red")
    plt.plot(2.1, 2.8, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    uri4 = render_chart(plt)
    plt.plot(x_values, y_values, 'black', linestyle="-")
    plt.plot(2.1, 2.8, marker="x", markersize=5, markeredgecolor="black", markerfacecolor="black")
    point3 = [2.1, 2.8]
    point4 = [2.1, -2.8]
    x_values = [point3[0], point4[0]]
    y_values = [point3[1], point4[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="--")
    plt.text(2.5, -2.8, "P' = A + B", weight="bold", color="blue")
    plt.plot(2.1, -2.8, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    uri5 = render_chart(plt)
    plt.close()
    return {"graph0": uri0, "graph1": uri1, "graph2": uri2, "graph3": uri3, "graph4": uri4, "graph5": uri5}


def second_step_graph(a=-3, b=-5):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(False)
    plt.text(2.5, -2.8, "A", weight="bold", color="blue")
    plt.plot(2.1, -2.8, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    uri1 = render_chart(plt)
    plt.text(-2.8, 0.5, "B", weight="bold", color="blue")
    plt.plot(-2.3, 0, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    uri2 = render_chart(plt)
    point1 = [2.1, -2.8]
    point2 = [-2.3, 0]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'red', linestyle="-")
    plt.plot(0.6, -1.8, marker="x", markersize=10, markeredgecolor="red", markerfacecolor="red")
    uri3 = render_chart(plt)
    point3 = [0.6, -1.8]
    point4 = [0.6, 1.8]
    x_values = [point3[0], point4[0]]
    y_values = [point3[1], point4[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="--")
    plt.text(0.2, 2.5, "P' = A + B", weight="bold", color="blue")
    plt.plot(0.6, 1.85, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    uri4 = render_chart(plt)

    plt.close()
    return {"graph_second_1": uri1, "graph_second_2": uri2, "graph_second_3": uri3, "graph_second_4": uri4}


def render_chart(matplot):
    buff = io.BytesIO()
    matplot.savefig(buff, format="png", transparent=True)
    buff.seek(0)
    graph = base64.b64encode(buff.getvalue())
    buff.close()
    return graph.decode('utf-8')


def main(request):
    graphs = plot_graph()
    graphs.update(second_step_graph())
    return render(request, "pages/index.html", graphs)


def test(request):
    graphs = plot_graph()
    return render(request, "pages/home.html", graphs)

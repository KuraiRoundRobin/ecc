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
    ## Grid and ecc plot
    y, x = np.ogrid[-6:6:100j, -6:6:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(False)

    ## Basic plot
    uri0 = render_chart(plt)

    ## First point
    plt.text(-2.5, 2.25, "A", weight="bold", color="blue")
    plt.plot(-1.9, 2, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="From starting point A", xy=(-6, 4), fontsize=12, color="blue")
    uri1 = render_chart(plt)
    plot_text.remove()

    ## Second point
    plt.text(-0.3, 2.7, "B", weight="bold", color="blue")
    plt.plot(-0.25, 2.35, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="pick a point B", xy=(-5.5, 4), fontsize=12, color="blue")
    uri2 = render_chart(plt)
    plot_text.remove()

    ## Line between two points
    point1 = [-1.9, 2]
    point2 = [2.1, 2.8]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'red', linestyle="-")
    plt.plot(2.1, 2.8, marker="x", markersize=10, markeredgecolor="red", markerfacecolor="red")
    plot_text = plt.annotate(text="connect A and B with a line", xy=(-6, 4), fontsize=10, color="blue")
    plot_text2 = plt.annotate(text="the line cuts the curve on a point", xy=(2, 1.5), fontsize=10, color="blue")
    uri3 = render_chart(plt)
    plot_text.remove()
    plot_text2.remove()

    ## New point
    plt.text(2.5, 2.8, "P", weight="bold", color="red")
    plt.plot(2.1, 2.8, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plot_text = plt.annotate(text="we can call this point P", xy=(2, 1.5), fontsize=10, color="blue")
    uri4 = render_chart(plt)
    plot_text.remove()


    plt.plot(x_values, y_values, 'black', linestyle="-")
    plt.plot(2.1, 2.8, marker="x", markersize=5, markeredgecolor="black", markerfacecolor="black")
    point3 = [2.1, 2.8]
    point4 = [2.1, -2.8]
    x_values = [point3[0], point4[0]]
    y_values = [point3[1], point4[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="--")
    plt.text(2.5, -2.8, "P' = A + B", weight="bold", color="blue")
    plt.plot(2.1, -2.8, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="project the P point to the other axis", xy=(2.5, 2.2), fontsize=8, color="blue")
    plot_text2 = plt.annotate(text="to get the P' point", xy=(2.2, -2), fontsize=8, color="blue")
    uri5 = render_chart(plt)
    plot_text.remove()
    plot_text2.remove()

    ## Remove all annotations
    plt.close()
    return {"graph0": uri0, "graph1": uri1, "graph2": uri2, "graph3": uri3, "graph4": uri4, "graph5": uri5}


def second_step_graph(a=-3, b=-5):
    ## Basic plot
    y, x = np.ogrid[-6:6:100j, -6:6:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(False)

    ## First point
    plt.text(2.5, -2.8, "A", weight="bold", color="blue")
    plt.plot(2.1, -2.8, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="P' point becomes A point", xy=(2, -1.5), fontsize=10, color="blue")
    uri1 = render_chart(plt)
    plot_text.remove()

    ## Second point
    plt.text(-2.8, 0.5, "B", weight="bold", color="blue")
    plt.plot(-2.3, 0, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="Pick point B", xy=(-5, 1.5), fontsize=10, color="blue")
    uri2 = render_chart(plt)
    plot_text.remove()

    ## Connect points
    point1 = [2.1, -2.8]
    point2 = [-2.3, 0]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'red', linestyle="-")
    plt.plot(0.6, -1.8, marker="x", markersize=10, markeredgecolor="red", markerfacecolor="red")
    plt.text(0.7, -1.5, "P", weight="bold", color="blue")
    plot_text = plt.annotate(text="Connect A and B again", xy=(0.5, 0.5), fontsize=10, color="blue")
    plot_text2 = plt.annotate(text="And get another point P", xy=(1.5, -1.5), fontsize=10, color="blue")
    uri3 = render_chart(plt)
    plot_text.remove()
    plot_text2.remove()

    ## Project point
    point3 = [0.6, -1.8]
    point4 = [0.6, 1.8]
    x_values = [point3[0], point4[0]]
    y_values = [point3[1], point4[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="--")
    plt.text(0.2, 3, "P' = A + B", weight="bold", color="blue")
    plt.plot(0.6, 1.85, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
    plot_text = plt.annotate(text="Project P to get P'", xy=(1, 1), fontsize=10, color="blue")
    uri4 = render_chart(plt)
    plot_text.remove()

    plt.close()
    return {"graph_second_1": uri1, "graph_second_2": uri2, "graph_second_3": uri3, "graph_second_4": uri4}

def same_point_graph(a=-3, b=-5):
    ## Basic plot
    y, x = np.ogrid[-6:6:100j, -6:6:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(False)

    ## Pick P
    plt.text(-1, 3, "P", weight="bold", color="green")
    plt.plot(-0.8, 2.65, marker="o", markersize=10, markeredgecolor="green", markerfacecolor="green")
    plot_text = plt.annotate(text="From agreed point P", xy=(-5.5, 3.5), fontsize=12, color="green")
    uri1 = render_chart(plt)
    plot_text.remove()


    ## Tangent line
    point1 = [-0.8, 2.65]
    point2 = [2, 1.8]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="-")
    plt.plot(1.5, 2, marker="x", markersize=10, markeredgecolor="green", markerfacecolor="green")
    plot_text = plt.annotate(text="Pick 2 points infinitely close to P", xy=(-6, 3.5), fontsize=9, color="green")
    plot_text2 = plt.annotate(text="The line between these 2 points is the tangent at P", xy=(0.5, 0.5), fontsize=9, color="green")
    uri2 = render_chart(plt)
    plot_text.remove()
    plot_text2.remove()

    ## P' projection
    point3 = [1.5, 2]
    point4 = [1.5, -2]
    x_values = [point3[0], point4[0]]
    y_values = [point3[1], point4[1]]
    plt.plot(x_values, y_values, 'green', linestyle="--")
    plt.text(2, -2, "P' = P + P = 2P", weight="bold", color="green")
    plt.plot(1.5, -2, marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
    plot_text = plt.annotate(text="Follow the procedure to get P'", xy=(2, 1.3), fontsize=9, color="green")
    uri3 = render_chart(plt)
    plot_text.remove()

    plt.close()
    return {"graph_third_1": uri1, "graph_third_2": uri2, "graph_third_3": uri3}

def last_point_graph(a=-3, b=-5):
    y, x = np.ogrid[-6:6:100j, -6:6:100j]
    xlist = x.ravel()
    ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    plt.gca().spines[:].set_position('center')
    plt.grid(False)

    plt.text(-1, 3, "P", weight="bold", color="green")
    plt.plot(-0.8, 2.65, marker="o", markersize=10, markeredgecolor="green", markerfacecolor="green")

    plt.text(-2.5, 2.1, "NP", weight="bold", color="red")
    plt.plot(-1.98, 1.8, marker="o", markersize=5, markeredgecolor="purple", markerfacecolor="red")

    point1 = [-0.8, 2.65]
    point2 = [-1.98, 1.8]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'blue', linestyle="-.")

    uri1 = render_chart(plt)

    plt.close()
    return {"last_graph": uri1}

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
    graphs.update(same_point_graph())
    graphs.update(last_point_graph())
    return render(request, "pages/index.html", graphs)


def test(request):
    graphs = plot_graph()
    return render(request, "pages/home.html", graphs)

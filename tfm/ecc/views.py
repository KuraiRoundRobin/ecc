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
    randmid = random.randint(30, 70)
    plt.plot([-1.5, 5], [-1, 8], color="c", linewidth=1)  # plot([x1,x2,x3,...],[y1,y2,y3,...])
    plt.plot([xlist[randmid], 5], [ylist[randmid], 5], color="m", linewidth=1)
    plt.annotate('$O+G+T=OGT$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))

    plt.grid(True)
    uri1 = render_chart(plt)
    plt.annotate('$O+G+T=OGT2$', xy=(2, 1), xytext=(2, 5.5), arrowprops=dict(facecolor='red', shrink=0.05))
    uri2 = render_chart(plt)
    plt.annotate('$O+G+T=OGT3$', xy=(2, 1), xytext=(1, 2.5), arrowprops=dict(facecolor='blue', shrink=0.05))
    #to delete annotations in future iterations
    #ann = plt.annotate
    #ann.remove()
    uri3 = render_chart(plt)
    plt.close()
    return {"graph1": uri1, "graph2": uri2, "graph3": uri3}


def render_chart(matplot):
    buff = io.BytesIO()
    matplot.savefig(buff, format="png")
    buff.seek(0)
    graph = base64.b64encode(buff.getvalue())
    buff.close()
    return graph.decode('utf-8')


def main(request):
    graphs = plot_graph()
    return render(request, "pages/index.html", graphs)


def test(request):
    graphs = plot_graph()
    return render(request, "pages/home.html", graphs)

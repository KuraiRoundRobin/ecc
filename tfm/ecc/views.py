

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


def plotGraph(request):

    fig = plt.figure(1)
    #ax = SubplotZero(fig, 111)
    #fig.add_subplot(ax)
    #for direction in ["xzero", "yzero"]:
        #ax.axis[direction].set_axisline_style("-|>")
        #ax.axis[direction].set_visible(True)
    #ax.axis([-10,10,-10,10])
    a = -3; b = -5
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    xlist = x.ravel(); ylist = y.ravel()
    elliptic_curve = pow(y, 2) - pow(x, 3) - x * a + b
    plt.contour(xlist, ylist, elliptic_curve, [0])
    #rand = random.uniform(-5,5)
    randmid = random.randint(30,70)
    #y = ylist[randmid]; x = xlist[randmid]
    xsym, ysym = symbols('x ylist[randmid]')
    x_result = solve(pow(ysym, 2) - pow(xsym, 3) - xsym * a - b, xsym) # 11/5/13 needs to return a value
    plt.plot([-1.5,5], [-1,8], color = "c", linewidth=1) # plot([x1,x2,x3,...],[y1,y2,y3,...])
    plt.plot([xlist[randmid],5], [ylist[randmid],5], color = "m", linewidth=1)
    #rc('text', usetex=True)
    #text(-9,6, 'ojete')
    #text(-9,6,' size of xlist: %s \n size of ylist: %s \n x_coord: %s \n random_y: %s'
     #   %(len(xlist),len(ylist),x_result,ylist[randmid]),
      #  fontsize=10, color = 'blue',bbox=dict(facecolor='tan', alpha=0.5))
    #plt.annotate('$P+Q=R$', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('$O+G+T=OGT$', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))

##    verts = [(-5, -10),(5, 10)] # [(x,y)startpoint,(x,y)endpoint] #,(0, 0)]
##    codes = [Path.MOVETO,Path.LINETO] # related to verts[] #,Path.STOP]
##    path = Path(verts, codes)
##    patch = patches.PathPatch(path, facecolor='none', lw=2)
##    ax.add_patch(patch)

    plt.grid(True)
    buff = io.BytesIO()
    plt.savefig(buff, format="png")
    buff.seek(0)
    graph1 = base64.b64encode(buff.read())
    uri1 = urllib.parse.quote(graph1)
    plt.annotate('$O+G+T=OGT2$', xy=(2, 1), xytext=(2, 5.5), arrowprops=dict(facecolor='red', shrink=0.05))
    buff = io.BytesIO()
    plt.savefig(buff, format="png")
    buff.seek(0)
    graph2 = base64.b64encode(buff.read())
    uri2 = urllib.parse.quote(graph2)

    return render(request, "pages/home.html", {"graph1": uri1, "graph2": uri2})


def main(request):
    return render(request, "pages/index.html")

if __name__ == '__main__':
    main()

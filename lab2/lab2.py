from cvxopt.solvers import qp
from cvxopt.base import matrix
#from cvxopt import trans

import numpy, pylab, random, math

classA = []
classB = []
xs = []
C = 10

def genData():
	global classA, classB, xs
	classA = [(random.normalvariate(-1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(10)] + [(random.normalvariate(1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(10)]
	classB = [(random.normalvariate(0, 0.5), random.normalvariate(-.5, .5),
		   -1.0)
		  for i in range(20)]
	xs = classA + classB
	random.shuffle(xs)


genData()
eps = 0.00001


def kernel(x,y):
	return radialK(x,y,.5)

def linearK(x, y):
	s = 1;
	for i in range(2):
		s+= (x[i] * y[i])
	return s

def polyK(x,y,p):
    return pow(linearK(x,y),p)

def radialK(x,y,sigma):
    diff = range(2)
    for i in range(2):
        diff[i] = x[i] - y[i]
    val = 0
    for i in range(2):
        val += diff[i] * diff[i]
    return math.exp(-(val) / (2 * sigma * sigma))

def sigmoidK(x,y,k,delta):
    val = 0;
    for i in range(2):
        val += x[i]*y[i]
    val *= k
    val - delta
    return val



def buildP(xs,ker):
	P = range(len(xs))
	for i in range(len(xs)):
		P[i] = range(len(xs))
		for j in range(len(xs)):
			P[i][j] = xs[i][2]*xs[j][2]*ker(xs[i], xs[j])
	return P

def buildq(xs):
	q = range(len(xs))
	for i in range(len(xs)):
		q[i] = -1.0
	return q

def buildh(xs):
	h = range(2*len(xs))
	for i in range(len(xs)):
		h[i] = 0.0
	for i in range(len(xs)):
		h[len(xs)+i] = C
	return h

def buildG(xs):
	G = range(2*len(xs))
	for i in range(len(xs)):
		G[i] = range(len(xs))
		for j in range(len(xs)):
			if i == j:
				G[i][j] = -1.0
			else:
				G[i][j] = 0.0
	for i in range(len(xs)):
		G[len(xs)+i] = range(len(xs))
		for j in range(len(xs)):
			if i == j:
				G[len(xs)+i][j] = 1.0
			else:
				G[len(xs)+i][j] = 0.0
	return G

def callQP(P, q, G, h):
	r = qp(matrix(P), matrix(q,(len(q),1)), matrix(G).T, matrix(h,(len(h),1)))
	alpha = list(r['x'])
	return alpha

def extractSupportVectors(xs, alphas):
	result = []
	for i in range(len(xs)):
		if abs(alphas[i]) > eps:
			result.append((alphas[i], xs[i]))
	return result

def indicate(x, supportVecs,ker):
	val = 0
	for i in range(len(supportVecs)):
		a,y = supportVecs[i]
		val += a * y[2] * ker(x,y)
	return val

def classify(x, supportVecs,ker):
	val = indicate(x, supportVecs,ker)
	if val > 0:
		return 1.0
	else:
		return -1.0
	
			
def plotBoundary(supportVecs, ker):
	x_range = numpy.arange(-4, 4, 0.01)
	y_range = numpy.arange(-4, 4, 0.01)
	
	grid = matrix([[indicate((x,y), supportVecs, ker)
			for y in y_range]
		       for x in x_range])
	
	pylab.contour(x_range, y_range, grid,
		      (-1.0, 0.0, 1.0),
		      colors = ('red', 'black', 'green'),
		      linewidths=(1, 3, 1))		      


def plotData(supportVecs, ker):
    pylab.hold(True)
	# todo: split up in support vecs and non sup vecs
    pylab.plot([p[0] for p in classA],
               [p[1] for p in classA],
               'bo')
    pylab.plot([p[0] for p in classB],
               [p[1] for p in classB],
               'ro')
    pylab.plot([p[0] for (a,p) in supportVecs],
               [p[1] for (a,p) in supportVecs],
               'kx')
    plotBoundary(supportVecs, ker)
    pylab.show()



def run(ker):
	P = buildP(xs, ker)
	q = buildq(xs)
	h = buildh(xs)
	G = buildG(xs)

	alphas = callQP(P, q, G, h)

	supportVecs = extractSupportVectors(xs, alphas)

	plotData(supportVecs, ker)
				

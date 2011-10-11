import monkdata as m
import dtree
from itertools import izip, count
import random
from pylab import *

def gainTable(dataset):
	"Returns the information gain for all attributes as a list"
	return [dtree.averageGain(dataset, m.attributes[i]) for i in range(6)]
		

def splitDataset(dataset, attributeNumber):
	"Function to split an entire dataset on attributes"
	return [dtree.select (dataset, m.attributes[attributeNumber], x) for x in m.attributes[attributeNumber].values]
	

def calculate1stLevelGain(dataset, attributeNumber):
	"Calculates the information gain at the 1st level of the decision tree"
	return [gainTable(x) for x in splitDataset(dataset, attributeNumber)]

def calculate1stLevelEntropy(dataset, attributeNumber):
	"blah blah blah"
	[entropy(x) for x in splitDataset(dataset, attributeNumber)]
	
def pickNextAttribute(dataset):	
	return reduce(largestAttributeGain, zip(gainTable(dataset), range(6)))[1]

def largestAttributeGain(x, y):
	xg, xi = x
	yg, yi = y
	if(xg < yg):
		return y
	else:
		return x
	
def mostCommonAfterSplit(dataset, attributeNumber):
	return [dtree.mostCommon(x) for x in splitDataset(dataset, attributeNumber)]
	
def expandOneLevel(dataset):
	return splitDataset(dataset, pickNextAttribute(dataset))
	
def secondLevelExpansion(dataset):
	return [map(dtree.mostCommon, expandOneLevel(x)) for x in expandOneLevel(dataset)]

def findBestPrune(tree, validationSet):
#    print("tree")
#    print(tree)
    current=tree
    while True:
        currentPerformance=dtree.check(current, validationSet)	
        pruned=dtree.allPruned(current)	
        if pruned == ():
            break
#        print("current")
#        print(current)
#        print("pruned trees")
#        print(len(pruned))
        performances=map(lambda t : dtree.check(t, validationSet), pruned)
        best, i=max(izip(performances,count())) 
        # ask which trees we should pick when performance is equal? min depth, min average depth, min no of nodes, order in allPruned
        if best < currentPerformance:
            break
        current = pruned[i]
    return current		 
		
def partition(data, fraction):
	ldata = list(data)
	random.shuffle(ldata)
	breakpoint = int(len(ldata) * fraction)
	return ldata[:breakpoint], ldata[breakpoint:]

def generateErrorTable(dataset, testset, fractions, tries):
    result=[]	
    for x in fractions:
        acc = 0
        for i in range(tries):
            trainSet, valSet =partition(dataset, x)

            tree = dtree.buildTree(trainSet, m.attributes)
            prunedTree = findBestPrune(tree, valSet)
            acc += dtree.check(prunedTree, testset)
        result.append( (x,acc / tries) )
    return result

def plotPruning():
    fractions = [.3,.4,.5,.6,.7,.8]
    monk1 = [.766,.788,.799,.797,.802,.780]
    monk3 = [.920,.939,.951,.966,.963,.967]
    plot(fractions, monk1, 'bo', markerfacecolor='green')
    grid(True)
    show()




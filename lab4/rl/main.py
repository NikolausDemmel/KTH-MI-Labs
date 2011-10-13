import animate as a

import random
import numpy
import pylab

trans = ((1,3,4,12),
         (0,2,5,13),
         (3,1,6,14),
         (2,0,7,15),
         (5,7,0,8),
         (4,6,1,9),
         (7,5,2,10),
         (6,4,3,11),
         (9,11,12,4),
         (8,10,13,5),
         (11,9,14,6),
         (10,8,15,7),
         (13,15,8,0),
         (12,14,9,1),
         (15,13,10,2),
         (14,12,11,3))

gamma = 0.9

rew = ((0,-1,0,-1),
       (0,0,-1,-1),
       (0,0,-1,-1),
       (0,-1,0,-1),
       (-1,-1,0,0),
       (0,0,0,0), # both legs up
       (0,0,0,0), # both legs up
       (-1,1,0,0), 
       (-1,-1,0,0),
       (0,0,0,0), # both legs up
       (0,0,0,0), # both legs up
       (-1,1,0,0), 
       (0,-1,0,-1),
       (0,0,-1,1),
       (0,0,-1,1),
       (0,-1,0,-1),)

policy = [None for s in trans]
value = [0 for s in trans]

class Environment: 
    def __init__(self, state = 0):
        self.state= state
        self.trans = ((1,3,4,12),
                      (0,2,5,13),
                      (3,1,6,14),
                      (2,0,7,15),
                      (5,7,0,8),
                      (4,6,1,9),
                      (7,5,2,10),
                      (6,4,3,11),
                      (9,11,12,4),
                      (8,10,13,5),
                      (11,9,14,6),
                      (10,8,15,7),
                      (13,15,8,0),
                      (12,14,9,1),
                      (15,13,10,2),
                      (14,12,11,3))


        self.rew = ((0,-1,0,-1),
                    (0,0,-1,-1),
                    (0,0,-1,-1),
                    (0,-1,0,-1),
                    (-1,-1,0,0),
                    (0,0,0,0), # both legs up
                    (0,0,0,0), # both legs up
                    (-1,1,0,0), 
                    (-1,-1,0,0),
                    (0,0,0,0), # both legs up
                    (0,0,0,0), # both legs up
                    (-1,1,0,0), 
                    (0,-1,0,-1),
                    (0,0,-1,1),
                    (0,0,-1,1),
                    (0,-1,0,-1),)

 

    def go(self, a): 
        r = self.rew[self.state][a]
        self.state = self.trans[self.state][a]
        return self.state, r

def qlearn(env, steps, epsilon, eta, gamma):
    s = 0
    q = [ [0,0,0,0] for x in range(16)]
    for x in range(steps):
        r = random.random()
        if r < epsilon:
            a = random.randint(0, 3)
        else :
            a = argmax(
                lambda a:
                    q[s][a],
                range(4))
        (newS, r) = env.go(a)
        q[s][a] = q[s][a] + eta * (r + gamma * max([ q[newS][a_] for a_ in range(4)]) - q[s][a])
        s = newS
    return q

def qMove(state, steps, q): 
    result = [state]
    for x in range(steps): 
        a = argmax(
            lambda a:
                q[state][a],
            range(4))
        state = trans[state][a]
        result.append(state)
    return result
        

def argmax(f, args):
    mi = None
    m = -1e10
    for i in args:
        v = f(i)
        if v > m:
            m = v
            mi = i
    return mi

def pol_iter(iterations):
    global policy, value, rew, gamma, trans
    for p in range(iterations):
        for s in range(len(policy)):
            policy[s] = argmax(
                lambda a:
                    rew[s][a] + gamma * value[trans[s][a]],
                range(4))

        for s in range(len(value)):
            a = policy[s]
            value[s] = rew[s][a] + gamma * value[trans[s][a]]


def move(state, steps):
    ret = [state]
    for s in range(steps):
        state = trans[state][policy[state]]
        ret.append(state)
    return ret


pol_iter(100)

result = move(0, 20)

#a.draw(result)




images = (pylab.imread('step1.png'),
          pylab.imread('step2.png'),
          pylab.imread('step3.png'),
          pylab.imread('step4.png'),
          pylab.imread('step5.png'),
          pylab.imread('step6.png'),
          pylab.imread('step7.png'),
          pylab.imread('step8.png'),
          pylab.imread('step9.png'),
          pylab.imread('step10.png'),
          pylab.imread('step11.png'),
          pylab.imread('step12.png'),
          pylab.imread('step13.png'),
          pylab.imread('step14.png'),
          pylab.imread('step15.png'),
          pylab.imread('step16.png'))

#comic = numpy.concatenate([images[i] for i in result], axis=1)

#pylab.imshow(comic)
#pylab.show()
env = Environment()
epsilon = 0.01
eta = 0.1
gamma = 0.9
q = qlearn(env, 200000, epsilon, eta, gamma)
print(q)
moves= qMove(0, 20, q)
print(moves)
a.draw(moves)
comic = numpy.concatenate([images[i] for i in moves], axis=1)

pylab.imshow(comic)
pylab.show()

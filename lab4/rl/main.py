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

print(move(0, 20))

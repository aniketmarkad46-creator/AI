import math

def alphabeta(d, i, maxp, v, a, b):
    if d == 3:
        return v[i]
    
    if maxp:
        best = -math.inf
        for j in range(2):
            best = max( best, alphabeta(d+1, i*2+j, False, v, a, b))
            a = max(a, best)
            if b <= a:
                break
        
        else: 
            best = math.inf
            for j in range(2):
                best = min( best, alphabeta(d+1, i*2+j, True,  v, a, b))
                b = min(b, best)
                if b <= a:
                    break
        return best
            
v = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal Value:", alphabeta(0, 0, True, v, -math.inf, math.inf))
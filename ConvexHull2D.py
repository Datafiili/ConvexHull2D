## -------------------- Convex Hull 2D -------------------- ##
#Written By: Aarni Junkkala

import math

def ConvexHull2D(vectors):
    if len(vectors) <= 2:
        return vectors
    #Finds the vector that is most left
    Leftest = 0
    for i in range(1,len(vectors)):
        if vectors[i][0] < vectors[Leftest][0]:
            Leftest = i
    
    Points = [vectors[Leftest]]
    AngleHolder = 0

    while True:
        SmallestAngle = 360 #Defaults to impossible
        SmallestIndex = -1 # -||-
        for i in range(len(vectors)): #Checks all angles compared to latest one
            if vectors[i] != Points[-1]:
                #Calculates the angle
                Angle = math.atan2(vectors[i][0] - Points[-1][0], vectors[i][1] - Points[-1][1])
                if Angle < 0: #If angle goes below zero, it must be rotated around
                    Angle += 360
                if Angle < SmallestAngle: #remembers one thatis smallest
                    SmallestAngle = Angle
                    SmallestIndex = i
        if vectors[SmallestIndex] in Points: #If tries to return back, then we are done
            break
        Points.append(vectors[SmallestIndex])
        AngleHolder += SmallestAngle
    return Points
#     for i in range(len(vectors)):
#         start = vectors[i]
#         print("\nPoints from ", vectors[i])
#         for j in range(len(vectors)):
#             if i != j:
#                 #if i != korkein:
#                 end = vectors[j]                
#                 print("Angle: " , AngleOfPoints(start,vectors[j]), vectors[j])
    
    
if __name__ == "__main__":
    print("##--------------------##")
    print(ConvexHull2D([[1.2,1.5],[2,0],[0,0],[-2,-2.2],[-3,1],[-1,-4]]))
    print(ConvexHull2D([[0,0],[1,0],[0,1]]))
    print(ConvexHull2D([[1,0],[1,1],[0,0],[-1,0],[-1,-1]]))
    
    import time
    s = time.time()
    
    import random
    for i in range(1000):
        L = []
        for i in range(16):
            L.append([random.random() * 20 - 10,random.random() * 20 - 10])
            ConvexHull2D(L)
    e = time.time()
    print("Time",e-s)
    
    print("##--------------------##")
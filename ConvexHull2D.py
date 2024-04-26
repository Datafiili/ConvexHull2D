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
        SmallestAngle = math.pi * 2 #Defaults to impossible
        SmallestIndex = -1 # -||-
        #print("Angle holder:", AngleHolder)
        #print("Starting point:",Points[-1])
        for i in range(len(vectors)): #Checks all angles compared to latest one
            if vectors[i] != Points[-1]:
                #Calculates the angle
                Angle = math.atan2(vectors[i][0] - Points[-1][0], vectors[i][1] - Points[-1][1])
                Angle -= AngleHolder
                if Angle < 0:
                    Angle += math.pi * 2
                #print(vectors[i], Angle)
                if Angle < SmallestAngle: #remembers one thatis smallest
                    SmallestAngle = Angle
                    SmallestIndex = i
        if vectors[SmallestIndex] in Points: #If tries to return back, then we are done
            break
        Points.append(vectors[SmallestIndex])
        #print("Connected to",vectors[SmallestIndex])
        AngleHolder += SmallestAngle
    return Points

def ConvexHullV2(vectors):
    if len(vectors) <= 2:
        return vectors
    
    corners = [vectors[0],vectors[0],vectors[0],vectors[0]] # Most left, top, right and bottom vectors
    for i in range(1,len(vectors)):
        if vectors[i][0] < corners[0][0]: #Left
            corners[0] = vectors[i]
        if vectors[i][1] > corners[1][1]: #Top
            corners[1] = vectors[i]
        if vectors[i][0] > corners[2][0]: #Right
            corners[2] = vectors[i]
        if vectors[i][1] < corners[3][1]: #Bottom
            corners[3] = vectors[i]
    print("Corners:",corners)
    
    Packs = [[corners[1]],[[corners[2]]],[[corners[3]]],[[corners[0]]]] #Packs of vertexes that are possibly on the hull. Seperated based on the 4 corners.
    
    for i in range(len(vectors)):
        if vectors[i] not in corners:
            #Top left pack
            if vectors[i][0] < corners[1][0] and vectors[i][1] > corners[0][1]:
                if math.atan2(vectors[i][0] - corners[0][0],vectors[i][1] - corners[0][1]) > math.atan2(corners[1][0] - corners[0][0],corners[1][1] - corners[0][1]): 
                    Packs[0].append(vectors[i])
            #Top right
            if vectors[i][0] > corners[1][0] and vectors[i][1] > corners[2][1]:
                if math.atan2(vectors[i][0] - corners[1][0],vectors[i][1] - corners[1][1]) < math.atan2(corners[2][0] - corners[1][0], corners[2][1] - corners[1][1]):
                    Packs[1].append(vectors[i])
            #Bottom right
            if vectors[i][0] > corners[3][0] and vectors[i][1] < corners[2][1]:
                if math.atan2(vectors[i][0] - corners[2][0], vectors[i][1] - corners[2][1]) > math.atan2(corners[3][0] - corners[2][0], corners[3][1] - corners[2][1]):
                    Packs[2].append(vectors[i])
            #Bottom left
            if vectors[i][0] < corners[3][0] and vectors[i][1] < corners[0][1]:
                if math.atan2(vectors[i][0] - corners[3][0],vectors[i][1] - corners[3][1]) < math.atan2(corners[0][0] - corners[3][0], corners[0][1] - corners[3][1]):
                    Packs[3].append(vectors[i])
    for i in range(4):
        print("Pack",i+1,Packs[i])
    #print("Angle to ", vectors[i] , ": " , math.atan2(corners[0][0] - corners[3][0], corners[0][1] - corners[3][1]))

    #Filter packs based on angle. If angle is greater than from corner to next, then it isn't in the area.
    points = [corners[0]]
               


if __name__ == "__main__":
    print("##--------------------##")
    #print(ConvexHull2D([[1.2,1.5],[2,0],[0,0],[-2,-2.2],[-3,1],[-1,-4]]))
    print(ConvexHull2D([[5,1],[-5,-1],[1,5],[-1,-5],[1,1],[2,2],[3,3],[-1,1],[-2,2],[-3,3],[1,-1],[2,-2],[3,-3],[-1,-1],[-2,-2],[-3,-3],[0,0]]))
    print(ConvexHullV2([[5,1],[-5,-1],[1,5],[-1,-5],[1,1],[2,2],[3,3],[-1,1],[-2,2],[-3,3],[1,-1],[2,-2],[3,-3],[-1,-1],[-2,-2],[-3,-3],[0,0]]))

#     import random
#     import time
#     tik = time.time()
#     for i in range(2000):
#         L = []
#         for i in range(1000):
#             L.append([random.uniform(-5.0,5.0),random.uniform(-5.0,5.0)])
#         ConvexHull2D(L)
#     print(time.time() - tik)
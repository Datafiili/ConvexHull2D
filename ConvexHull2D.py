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
    #print("Corners:",corners)
    
    Packs = [[corners[1]],[corners[2]],[corners[3]],[corners[0]]] #Packs of vertexes that are possibly on the hull. Seperated based on the 4 corners.
    print("## ----- Calculate Corners ----- ##")
    CornerAngles = [] #Angle from corner to a nother
    for i in range(len(corners)):
        Angle = math.atan2(corners[(i + 1) % len(corners)][0] - corners[i][0],corners[(i + 1) % len(corners)][1] - corners[i][1])
        if Angle < 0:
            Angle += math.pi * 2
        CornerAngles.append(Angle)

    for i in range(len(vectors)):
        if vectors[i] not in corners:
            print("Vectors[i]",vectors[i])
            #Top left pack
            if vectors[i][0] < corners[1][0] and vectors[i][1] > corners[0][1]:
                if math.atan2(vectors[i][0] - corners[0][0],vectors[i][1] - corners[0][1]) < CornerAngles[0]: 
                    print("Added to top left")
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
    print("## ----- Packs ----- ##")
    #print("Angle to ", vectors[i] , ": " , math.atan2(corners[0][0] - corners[3][0], corners[0][1] - corners[3][1]))

    #Filter packs based on angle. If angle is greater than from corner to next, then it isn't in the area.
    points = [corners[0]]
    Index = 0
    Repeats = 0
    while True:
        Repeats += 1
        if Repeats > 20:
            print("Failed")
            break
        SmallestAngle = math.pi * 2 #Defaults to impossible
        SmallestIndex = -1 
        print("##-----##")
        print("From:", points[-1])
        for i in range(len(Packs[Index])):
            Angle = math.atan2(Packs[Index][i][0] - points[-1][0],Packs[Index][i][1] - points[-1][1])
            print("To",Packs[Index][i], Angle)
            if Index > 1:
                Angle = abs(Angle) + math.pi
            if Angle < SmallestAngle:
                SmallestAngle = Angle
                SmallestIndex = i
        points.append(Packs[Index][SmallestIndex])
        if Packs[Index][SmallestIndex] == corners[(Index + 1) % 4]: #If we meet one of the corners -> Aim for next one.
            Index += 1
        if Packs[Index][SmallestIndex] == points[0]: #If we are back at start
            break
    return points

if __name__ == "__main__":
    print("##--------------------##")
    #print(ConvexHull2D([[1.2,1.5],[2,0],[0,0],[-2,-2.2],[-3,1],[-1,-4]]))
    #print(ConvexHull2D([[5,1],[-5,-1],[1,5],[-1,-5],[1,1],[2,2],[3,3],[-1,1],[-2,2],[-3,3],[1,-1],[2,-2],[3,-3],[-1,-1],[-2,-2],[-3,-3],[0,0]]))
    #print(ConvexHullV2([[5,1],[-5,-1],[1,5],[-1,-5],[1,1],[2,2],[3,3],[-1,1],[-2,2],[-3,3],[1,-1],[2,-2],[3,-3],[-1,-1],[-2,-2],[-3,-3],[0,0]]))
    print(ConvexHullV2([[0,3],[3,0],[0,-3],[-3,0],[2,2],[-2,2],[2,-2],[-2,-2],[0,0],[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[0,1],[-1,0],[0,-1]]))

#     import random
#     import time
#     tik = time.time()
#     for i in range(2000):
#         L = []
#         for i in range(1000):
#             L.append([random.uniform(-5.0,5.0),random.uniform(-5.0,5.0)])
#         ConvexHull2D(L)
#     print(time.time() - tik)
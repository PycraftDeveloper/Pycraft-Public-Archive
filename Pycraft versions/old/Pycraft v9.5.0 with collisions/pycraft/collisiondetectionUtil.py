import time

with open(r"D:\Pycraft - Copy with collisions v0.9.5\Resources\G3_Resources\map\vertex.txt", "r") as file:
    readData = file.read()
    
string = readData
arr = string.split(",")

arrayX = []
arrayY = []
arrayZ = []

for i in range(0, len(arr), 3):
    arrayX.append(float(arr[i]))
    arrayY.append(float(arr[i+1]))
    arrayZ.append(float(arr[i+2]))

def GC(camera_pos):
    try:
        camera_pos = (camera_pos[0], camera_pos[1], camera_pos[2]) # 6574 fix this to represent in game tile on floor, also this needs a lot of optim and restr
    except:
        camera_pos = (0,0,0)
    id = []

    for i in range(len(arrayX)):
        try:
            if arrayX[i] < camera_pos[0] and arrayX[i+1] > camera_pos[0]:
                id.append(i)
        except:
            pass
        
    for i in range(len(arrayZ)):
        try:
            if arrayZ[i] < camera_pos[2] and arrayZ[i+1] > camera_pos[2]:
                id.append(i)
        except:
            pass
        
    num = 0
    countr = 0
        
    for i in range(len(id)):
        for j in range(len(id)):
            if id[i] == id[j]:
                num += arrayY[id[i]]
                countr += 1

    try:
        return num/countr
    except:
        return -80
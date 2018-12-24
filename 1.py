import cv2
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

ImSize = [600, 338]
PreImNum = 10000
fileIdLen = 6
ImExpName = '.jpg'
AnotExpName = '.xml'
ImIdSet = range(1, PreImNum + 1)

# data file
MainFolder = '/home/ex/桌面/dataset/12_6_data/images_all'
ImFolder = os.path.join(MainFolder, 'JPEGImages')
AnotFolder = os.path.join(MainFolder, 'Annotations')


##get object annotation bndbox loc start
def GetAnnotBoxLoc(AnotPath):
    # open xml
    tree = ET.ElementTree(file=AnotPath)
    root = tree.getroot()
    ObjectSet = root.findall('object')
    ObjBndBoxSet = {}
    for Object in ObjectSet:
        ObjName = Object.find('name').text
        BndBox = Object.find('bndbox')
        x1 = int(BndBox.find('xmin').text) - 1
        y1 = int(BndBox.find('ymin').text) - 1
        x2 = int(BndBox.find('xmax').text) - 1
        y2 = int(BndBox.find('ymax').text) - 1
        BndBoxLoc = [x1, y1, x2, y2]
        if ObjBndBoxSet.has_key(ObjName):
            ObjBndBoxSet[ObjName].append(BndBoxLoc)
        else:
            ObjBndBoxSet[ObjName] = [BndBoxLoc]  # why not ues dict(key=val)?
    return ObjBndBoxSet


##get object annotation bndbox loc end

##draw all bndbox on image
def DrawObjectBox(Im, ObjBndBoxSet, BoxColor):
    for ObjName, BndBoxSet in ObjBndBoxSet.iteritems():
        for BndBox in BndBoxSet:
            cv2.rectangle(Im, (BndBox[0], BndBox[1]), (BndBox[2], BndBox[3]), BoxColor, 2)
            dsptxt = '{:s}'.format(ObjName)
            cv2.putText(Im, dsptxt, (max([(BndBox[0] + BndBox[2]) / 2 - 10, 0]), max([BndBox[3] - 3, 0])),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


for ImId in ImIdSet:
    ImIdStr = str(ImId).zfill(fileIdLen)
    ImName = ImIdStr + ImExpName
    ImPath = os.path.join(ImFolder, ImName)
    Im = cv2.imread(ImPath, 1)
    # print ImName
    AnotName = ImIdStr + AnotExpName
    AnotPath = os.path.join(AnotFolder, AnotName)
    ObjBndBoxSet = GetAnnotBoxLoc(AnotPath)
    print
    str(ObjBndBoxSet)
    DrawObjectBox(Im, ObjBndBoxSet, (255, 0, 0))
    cv2.imshow('OriginIm', Im)

    cv2.waitKey(2000)
    cv2.destroyAllWindows()

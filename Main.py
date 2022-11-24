from sysModule import *  # not installable on windows but intern to systema

import math

import csv

card_database = []
card_database += [["Card1", 0.2]]

######### fonctions de bases utiles pour la programmation #########

# ------------------------------------------------------------------------
# @methodname findObject(ModelObject originObject, string name)
# @methodbrief Find the first object called "name" in the descendency of "originObject"
# ------------------------------------------------------------------------
def findObject(originObject, name):
    for element in getSubTree(originObject):
        if (element.getType() == "object" and element.getName() == name):
            return ModelObject(element)


# ------------------------------------------------------------------------
# @methodname findShape(ModelObject originObject, string name)
# @methodbrief Find the first shape called "name" in the descendency of "originObject"
# ------------------------------------------------------------------------
def findShape(originObject, name):
    for element in getSubTree(originObject):
        if (element.getType() == "shape" and element.getName() == name):
            return ModelShape(element)


# ------------------------------------------------------------------------
# @methodname findObjectList(ModelObject originObject, string name)
# @methodbrief Find all the objects called "name" in the descendency of "originObject"
# ------------------------------------------------------------------------
def findObjectList(originObject, name):
    found = []

    for element in getSubTree(originObject):
        if (element.getType() == "object" and element.getName() == name):
            found.append(ModelObject(element))

    return found


# ------------------------------------------------------------------------
# @methodname findShapeList(ModelObject originObject, string name)
# @methodbrief Find all the shapes called "name" in the descendency of "originObject"
# ------------------------------------------------------------------------
def findShapeList(originObject, name):
    found = []

    for element in getSubTree(originObject):
        if (element.getType() == "shape" and element.getName() == name):
            found.append(ModelShape(element))

    return found


# ------------------------------------------------------------------------
# @methodname getSubTree(ModelElement element)
# @methodbrief Returns the sub-tree of a Systema element
# @methodbrief If the element is an object, getSubTree() returns a list with all its descendency
# @methodbrief If the element is a shape, getSubTree returns a list constituted with only this shape
# ------------------------------------------------------------------------
def getSubTree(element):
    descendants = []  # this is the list of the elements of the sub-tree we will fill
    descendants.append(element)  # the current element is part of the sub-tree

    if (element.getType() == "object"):
        # if the current element is an object
        children = ModelObject(element).getChildren()  # we retrieve all its children

        for e in children:  # we append all the children's subtrees to the list
            descendants = descendants + getSubTree(
                e)  # we call the function recursively to retrieve all children's sub-trees

    return descendants


# ------------------------------------------------------------------------
# @methodname getPath(ModelElement element)
# @methodbrief Return the path of an element in its Systema model structure
# ------------------------------------------------------------------------
def getPath(element):
    if (element.getName() == element.getModelFile().getRoot().getName()):
        return ""
    else:
        return getPath(element.getFather()) + "/" + element.getName()

####################################################################################################

 # Programming part
model = getCurrentModelFile() #we retrieve the model used for the exercise

Boards = findObject(model.getRoot(), "Boards") #we find the object called "SatBody" in the model
Boards = getSubTree(Boards)
for board in Boards:
    if board.getType() == "shape":
        print(board)
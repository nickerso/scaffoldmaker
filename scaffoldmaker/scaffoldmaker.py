"""
Class for listing and accessing all mesh type scripts supported by scaffoldmaker.
"""

from meshtypes.meshtype_2d_plate1 import MeshType_2d_plate1
from meshtypes.meshtype_2d_platehole1 import MeshType_2d_platehole1
from meshtypes.meshtype_2d_sphere1 import MeshType_2d_sphere1
from meshtypes.meshtype_2d_tube1 import MeshType_2d_tube1
from meshtypes.meshtype_3d_box1 import MeshType_3d_box1
from meshtypes.meshtype_3d_boxhole1 import MeshType_3d_boxhole1
from meshtypes.meshtype_3d_heartatria1 import MeshType_3d_heartatria1
from meshtypes.meshtype_3d_heartventricles1 import MeshType_3d_heartventricles1
from meshtypes.meshtype_3d_heartventricles2 import MeshType_3d_heartventricles2
from meshtypes.meshtype_3d_heartventriclesbase1 import MeshType_3d_heartventriclesbase1
from meshtypes.meshtype_3d_sphereshell1 import MeshType_3d_sphereshell1
from meshtypes.meshtype_3d_sphereshellseptum1 import MeshType_3d_sphereshellseptum1
from meshtypes.meshtype_3d_tube1 import MeshType_3d_tube1
from meshtypes.meshtype_3d_tubeseptum1 import MeshType_3d_tubeseptum1
from opencmiss.zinc.field import FieldGroup

class Scaffoldmaker(object):

    def __init__(self):
        self._allMeshTypes = [
            MeshType_2d_plate1,
            MeshType_2d_platehole1,
            MeshType_2d_sphere1,
            MeshType_2d_tube1,
            MeshType_3d_box1,
            MeshType_3d_boxhole1,
            MeshType_3d_heartatria1,
            MeshType_3d_heartventricles1,
            MeshType_3d_heartventricles2,
            MeshType_3d_heartventriclesbase1,
            MeshType_3d_sphereshell1,
            MeshType_3d_sphereshellseptum1,
            MeshType_3d_tube1,
            MeshType_3d_tubeseptum1
            ]

    def getMeshTypes(self):
        return self._allMeshTypes

    def getDefaultMeshType(self):
        return MeshType_3d_box1
    
    @staticmethod
    def defineAnnotationGroupFields(fieldModule, groupNames):
        for groupName in groupNames:
            f = fieldModule.createFieldGroup()
            f.setName(groupName)
            f.setManaged(True)
            f.setSubelementHandlingMode(FieldGroup.SUBELEMENT_HANDLING_MODE_FULL)

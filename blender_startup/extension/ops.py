import bpy
import os
import pickle
import numpy as np

from blender_figo import mesh as bmesh, collection as bcollection, scene as bscene
from blender_figo import objects as bobjects

BLENDER_COORD=np.array([[1,0,0],[0,0,-1],[0,1,0]])


class Operator(bpy.types.Operator):
    bl_idname = "extension.operator"
    bl_label = "Operator"
    bl_description = "A Sample Operator"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return False

    def execute(self, context):
        # TODO
        return {'FINISHED'}
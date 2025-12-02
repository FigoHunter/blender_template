from . import props, ops, panels
import bpy
from bpy.props import PointerProperty


bpy.utils.register_class(props.Properties)
bpy.types.Scene.extension = PointerProperty(type=props.Properties)
bpy.utils.register_class(ops.Operator)
bpy.utils.register_class(panels.Extension_PT_Panel)


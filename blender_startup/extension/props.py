import bpy
from bpy.props import ( BoolProperty, EnumProperty, FloatProperty, IntProperty, PointerProperty, StringProperty )
from bpy.types import ( PropertyGroup )


class Properties(PropertyGroup):
    path : StringProperty(
        name = "",
        description = "Path Property",
        default = "",
        subtype = 'FILE_PATH'
        ) # type: ignore
    
    type : EnumProperty(
        name = "Type",
        description = "Type Property",
        items = [
            ('a', "A", "type a"),
            ('b', "B", "type b"),
            ('c', "C", "type c"),
        ],
        default = 'a'
    ) # pyright: ignore[reportInvalidTypeForm]

    text : StringProperty(
        name = "",
        description = "String Property",
        default = "",
        ) # type: ignore
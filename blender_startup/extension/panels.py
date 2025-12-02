import bpy

class Extension_PT_Panel(bpy.types.Panel):
    bl_label = "Extension Panel"
    bl_idname = "EXTENSION_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Extension"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.label(text="Extension Settings")
        layout.prop(scene.extension, "path")
        layout.prop(scene.extension, "type")
        layout.prop(scene.extension, "text")
        layout.operator("extension.operator", text="Run Operator")
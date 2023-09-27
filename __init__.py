import bpy
import os

bl_info = {
    "name": "Export Selected Objects as FBX w. Presets",
    "author": "pleebs_xyz",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "File > Export > FBX",
    "description": "Exports selected objects as individual FBX files",
    "category": "Import-Export"
}


class ExportSelectedObjectsProps(bpy.types.PropertyGroup):
    preset_name: bpy.props.StringProperty(name="Preset Name", description="Specify the preset you saved in File/Export/Fbx dialog window here")
    move_to_origin: bpy.props.BoolProperty(name="Move to Origin", default=True, description="exports the objects at 0.0.0 and restores their org. Position after Export")

class OBJECT_OT_export_selected_objects(bpy.types.Operator):
    bl_idname = "object.export_selected_objects"
    bl_label = "Export Selected Objects"
    bl_description = "exports selected objects as individual .fbx-files"
    bl_options = {'REGISTER', 'UNDO'}

    def get_op(self, filepath):
        preset_name = os.path.splitext(os.path.basename(filepath))[0]
        preset_path = bpy.utils.preset_paths('operator/export_scene.fbx/')
        preset_full_path = os.path.join(preset_path[0], preset_name + '.py')

        if os.path.exists(preset_full_path):
            class Container(object):
                __slots__ = ('__dict__',)

            op = Container()
            with open(preset_full_path, 'r') as f:
                for line in f.readlines()[3::]:
                    exec(line, globals(), locals())

            return op

        return None

    def execute(self, context):
        preset = context.scene.export_selected_objects_props.preset_name
        move_to_origin = context.scene.export_selected_objects_props.move_to_origin
        selected_objects = context.selected_objects

        op = self.get_op(preset)
        if op is None:
            raise RuntimeError("Failed to load preset '{}'".format(preset))

        for obj in selected_objects:
            # temporarily deselect all objects except for the current object
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)

            # move the object to the origin point
            if move_to_origin:
                original_location = obj.location.copy()
                obj.location = (0, 0, 0)

            # set the export filepath to include the object name
            filepath = os.path.join(os.path.dirname(bpy.data.filepath), bpy.path.ensure_ext(obj.name, '.fbx'))

            # export the object as an FBX file
            kwargs = op.__dict__.copy()
            kwargs['filepath'] = filepath
            kwargs['use_selection'] = True
            bpy.ops.export_scene.fbx(**kwargs)

            # reset the object location to its original location
            if move_to_origin:
                obj.location = original_location

        # re-select all objects that were selected before
        for obj in selected_objects:
            obj.select_set(True)

        return {'FINISHED'}

class OBJECT_OT_rename_mesh(bpy.types.Operator):
    bl_idname = "object.rename_mesh"
    bl_label = "Rename Mesh to ObjectName's MeshName"
    bl_description = "Rename MeshName to objectname,for all selected objects ; can be handy in some engines like UE"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects = context.selected_objects

        for obj in selected_objects:
            if obj.type == 'MESH':
                obj.data.name = obj.name

        return {'FINISHED'}

class OBJECT_PT_export_selected_objects_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_export_selected_objects_panel"
    bl_label = "FBX Export Selected Objects"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FBX Batch'

    def draw(self, context):
        layout = self.layout
        props = context.scene.export_selected_objects_props

        layout.prop(props, "preset_name")
        layout.prop(props, "move_to_origin")
        
        row = layout.row()
        row.scale_y = 2  # Adjust the button width
        row.operator("object.export_selected_objects", icon='EXPORT', text="Export")
        
        layout.separator()
        
        row = layout.row()
        row.scale_y = 0.9 # Adjust the button width
        row.operator("object.rename_mesh", text="Rename Mesh", icon='MESH_CUBE')
        
                
def register():
    bpy.utils.register_class(ExportSelectedObjectsProps)
    bpy.utils.register_class(OBJECT_OT_export_selected_objects)
    bpy.utils.register_class(OBJECT_OT_rename_mesh)
    bpy.utils.register_class(OBJECT_PT_export_selected_objects_panel)
    bpy.types.Scene.export_selected_objects_props = bpy.props.PointerProperty(type=ExportSelectedObjectsProps)

def unregister():
    bpy.utils.unregister_class(ExportSelectedObjectsProps)
    bpy.utils.unregister_class(OBJECT_OT_export_selected_objects)
    bpy.utils.unregister_class(OBJECT_OT_rename_mesh)
    bpy.utils.unregister_class(OBJECT_PT_export_selected_objects_panel)
    del bpy.types.Scene.export_selected_objects_props

    
if __name__ == '__main__':
    register()

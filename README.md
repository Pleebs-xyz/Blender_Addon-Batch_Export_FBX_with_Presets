![FBX_addon1](https://github.com/Pleebs-xyz/blender-addon-Batch-Export-FBX-with-Presets./assets/142031831/0c3cf1bc-18de-4f0d-89d5-547decce6af0)

# blender-addon-Batch-Export-FBX-with-Presets

I recently had to export many foliage-assets, so I made myself a little script to aid me.

It exports all selected objects as individual .Fbx- files. inheriting the Objectname, and utilizing blenders build-in Fbx export Operator Presets.

Thought this might be useful for anyone else too, so i created this small and lightweight Addon for it.


https://github.com/Pleebs-xyz/blender-addon-Batch-Export-FBX-with-Presets./assets/142031831/f718837a-ddb3-42ff-9538-46260ca0b370


# Here's how it works:

* Install and activate the add-on, like any other blender Addon. Now it show up in you N-panel under 'FBX Batch'
* Save your .blend file in the directory you want to Export to. The Script exports the fbx-files to the same Directory the blend is stored in.
* Go to File/Export/Fbx and enter a preset. You can do this simply by creating the right settings, and then press the little '+' Icon (Top right, next to the Operator Presets Drop-down) and giving it a name.
* Now you can enter the same name into the Preset Name Text-Input-Field of the Add-on. Has to be the exact name!
* The Move to Origin -Bool/Checkbox, moves to objects temporarily to Worldcenter (0,0,0) whilst exporting, and is on by default. Deactivate if you don't want this behavior.
* Hit the Export-Button and the add-on will export all selected objects as a individual .fbx file. inheriting the object name.


Tested in Blender 3.5.1

Hope it saves you time too!



### My Social-media:

https://twitter.com/Pleebs_xyz

https://blenderartists.org/u/pleebs/activity/portfolio

https://www.instagram.com/pleebs_xyz/



Discord: https://discord.gg/bRbzbST8ra

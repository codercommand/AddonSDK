# AddonSDK
version 1.1

This is a command line program for making minecraft behavior pack addons.


The Zip packer for packing addons is
not beleaved to be the most stable,
bugs with it are kinda known.


The AddonSDK is a standard development kit
for making behavior addons

the SDK currently only supports the creation
of behavior packs

all the following directorys are supported:

pack_manifest.json
pack_icon.png
entities/<file name>
loot_table/<folder name>/<file names>


the SDK currently only has the following commands:

$ random 
random returns a random uuid for your projects

$ exit
this can be used to close the console instead of the exit button

$ make manifest
this is used to make a manifest for anyone that only
wants a manifest, the manifests already come with a random 
uuid, so no need to find one

$ make ziper
this can be used to make a ziper program, for if anyone wants to zip
a pack but never made it with the $ new <project name>
command

$ new <project name>
this is used to start a behavior addon pack,
it'll make the manifest, ziper, entities, and loot_tables
folder/files

$ update <project name>
this is used to change/update the manifest in an already made
project, when doing so it'll also make new uuids for the manifest

import os

os.system("title Easy Datapack Generation")

WorldName = ""
DatapackName = ""
DatapackDisplayName = ""
VersionID = 0
MainBranchName = ""
GenerateTickFunction = False
GenerateLoadFunction = False

print("\n    Easy Datapack Generation - 1.0")
print("\n")

if os.path.exists("saves/"):

    WorldName = input("    Please enter the world file name in which you want to create the Datapack in.: ")
    DatapackName = input("    Select an internal name for the Datapack. (e.g. CoolDatapack; Do not use spaces.): ")
    DatapackDisplayName = input("    Select a Display name for the Datapack. (Minecraft Syntax formatting is supported.): ")
    VersionID = input("    Select the Version of the Datapack. (e.g. 1.16.4 = 6): ")
    MainBranchName = input("    Select the Name for the Main Branch. (e.g. cool_datapack_main; Do not use spaces, uppercase letters or special characters.): ")
    GenerateTickFunction = input("    Generate a tick function? (True or False; case sensitive.): ")
    GenerateLoadFunction = input("    Generate a load function? (True or False; case sensitive.): ")

    if os.path.exists("saves/" + WorldName + "/"):

        os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName)
        os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data")
        os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/minecraft/")

        os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/" + MainBranchName + "/")
        os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/" + MainBranchName + "/functions/")

        if GenerateTickFunction or GenerateLoadFunction:

            os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/minecraft/tags/")
            os.mkdir("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/minecraft/tags/functions/")
            
            if GenerateTickFunction == "True":
            
                with open("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/" + MainBranchName + "/functions/tick.mcfunction", "w") as TickFunction: TickFunction.write("")
                with open("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/minecraft/tags/functions/tick.json", "w") as TickTag: TickTag.write("{\n    \"values\": [\n        \"" + MainBranchName + ":tick\"\n    ]\n}")
                
            if GenerateLoadFunction == "True":
            
                with open("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/" + MainBranchName + "/functions/load.mcfunction", "w") as LoadFunction: LoadFunction.write("")
                with open("saves/" + WorldName + "/Datapacks/" + DatapackName + "/data/minecraft/tags/functions/load.json", "w") as LoadTag: LoadTag.write("{\n    \"values\": [\n        \"" + MainBranchName + ":load\"\n    ]\n}")

        with open("saves/" + WorldName + "/Datapacks/" + DatapackName + "/pack.mcmeta", "w") as PackMCMeta: PackMCMeta.write("{\n    \"pack\": {\n	\"pack_format\": " + VersionID + ",\n	\"description\": \"" + DatapackDisplayName +  "\"\n    }\n}")
        
    else:
    
        print("\n    Could not find world save \"" + WorldName + "\".\n")

        os.system("pause")
    
else:

    print("    Could not detect saves folder.\n")

    os.system("pause")
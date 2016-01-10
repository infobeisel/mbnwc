from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

scenes = [


#OPEN WORLD
  ("ow_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
     [],[],"outer_terrain_plain"),

  ("ow_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("ow_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000000000fffff000000000000000000000000",
     [],[],"outer_terrain_plain"),
     
  ("ow_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
     [],[],"outer_terrain_plain"),

  ("ow_multiplayer_scenes_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[],"outer_terrain_plain"),
#OPEN WORLD END
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[]),
  ("conversation_scene",0,"none", "none", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),
  ("random_scene_steppe",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_desert"),
  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_plain"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),

    
  ("tutorial",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
    

  # # # Randoms
  
  # plain
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_medium_rain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large_rain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  
  # steppe
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_forest_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x00000001a8601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_forest_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x00000001aa00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  
  # snow
  ("random_multi_snow_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001494018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_medium_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001494018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000014a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_large_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000014a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_forest_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001c94018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_forest_medium_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001c94018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001ca001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_snow"),
  ("random_multi_snow_forest_large_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001ca001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_snow"),
  
  # Desert
  ("random_multi_desert_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000158601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_desert"),
  ("random_multi_desert_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000015a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_desert"),
  ("random_multi_desert_forest_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x00000001d8601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_desert"),
  ("random_multi_desert_forest_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x00000001da00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_desert"),

  # Forest
  ("random_multi_forest_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001b94018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_forest_medium_rain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001b94018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_forest_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001ba001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_forest_large_rain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001ba001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),

######################

### CUSTOM

  ("mp_custom_map_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_18",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  ("mp_custom_map_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
     [],[],"outer_terrain_plain"),
  
  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  
  ("quick_battle_french_farm",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
     [],[],"outer_terrain_plain"),
  ("quick_battle_landshut",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e00078584000011c60000285b00005cbe",
     [],[],"outer_terrain_plain"),
  ("quick_battle_river_crossing",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
     [],[],"outer_terrain_plain"),
  ("quick_battle_spanish_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
     [],[],"outer_terrain_steppe"),
  ("quick_battle_strangefields",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
     [],[],"outer_terrain_plain"),
  
  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000013c665098000769d80000534600001adc00001118", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000014940095d000649920004406900002920000056d7", 
    [],[], "outer_terrain_snow"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001bc6fd0ae000611870000202600001adc0000240e", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000122f00b52000611870000175c00007b5c00003013", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001db034fc50006118500001d4900007f70000073fc",
    [],[],"outer_terrain_desert_b"),
  
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001db034fc50006118500001d4900007f70000073fc",
    [],[],"outer_terrain_plain"),

    
  # SP Scenes

  # Vienna battles
  ("sp_vienna",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  
  # Austerlitz battles
  ("sp_sokolniz",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  ("sp_auster",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024ee3400d2348591ef0ff00001bb1647fd81f",
    [],[],"outer_terrain_plain"),
  ("sp_sokolniz2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  
  # Dresden battles
  ("sp_dresden1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  ("sp_dresden2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),

  # Test crap
  ("sp_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  ("sp_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  ("sp_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
  ("sp_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330004563000d23480000074800005c49000021c5",
    [],[],"outer_terrain_plain"),
 
  # Camps
  ("sp_camp_austerlitz",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("sp_camp_dresden",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),  
 
]

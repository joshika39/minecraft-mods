from mod import ModManager, PackManager
from baselib import minecraft_path
from modoperations import copy_to_target
from picker import SingleMenu

mod_mgr = ModManager(True)
pack_mgr = PackManager(mod_mgr, True)
pack = pack_mgr.select_mod_packs()

if pack is not None:
	copy_to_target(mod_mgr, pack.pack_content, minecraft_path())
	input("Press Enter to exit...")


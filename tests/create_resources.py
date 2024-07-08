# -*- coding: utf-8 -*-
from resource_pack import ResourceManager, __version__


manager = ResourceManager()
manager.add_file("python_logo.png", "logo")
manager.add("version", __version__)
manager.add_glob("*.*", "resource_files")

manager.dump("test.res")

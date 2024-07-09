# -*- coding: utf-8 -*-
"""
Resource packaging manager for python(written in pure python)
"""

__version__ = "0.2.0"


from .resource_manager import ResourceManager
load = ResourceManager.load

__all__ = [
    "load",
    "ResourceManager"
]

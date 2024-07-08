# -*- coding: utf-8 -*-
"""
Resource packaging manager for python(written in pure python)
"""

__version__ = "0.1.0"


from .functions import load
from .resource_manager import ResourceManager

__all__ = [
    "load",
    "ResourceManager"
]

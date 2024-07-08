# -*- coding: utf-8 -*-
from .resource_manager import ResourceManager


def load(resource_file:str) -> ResourceManager:
    return ResourceManager.load(resource_file)

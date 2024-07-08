# -*- coding: utf-8 -*-
import os, pathlib, pprint, pickle
from typing import Any, Union


class ResourceManager:
    def __init__(self):
        self.__map = {}

    def __str__(self) -> str:
        return f"""ResourceManager at {hex(id(self))}
{pprint.pformat(self.__map, 4)}
"""

    def __getitem__(self, name:str) -> Any:
        return self.__map[name]
    
    @staticmethod
    def load(resource_file:str) -> "ResourceManager":
        resource_file = pathlib.Path(resource_file).resolve()
        with open(resource_file, "rb") as dfr:
            manager = pickle.load(dfr)

        return manager

    def add_file(self, file_path:Union[str, pathlib.Path, os.PathLike], name:str = None):
        if not isinstance(file_path, pathlib.Path):
            file_path = pathlib.Path(file_path).resolve()

        if name is None:
            name = file_path.name

        try:
            with open(str(file_path), "r", encoding = "utf-8") as rfr:
                self.__map[name] = rfr.read()
        except UnicodeDecodeError:
            with open(str(file_path), "rb") as rfr:
                self.__map[name] = rfr.read()

    def add(self, name:str, value:Any):
        self.__map[name] = value

    def add_glob(self, pattern:str = "*.*", root_path:Union[str, pathlib.Path, os.PathLike] = None):
        if root_path is None:
            root_path = os.getcwd()

        if not isinstance(root_path, pathlib.Path):
            root_path = pathlib.Path(root_path)

        for glob_file in root_path.glob(pattern):
            self.add_file(glob_file)

    def dump(self, resource_file:str):
        resource_file = pathlib.Path(resource_file).resolve()
        with open(resource_file, "wb") as dfw:
            pickle.dump(self, dfw)

    def export(self, python_file:str):
        python_file = pathlib.Path(python_file).resolve()
        with open(python_file, "w", encoding = "utf-8") as etp:
            etp.write(f"""# -*- coding: utf-8 -*-
import pickle
from typing import Dict, Union, Any

resources:Dict[str, Union[str, bytes, Any]] = pickle.loads({pickle.dumps(self.__map)})
""")

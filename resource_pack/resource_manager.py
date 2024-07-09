# -*- coding: utf-8 -*-
import os, pathlib, pprint, codecs, pickle, py_compile
from typing import Any, Union


class ResourceManager:
    """
    ResourceManager class
    """
    def __init__(self):
        self.__map = {}

    def __str__(self) -> str:
        return f"""ResourceManager at {hex(id(self))}
{pprint.pformat(self.__map, 4)}
"""

    def __getitem__(self, name:str) -> Any:
        return self.__map[name]
    
    @staticmethod
    def load(resource_file:Union[str, pathlib.Path, os.PathLike]) -> "ResourceManager":
        """
        load from resource file

        Parameters
        ----------
        - resource_file: path of resource file(Union[str, pathlib.Path, os.PathLike])

        Return
        ------
        ResourceManager
        """
        if not isinstance(resource_file, pathlib.Path):
            resource_file = pathlib.Path(resource_file).resolve()

        with open(resource_file, "rb") as dfr:
            manager = pickle.load(dfr)

        return manager

    def add_file(self, file_path:Union[str, pathlib.Path, os.PathLike], name:str = None) -> "ResourceManager":
        """
        add file to ResourceManager

        Parameters
        ----------
        - file_path: path of file to add(Union[str, pathlib.Path, os.PathLike])
        - name: name to add(type: str, default: None)

        Return
        ------
        ResourceManager
        """
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

        return self

    def add(self, name:str, value:Any) -> "ResourceManager":
        """
        add value to ResourceManager

        Parameters
        ----------
        - name: name to add(str)
        - value: value to add(Any)
        
        Return
        ------
        ResourceManager
        """
        self.__map[name] = value

        return self

    def add_glob(self, pattern:str = "*.*", root_path:Union[str, pathlib.Path, os.PathLike] = None, as_tree:bool = True, include_ext:bool = True) -> "ResourceManager":
        """
        add files by glob pattern to ResourceManager

        Parameters
        ----------
        - pattern: pattern to search by glob(type: str, default: "*.*")
        - root_path: path of glob pattern search(type: Union[str, pathlib.Path, os.PathLike], default: None)
        - as_tree: add name as tree or not(type: bool, default: True)
        - include_ext: include extention to name or not(type: bool, default: True)

        Return
        ------
        ResourceManager
        """
        if root_path is None:
            root_path = os.getcwd()

        if not isinstance(root_path, pathlib.Path):
            root_path = pathlib.Path(root_path)

        for glob_file in root_path.glob(pattern):
            if as_tree:
                name_to_add = str(glob_file).replace(str(root_path), "").replace("\\", "/")
            else:
                name_to_add = glob_file.name

            self.add_file(glob_file, name_to_add if include_ext else os.path.splitext(name_to_add)[0])

        return self

    def dump(self, resource_file:Union[str, pathlib.Path, os.PathLike]):
        """
        dump resources into file

        Parameters
        ----------
        - resource_file: path of resource file(Union[str, pathlib.Path, os.PathLike])
        """
        if not isinstance(resource_file, pathlib.Path):
            resource_file = pathlib.Path(resource_file).resolve()

        with open(resource_file, "wb") as dfw:
            pickle.dump(self, dfw)

    def export(self, python_file:Union[str, pathlib.Path, os.PathLike], as_pyc:bool = False, remove_origin:bool = False):
        """
        export resources into python file

        can be loaded where `py-resource-pack` is not installed

        Parameters
        ----------
        - python_file: python file to export(Union[str, pathlib.Path, os.PathLike])
        - as_pyc: compile to pyc or not(type: bool, default: False)
        - remove_origin: remove origin python file or not only when `as_pyc` is True(type: bool, default: False)
        """
        if not isinstance(python_file, pathlib.Path):
            python_file = pathlib.Path(python_file).resolve()

        with open(str(python_file), "w", encoding = "utf-8") as etp:
            etp.write(f"""# -*- coding: utf-8 -*-
import pickle, codecs
from typing import Dict, Union, Any

resources:Dict[str, Union[str, bytes, Any]] = pickle.loads(codecs.decode('''{codecs.encode(pickle.dumps(self.__map), "base64").decode()}'''.encode(), "base64"))
""")

        if as_pyc:
            py_compile.compile(str(python_file), str(python_file) + "c")

            if remove_origin:
                os.remove(str(python_file))

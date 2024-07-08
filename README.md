<h1 align="center">
    resource.pack
</h1>
<p align="center">
    Resource packaging manager for python(written in pure python)
</p>
<br/>

<div align="center">
    <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue" />
    <br>
    <a href="https://github.com/somehitDev/resource-pack/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/somehitDev/resource-pack.svg" alt="GPL-3.0 License" />
    </a>
    <a href="https://pypi.org/project/resource-pack/">
        <img src="https://img.shields.io/pypi/v/resource-pack.svg" alt="pypi" />
    </a>
</div><br><br>

## 🛠️ Installation
- install from git(latest)
```bash
pip install git@github.com:somehitDev/resource-pack.git
```
- pypi
```bash
pip install py-resource-pack
```

<br>

## 📄 Usage
```python
## create resource
manager = ResourceManager()
# add file
manager.add_file("{file_path}", "{name}")
# add value
manager.add("{name}", {value})
# add with glob pattern
manager.add_glob("{pattern}", "{root_path}")

## dumps to file
manager.dump("{resource_file}")

## load from file
load("{resource_file}")
# or
ResourceManager.load("{resource_file}")

## export as python file
manager.export("{python_file}")
```

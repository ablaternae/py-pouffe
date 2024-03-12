# PoufDB

_Naming: pouf (aka pouffe) literally means a padded chair. 
PoufDB is based on [ChairDB source code](https://github.com/marten-de-vries/chairdb)._

[![PyPI - Version](https://img.shields.io/pypi/v/chitchat.svg)](https://pypi.org/project/chitchat)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chitchat.svg)](https://pypi.org/project/chitchat)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install poufdb
```
```console
git clone --depth=1 https://github.com/ablaternae/py-pouffe .
pip install --upgrade .
```

## Run
```console
> poufdb.exe --help
Usage: poufdb [OPTIONS] COMMAND [ARGS]...

Options:
  -r, --start                     API REST Server run
  -d, --data-dir PATH             Data directory, default `%current_dir%/_data`
  -a, --admin-panel               Start discrete server for admin panel
                                  (disable now)
  --host TEXT                     Host, default `0.0.0.0`
  --port INTEGER                  Port, default `5984`
  --engine [sqlite|inmemory|csv]  Backend engine (disable now)
  -v, --version                   Show the version and exit
  -h, --help                      Show this message and exit
```


## License

`chitchat` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

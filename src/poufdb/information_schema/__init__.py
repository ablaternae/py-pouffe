# =============================================================================
#
# dynamic config
#
# =============================================================================


import sys
from typing import Any, NoReturn, Final, Literal, TypedDict, Union, Optional
from types import ModuleType


class InformationSchema(ModuleType):
    def __repr__(self) -> str:
        return f"Schema {self.__name__}"

    def __getitem__(self, name: str) -> Any:
        print(str(name) + "!!!")
        ...


sys.modules[__name__].__class__ = InformationSchema

# =============================================================================
#
# dynamic config
#
# =============================================================================


import sys
from types import ModuleType, SimpleNamespace
from typing import Any, Callable, Iterable, Mapping

import ujson as json


class InformationSchema(ModuleType):
    """Singletone to config them all."""

    def __repr__(self) -> str:
        return f"InformationSchema <{self.__name__}>"

    def __dir__(self) -> list:
        return list(
            filter(
                lambda k: not isinstance(self[k], (Callable, ModuleType)),
                filter(lambda k: not k.startswith("__"), self.__dict__.keys()),
            )
        )

    def __getitem__(self, name: str) -> Any:
        return getattr(self, str(name), None)

    def __setitem__(self, name: str, value: Any = None) -> Any:
        return setattr(self, str(name), value)

    def from_dict(self, obj: dict, uppercase_only: bool = False) -> Any:
        """@see also from_object().

        :param obj: source dict
        :param uppercase_only: import upper KEYS only, defaults to False
        :return: Self

        """

        if isinstance(obj, dict):
            for k, v in obj.items():
                if not uppercase_only or k.isupper():
                    if not isinstance(v, (Callable, ModuleType)):
                        self[k] = v

        return self

    def from_object(self, obj: object, uppercase_only: bool = False) -> Any:
        """
        Updates the values from the given object.  An object can be of one
        of the following two types:

        -   @DEPRECATED a string: in this case the object with that name will be imported
        -   an actual object reference: that object is used directly

        Objects are usually either modules or classes. :meth:`from_object`
        loads only the uppercase attributes of the module/class. A ``dict``
        object will not work with :meth:`from_object` because the keys of a
        ``dict`` are not attributes of the ``dict`` class.

        Example of module-based configuration::

            app.config.from_object('yourapplication.default_config')
            from yourapplication import default_config
            app.config.from_object(default_config)

        Nothing is done to the object before loading. If the object is a
        class and has ``@property`` attributes, it needs to be
        instantiated before being passed to this method.

        You should not use this function to load the actual configuration but
        rather configuration defaults.  The actual config should be loaded
        with :meth:`from_pyfile` and ideally from a location not within the
        package because the package might be installed system wide.

        See :ref:`config-dev-prod` for an example of class-based configuration
        using :meth:`from_object`.

        :param obj: an import name or object
        """
        #

        if isinstance(obj, dict) or (
            hasattr(obj, "keys") and isinstance(obj.keys, Callable)
        ):
            return self.from_dict(obj)

        if isinstance(obj, Mapping):
            return self.from_mapping(obj)

        keys = dir(obj)
        keys = filter(lambda x: not x.startswith("__"), keys)
        if uppercase_only:
            keys = filter(str.isupper, keys)

        for k in keys:
            # https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
            attr = getattr(obj, k)
            if not isinstance(attr, (Callable, ModuleType)):
                # ModuleType кажется лишним
                # можно проверить через исключение pickle.dumps( attr )
                self[k] = attr

        return self

    def from_mapping(
        self,
        mapping: Mapping[str, Any] | None = None,
        uppercase_only: bool = False,
        **kwargs: Any,
    ) -> Any:
        """
        Updates the config like :meth:`update` ignoring items with
        non-upper keys.

        :return: Always returns ``True``.

        .. versionadded:: 0.11
        """

        mappings: dict[str, Any] = {}

        if mapping is not None:
            mappings.update(mapping)
        mappings.update(kwargs)

        for key, value in mappings.items():
            if not uppercase_only or key.isupper():
                self[key] = value

        return self

    def get_namespace(
        self, namespace: str, lowercase: bool = False, trim_namespace: bool = True
    ) -> Iterable | dict[str, Any]:
        """Return dict with trimmed keys.

        Returns a dictionary containing a subset of configuration options
        that match the specified namespace/prefix. Example usage::

            app.config['IMAGE_STORE_TYPE'] = 'fs'
            app.config['IMAGE_STORE_PATH'] = '/var/app/images'
            app.config['IMAGE_STORE_BASE_URL'] = 'http://img.website.com'
            image_store_config = app.config.get_namespace('IMAGE_STORE_')

        The resulting dictionary `image_store_config` would look like::

            {
                'type': 'fs',
                'path': '/var/app/images',
                'base_url': 'http://img.website.com'
            }

        This is often useful when configuration options map directly to
        keyword arguments in functions or class constructors.

        :param namespace: a configuration namespace
        :param lowercase: a flag indicating if the keys of the resulting
                          dictionary should be lowercase
        :param trim_namespace: a flag indicating if the keys of the resulting
                          dictionary should not include the namespace

        .. versionadded:: 0.11
        """

        rv = {}
        d = filter(lambda x: x.startswith(namespace), dir(self))
        ln = len(namespace)

        # for k in d:
        #    key = k[ln:] if trim_namespace else k
        #    if lowercase:
        #        key = key.lower()
        #    rv[key] = self[k]

        rv = [(k[ln:] if trim_namespace else k, self[k]) for k in d]
        if lowercase:
            rv = map(lambda x: (x[0].lower(), x[1]), rv)

        return rv

    def to_json(
        self,
        namespace: str = None,
        lowercase: bool = False,
        trim_namespace: bool = True,
    ) -> Any:

        return json.loads(self.to_json_string(namespace, lowercase, trim_namespace))

    def to_json_string(
        self,
        namespace: str = None,
        lowercase: bool = False,
        trim_namespace: bool = True,
    ) -> Any:
        if not isinstance(namespace, str):
            namespace = ""

        return json.dumps(self.to_dict(namespace, lowercase, trim_namespace))

    def to_dict(
        self,
        namespace: str = None,
        lowercase: bool = False,
        trim_namespace: bool = True,
    ) -> dict:
        if not isinstance(namespace, str):
            namespace = ""

        return dict(self.get_namespace(namespace, lowercase, trim_namespace))

    def to_object(
        self,
        namespace: str = None,
        lowercase: bool = False,
        trim_namespace: bool = True,
    ) -> object:

        # https://stackoverflow.com/a/56596405

        return SimpleNamespace(**self.to_dict(namespace, lowercase, trim_namespace))

    get_dict = to_dict
    get_json = to_json
    get_json_string = to_json_string
    get_object = to_object

    pass


sys.modules[__name__].__class__ = InformationSchema


__all__ = ()

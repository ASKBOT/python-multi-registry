"""Contains a single class :class:`MultiRegistry`,
please see doc string in the class for the further information.
"""
#todo: allow adding dictionaries as registry stores
#todo: support caching
from import_utils import import_module_from

__version__ = '0.0.2'

class MultiRegistry(object):
    """Allows to aggregate key-value data from many sources.
    Can be used, for example, as a proxy to settings object in Django framework.

    The sources of key-value data are appended to :class:`MultiRegistry`
    vi ``append()`` method, then looked up via standard Python
    dotted notation, as explained in more detail below.

    Upon access, attributes will be looked up in the parent objects
    in the order the latter were appended.

    For example, if we have two settings like objects:
    ``A`` with attribute ``a``
    and ``B`` with attribute ``b``
    and a third one, found in module importable from ``'some.registry.C'``,
    we can construct the registry as:

    >>>r = MultiRegistry([A, B, 'some.registry.C'])

    or alternatively:

    >>>r = MultiRegistry()
    >>>r.append(A)
    >>>r.append(B)
    >>>r.insert(2, 'some.registry.C')

    .. note::
        The registries can be provided as python objects or
        dotted python paths. In the latter case an import error will
        be raised if module at the path does not exist

    then access the registry as:

    r.b - attrubute b will be first looked
    up in the object A, then in the object B, where
    it will be found.

    If there is an attribute present in more than one appended object,
    the first one will be returned - in the same order the 
    registries are stored internally, which takes into account:

    * order the registries were provided at the object initialization
    * order of ``append()`` calls.
    * taking into account indices provided with ``insert()`` call

    If the attribute is not found, attribute error will be 
    raised.
    """
    def __init__(self, registry_objects = None):
        self.registry_stores = list()
        if registry_objects:
            for reg in registry_objects:
                self.append(reg)

    def append(self, registry_store):
        """adds a registry object to the list of
        """
        last_pos = len(self.registry_stores)
        self.insert(last_pos, registry_store)

    def insert(self, index, registry_store):
        """Inserts a registry store at a given position in the
        internal registry list"""
        if isinstance(registry_store, str):
            reg_obj = import_module_from(registry_store)
        else:
            reg_obj = registry_store

        if reg_obj in self.registry_stores:
            raise ValueError('duplicate registry inserted')
        self.registry_stores.insert(index, reg_obj)

    def __getattr__(self, attr_name):
        for store in self.registry_stores:
            if hasattr(store, attr_name):
                return getattr(store, attr_name)
        raise AttributeError('setting %s not found' % attr_name)


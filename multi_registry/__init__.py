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
    and we construct registry as:

    >>>r = MultiRegistry()
    >>>r.append_registry(A)
    >>>r.append_registry(B)

    then access the registry as:

    r.b - attrubute b will be first looked
    up in the object A, then in the object B, where
    it will be found.

    If there is an attribute present in more than one appended object,
    the first one will be returned - in the order of ``append()`` call.

    A second way to initialize the registry is to supply a tuple or a list
    of registry objects or python paths to those objects to the __init__ method:

    >>>r = MultiRegistry([settings, 'mymodule.conf.settings'])

    The tuple or a list may be mixed - some items might be settings objects
    and others - python dotted paths.

    If the attribute is not found, attribute error will be 
    raised.
    """
    def __init__(self, registry_objects = None):
        self.registry_stores = list()
        if registry_objects:
            for reg_info in registry_objects:
                if isinstance(reg_info, str):
                    reg_obj = import_module_from(reg_info)
                else:
                    reg_obj = reg_info
            self.registry_stores.append(reg_obj)
                    

    def append_registry(self, registry_store):
        """adds a registry object to the list of
        """
        self.registry_stores.append(registry_store)

    def __getattr__(self, attr_name):
        for store in self.registry_stores:
            if hasattr(store, attr_name):
                return getattr(store, attr_name)
        raise AttributeError('setting %s not found' % attr_name)


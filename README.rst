Allows to aggregate key-value data from many sources.
Can be used, for example, as a proxy to settings object in Django framework.

The sources of key-value data are appended to :class:`MultiRegistry`
vi ``append()`` method, then looked up via standard Python
dotted notation, as explained in more detail below.

Upon access, attributes will be looked up in the parent objects
in the order the latter were appended.

For example, if we have two settings like objects:
``A`` with attribute ``a``
and ``B`` with attribute ``b``
and we construct registry as::

    from multi_registry import MultiRegistry
    r = MultiRegistry()
    r.append(A)
    r.append(B)

then access the registry as:

``r.b`` - attrubute b will be first looked
up in the object ``A``, then in the object ``B``, where
it will be found.

If there is an attribute present in more than one appended object,
the first one will be returned - in the order of ``append()`` call.

If the attribute is not found, attribute error will be 
raised.

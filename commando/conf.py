"""
A few wrappers and utilities for handling complex
configuration objects.
"""

from collections import defaultdict

SEQS = (tuple, list, set, frozenset)

class ConfigDict(defaultdict):
    """
    A patchable dictionary like object that allows accessing items
    as attributes.
    """

    def __init__(self, initial=None):
        super(ConfigDict, self).__init__(ConfigDict)
        initial = initial or {}
        for key, value in initial.iteritems():
            self.__setitem__(key, value)

    def __setitem__(self, key, value):
        # pylint: disable-msg=C0111
        def transform(primitive):
            if isinstance(primitive, dict):
                return ConfigDict(primitive)
            elif isinstance(primitive, SEQS):
                seq = type(primitive)
                return seq(transform(v) for v in primitive)
            else:
                return primitive
        super(ConfigDict, self).__setitem__(key, transform(value))

    def __getitem__(self, key):
        return super(ConfigDict, self).__getitem__(key)

    def copy(self):
        """
        Returns a copy of the config dict object.
        """
        return ConfigDict(self)

    def patch(self, overrides):
        """
        Patches the config with the given overrides.

        Example:

        If the current dictionary looks like this:
        a: 1,
        b: {
            c: 3,
            d: 4
        }

        and `patch` is called with the following overrides:
        b: {
            d: 2,
            e: 4
        },
        c: 5

        then, the following will be the resulting dictionary:
        a: 1,
        b: {
            c: 3,
            d: 2,
            e: 4
        },
        c: 5

        """
        overrides = overrides or {}
        for key, value in overrides.iteritems():
            current = self.get(key)
            if isinstance(value, dict) and isinstance(current, dict):
                current.patch(value)
            else:
                self[key] = value

    __setattr__ = __setitem__
    __getattr__ = __getitem__


# pylint: disable-msg=R0903
class AutoPropDescriptor(object):
    """
    Descriptor for providing default values.
    """

    def __init__(self, default_prop):
        self.default_prop = default_prop
        self.name = default_prop.__name__
        self.assigned = '_' + self.name

    def __get_assigned__(self, instance):
        return getattr(instance, self.assigned, None)

    def __set_assigned__(self, instance, value):
        return setattr(instance, self.assigned, value)

    def __get__(self, instance, owner):
        value = self.__get_assigned__(instance)
        return value or self.default_prop(instance)

    def __set__(self, instance, value):
        self.__set_assigned__(instance, value)

# pylint: disable-msg=R0903
class AutoPropMetaClass(type):
    """
    Meta class for enabling autoprops.
    """
    def __new__(mcs, cname, cbases, cattrs):
        autoprops = {name: member
                        for name, member in cattrs.iteritems()
                        if getattr(member, 'autoprop', False)}
        for name, member in autoprops.iteritems():
            cattrs[name] = AutoPropDescriptor(member)
        return super(AutoPropMetaClass, mcs).__new__(
                mcs, cname, cbases, cattrs)

# pylint: disable-msg=R0903
class AutoProp(object):
    """
    The base class for all objects supporting autoprops.

    Usage:

    class Project(AutoProp):

        def __init__(self, config=None):
            self.config = config or {}

        @AutoProp.default
        def source_dir(self):
            return self.config.get('source')

    p = Project({'source': 'test'})
    p.source_dir
    >>> 'test'
    p.source_dir = 'xyz'
    p.source_dir
    >>> 'xyz'

    """
    __metaclass__ = AutoPropMetaClass

    @staticmethod
    def default(function):
        """
        Decorator for autoprops.
        """
        function.autoprop = True
        return function

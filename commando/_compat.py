"""Python 2 and 3 compatibility module."""

# Note: borrowed from https://github.com/dirn/Simon/

import sys

# Development should be done with Python 3 first. Rather than checking
# for Python 3 and creating special cases for it, check for Python 2 and
# create special cases for it instead.
PY2 = sys.version_info[0] == 2

if PY2:
    # Define everything that is Python 2 specific.

    # dictionary iterators
    _iteritems = 'iteritems'
    _iterkeys = 'iterkeys'
    _itervalues = 'itervalues'

    # other iterators
    def get_next(x): return x.next
    range = xrange  # NOQA, Python 2 only

    # types
    str_types = (str, unicode)  # NOQA, Python 2 only

    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')
else:
    # Define everything that is Python 3 specific.

    # dictionary iterators
    _iteritems = 'items'
    _iterkeys = 'keys'
    _itervalues = 'values'

    # other iterators
    def get_next(x): return x.__next__
    range = range

    # types
    str_types = (str,)

    def reraise(tp, value, tb=None):
        if getattr(value, '__traceback__', tb) is not tb:
            raise value.with_traceback(tb)
        raise value


def iteritems(d, *args, **kwargs):
    return iter(getattr(d, _iteritems)(*args, **kwargs))


def iterkeys(d, *args, **kwargs):
    return iter(getattr(d, _iterkeys)(*args, **kwargs))


def itervalues(d, *args, **kwargs):
    return iter(getattr(d, _itervalues)(*args, **kwargs))


def with_metaclass(meta, *bases):
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.  Because of internal type checks
    # we also need to make sure that we downgrade the custom metaclass
    # for one level to something closer to type (that's why __call__ and
    # __init__ comes back from type etc.).
    #
    # This has the advantage over six.with_metaclass in that it does not
    # introduce dummy classes into the final MRO.
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('DummyMetaClass', None, {})

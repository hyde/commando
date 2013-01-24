from commando.conf import AutoProp, ConfigDict


class TestClass(AutoProp):

    @AutoProp.default
    def source(self):
        return 'source'


def test_auto():
    t = TestClass()
    assert t.source == 'source'


def test_override():
    t = TestClass()
    t.source = 'source1'
    assert t.source == 'source1'
    t.source = 'source2'
    assert t.source == 'source2'
    t.source = None
    assert t.source == 'source'


def test_init():
    c = ConfigDict({"a": 1})
    assert c.a == 1
    assert c["a"] == 1


def test_change():
    c = ConfigDict({"a": 1})
    assert c.a == 1
    c.a = 2
    assert c["a"] == 2


def test_two_levels():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    assert c.b.c == 3


def test_two_levels_assignment():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    d = {"d": 5}
    c.b = d
    assert c.b.d == 5
    assert c.b == d


def test_two_levels_patch():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    d = {"d": 5}
    c.b.d = d
    assert c.b.c == 3
    assert c.b.d == d


def test_copy():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    d = c.copy()
    assert c == d
    c.b.c = 4
    assert c != d


def test_list():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    c.d = [dict(e=1), dict(f=2)]
    assert c.d[0].e == 1
    assert c.d[1].f == 2


def test_operator():
    c = ConfigDict({"a": 1, "b": {"c": 3}})
    from operator import attrgetter
    assert attrgetter('b.c')(c) == 3


def test_patch_simple():
    c = ConfigDict({"a": 1, "b": {"c": 3, "e": 4}})
    d = {"b": {"e": 5}}
    c.patch(d)
    assert c.b.c == 3
    assert c.b.e == 5


def test_patch_complex():

    c = ConfigDict({
        "a": 1,
        "b": {"x": 3, "y": 4},
        "c": {"x": 5, "y": 6},
        "d": {"x": 7, "y": 8}
    })
    d = {"a": 2, "b": {"z": 5}, "c": [1, 2], "d": {"y": 9}}
    c.patch(d)
    assert c.a == 2
    assert c.b.x == 3
    assert c.b.y == 4
    assert c.b.z == 5
    assert c.c == [1, 2]
    assert c.d.x == 7
    assert c.d.y == 9

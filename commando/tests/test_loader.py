# -*- coding: utf-8 -*-
"""
Use nose
`$ pip install nose`
`$ nosetests`
"""

from commando.util import CommandoLoaderException, load_python_object
from nose.tools import raises
import os

from fswrap import File


def test_can_load_locals():

    file_class = load_python_object('fswrap.File')
    assert file_class

    f = file_class(__file__)
    assert f

    assert f.name == os.path.basename(__file__)


def test_can_load_from_python_path():

    markdown = load_python_object('markdown.markdown')
    assert markdown

    assert "<h3>h3</h3>" == markdown("### h3")

def test_can_load_module_without_dot():

    yaml = load_python_object('yaml')

    abc = yaml.load("""
        d: efg
        l: mno
    """)

    assert abc['d'] == 'efg'
    assert abc['l'] == 'mno'

@raises(CommandoLoaderException)
def test_exception_raised_for_invalid_module():
    load_python_object("junk.junk.junk")
    assert False

@raises(CommandoLoaderException)
def test_exception_raised_for_invalid_object():
    load_python_object("markdown.junk")
    assert False
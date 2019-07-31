# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
from __future__ import print_function, unicode_literals

from ... import base as nib
from ..traits_extension import rebase_path_traits, resolve_path_traits, Path


class _test_spec(nib.TraitedSpec):
    a = nib.File()
    b = nib.Tuple(nib.File(), nib.File())
    c = nib.traits.List(nib.File())
    d = nib.Either(nib.File(), nib.traits.Float())
    e = nib.OutputMultiObject(nib.File())
    ee = nib.OutputMultiObject(nib.Str)
    f = nib.traits.Dict(nib.Str, nib.File())
    g = nib.Either(nib.File, nib.Str)
    h = nib.Str
    i = nib.Either(nib.File, nib.Tuple(nib.File, nib.traits.Int))
    j = nib.Either(nib.File, nib.Tuple(nib.File, nib.traits.Int),
                   nib.traits.Dict(nib.Str, nib.File()))


def test_rebase_path_traits():
    """Check rebase_path_traits."""
    spec = _test_spec()

    a = rebase_path_traits(
        spec.trait('a'), '/some/path/f1.txt', '/some/path')
    assert a == Path('f1.txt')

    a = rebase_path_traits(
        spec.trait('a'), '/some/path/f1.txt', '/some/other/path')
    assert a == Path('/some/path/f1.txt')

    b = rebase_path_traits(
        spec.trait('b'), ('/some/path/f1.txt', '/some/path/f2.txt'), '/some/path')
    assert b == (Path('f1.txt'), Path('f2.txt'))

    c = rebase_path_traits(
        spec.trait('c'), ['/some/path/f1.txt', '/some/path/f2.txt', '/some/path/f3.txt'],
        '/some/path')
    assert c == [Path('f1.txt'), Path('f2.txt'), Path('f3.txt')]

    d = rebase_path_traits(
        spec.trait('d'), 2.0, '/some/path')
    assert d == 2.0

    d = rebase_path_traits(
        spec.trait('d'), '/some/path/either.txt', '/some/path')
    assert '%s' % d == 'either.txt'

    e = rebase_path_traits(
        spec.trait('e'), ['/some/path/f1.txt', '/some/path/f2.txt', '/some/path/f3.txt'],
        '/some/path')
    assert e == [Path('f1.txt'), Path('f2.txt'), Path('f3.txt')]

    e = rebase_path_traits(
        spec.trait('e'), [['/some/path/f1.txt', '/some/path/f2.txt'], [['/some/path/f3.txt']]],
        '/some/path')
    assert e == [[Path('f1.txt'), Path('f2.txt')], [[Path('f3.txt')]]]

    ee = rebase_path_traits(
        spec.trait('ee'), [['/some/path/f1.txt', '/some/path/f2.txt'], [['/some/path/f3.txt']]],
        '/some/path')
    assert ee == [['/some/path/f1.txt', '/some/path/f2.txt'], [['/some/path/f3.txt']]]

    f = rebase_path_traits(
        spec.trait('f'), {'1': '/some/path/f1.txt'}, '/some/path')
    assert f == {'1': Path('f1.txt')}

    g = rebase_path_traits(
        spec.trait('g'), 'some/path/either.txt', '/some/path')
    assert '%s' % g == 'some/path/either.txt'

    g = rebase_path_traits(
        spec.trait('g'), '/some/path/either.txt', '/some')
    assert '%s' % g == 'path/either.txt'

    g = rebase_path_traits(spec.trait('g'), 'string', '/some')
    assert '%s' % g == 'string'

    g = rebase_path_traits(spec.trait('g'), '2', '/some/path')
    assert g == '2'  # You dont want this one to be a Path

    h = rebase_path_traits(spec.trait('h'), '2', '/some/path')
    assert h == '2'

    i = rebase_path_traits(spec.trait('i'), '/some/path/either/file.txt', '/some/path')
    assert '%s' % i == 'either/file.txt'

    i = rebase_path_traits(spec.trait('i'), ('/some/path/either/tuple/file.txt', 2), '/some/path')
    assert ('%s' % i[0], i[1]) == ('either/tuple/file.txt', 2)

    j = rebase_path_traits(spec.trait('j'), '/some/path/either/file.txt', '/some/path')
    assert '%s' % j == 'either/file.txt'

    j = rebase_path_traits(spec.trait('j'), ('/some/path/either/tuple/file.txt', 2), '/some/path')
    assert ('%s' % j[0], j[1]) == ('either/tuple/file.txt', 2)

    j = rebase_path_traits(spec.trait('j'), {'a': '/some/path/either/dict/file.txt'},
                           '/some/path')
    assert j == {'a': Path('either/dict/file.txt')}


def test_resolve_path_traits():
    """Check resolve_path_traits."""
    spec = _test_spec()

    a = resolve_path_traits(
        spec.trait('a'), 'f1.txt', '/some/path')
    assert a == Path('/some/path/f1.txt')

    a = resolve_path_traits(
        spec.trait('a'), '/already/absolute/f1.txt', '/some/path')
    assert a == Path('/already/absolute/f1.txt')

    b = resolve_path_traits(
        spec.trait('b'), ('f1.txt', 'f2.txt'), '/some/path')
    assert b == (Path('/some/path/f1.txt'), Path('/some/path/f2.txt'))

    c = resolve_path_traits(
        spec.trait('c'), ['f1.txt', 'f2.txt', 'f3.txt'],
        '/some/path')
    assert c == [Path('/some/path/f1.txt'), Path('/some/path/f2.txt'), Path('/some/path/f3.txt')]

    d = resolve_path_traits(
        spec.trait('d'), 2.0, '/some/path')
    assert d == 2.0

    d = resolve_path_traits(
        spec.trait('d'), 'either.txt', '/some/path')
    assert '%s' % d == '/some/path/either.txt'

    e = resolve_path_traits(
        spec.trait('e'), ['f1.txt', 'f2.txt', 'f3.txt'],
        '/some/path')
    assert e == [Path('/some/path/f1.txt'), Path('/some/path/f2.txt'), Path('/some/path/f3.txt')]

    e = resolve_path_traits(
        spec.trait('e'), [['f1.txt', 'f2.txt'], [['f3.txt']]],
        '/some/path')
    assert e == [[Path('/some/path/f1.txt'), Path('/some/path/f2.txt')],
                 [[Path('/some/path/f3.txt')]]]

    f = resolve_path_traits(
        spec.trait('f'), {'1': 'path/f1.txt'}, '/some')
    assert f == {'1': Path('/some/path/f1.txt')}

    g = resolve_path_traits(
        spec.trait('g'), '/either.txt', '/some/path')
    assert g == Path('/either.txt')

    # This is a problematic case, it is impossible to know whether this
    # was meant to be a string or a file.
    # In this implementation, strings take precedence
    g = resolve_path_traits(
        spec.trait('g'), 'path/either.txt', '/some')
    assert g == 'path/either.txt'

    # This is a problematic case, it is impossible to know whether this
    # was meant to be a string or a file.
    g = resolve_path_traits(spec.trait('g'), 'string', '/some')
    assert g == 'string'

    # This is a problematic case, it is impossible to know whether this
    # was meant to be a string or a file.
    g = resolve_path_traits(spec.trait('g'), '2', '/some/path')
    assert g == '2'  # You dont want this one to be a Path

    h = resolve_path_traits(spec.trait('h'), '2', '/some/path')
    assert h == '2'

    ee = resolve_path_traits(
        spec.trait('ee'), [['f1.txt', 'f2.txt'], [['f3.txt']]],
        '/some/path')
    assert ee == [['f1.txt', 'f2.txt'], [['f3.txt']]]

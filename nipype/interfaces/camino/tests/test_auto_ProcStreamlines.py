# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import ProcStreamlines


def test_ProcStreamlines_inputs():
    input_map = dict(allowmultitargets=dict(argstr='-allowmultitargets',
    ),
    args=dict(argstr='%s',
    ),
    datadims=dict(argstr='-datadims %s',
    units='voxels',
    ),
    directional=dict(argstr='-directional %s',
    units='NA',
    ),
    discardloops=dict(argstr='-discardloops',
    ),
    endpointfile=dict(argstr='-endpointfile %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    exclusionfile=dict(argstr='-exclusionfile %s',
    ),
    gzip=dict(argstr='-gzip',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-inputfile %s',
    mandatory=True,
    position=1,
    ),
    inputmodel=dict(argstr='-inputmodel %s',
    usedefault=True,
    ),
    iterations=dict(argstr='-iterations %d',
    units='NA',
    ),
    maxtractlength=dict(argstr='-maxtractlength %d',
    units='mm',
    ),
    maxtractpoints=dict(argstr='-maxtractpoints %d',
    units='NA',
    ),
    mintractlength=dict(argstr='-mintractlength %d',
    units='mm',
    ),
    mintractpoints=dict(argstr='-mintractpoints %d',
    units='NA',
    ),
    noresample=dict(argstr='-noresample',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    outputacm=dict(argstr='-outputacm',
    requires=['outputroot', 'seedfile'],
    ),
    outputcbs=dict(argstr='-outputcbs',
    requires=['outputroot', 'targetfile', 'seedfile'],
    ),
    outputcp=dict(argstr='-outputcp',
    requires=['outputroot', 'seedfile'],
    ),
    outputroot=dict(argstr='-outputroot %s',
    ),
    outputsc=dict(argstr='-outputsc',
    requires=['outputroot', 'seedfile'],
    ),
    outputtracts=dict(argstr='-outputtracts',
    ),
    regionindex=dict(argstr='-regionindex %d',
    units='mm',
    ),
    resamplestepsize=dict(argstr='-resamplestepsize %d',
    units='NA',
    ),
    seedfile=dict(argstr='-seedfile %s',
    ),
    seedpointmm=dict(argstr='-seedpointmm %s',
    units='mm',
    ),
    seedpointvox=dict(argstr='-seedpointvox %s',
    units='voxels',
    ),
    targetfile=dict(argstr='-targetfile %s',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    truncateinexclusion=dict(argstr='-truncateinexclusion',
    ),
    truncateloops=dict(argstr='-truncateloops',
    ),
    voxeldims=dict(argstr='-voxeldims %s',
    units='mm',
    ),
    waypointfile=dict(argstr='-waypointfile %s',
    ),
    )
    inputs = ProcStreamlines.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ProcStreamlines_outputs():
    output_map = dict(outputroot_files=dict(),
    proc=dict(),
    )
    outputs = ProcStreamlines.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

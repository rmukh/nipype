# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..qt1 import FitQt1


def test_FitQt1_inputs():
    input_map = dict(acceptance=dict(argstr='-acceptance %f',
    ),
    args=dict(argstr='%s',
    ),
    b1map=dict(argstr='-b1map %s',
    ),
    comp_file=dict(argstr='-comp %s',
    name_source=['source_file'],
    name_template='%s_comp.nii.gz',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    error_file=dict(argstr='-error %s',
    name_source=['source_file'],
    name_template='%s_error.nii.gz',
    ),
    flips=dict(argstr='-flips %s',
    sep=' ',
    ),
    flips_list=dict(argstr='-fliplist %s',
    ),
    gn_flag=dict(argstr='-gn',
    position=8,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    ir_flag=dict(argstr='-IR',
    position=13,
    ),
    lm_val=dict(argstr='-lm %f %f',
    position=7,
    ),
    m0map_file=dict(argstr='-m0map %s',
    name_source=['source_file'],
    name_template='%s_m0map.nii.gz',
    ),
    mask=dict(argstr='-mask %s',
    position=2,
    ),
    maxit=dict(argstr='-maxit %d',
    position=11,
    ),
    mcmap_file=dict(argstr='-mcmap %s',
    name_source=['source_file'],
    name_template='%s_mcmap.nii.gz',
    ),
    mcmaxit=dict(argstr='-mcmaxit %d',
    ),
    mcout=dict(argstr='-mcout %s',
    ),
    mcsamples=dict(argstr='-mcsamples %d',
    ),
    nb_comp=dict(argstr='-nc %d',
    position=6,
    ),
    prior=dict(argstr='-prior %s',
    position=3,
    ),
    res_file=dict(argstr='-res %s',
    name_source=['source_file'],
    name_template='%s_res.nii.gz',
    ),
    slice_no=dict(argstr='-slice %d',
    position=9,
    ),
    source_file=dict(argstr='-source %s',
    mandatory=True,
    position=1,
    ),
    spgr=dict(argstr='-SPGR',
    ),
    sr_flag=dict(argstr='-SR',
    position=12,
    ),
    syn_file=dict(argstr='-syn %s',
    name_source=['source_file'],
    name_template='%s_syn.nii.gz',
    ),
    t1_list=dict(argstr='-T1list %s',
    ),
    t1map_file=dict(argstr='-t1map %s',
    name_source=['source_file'],
    name_template='%s_t1map.nii.gz',
    ),
    t1max=dict(argstr='-T1max %f',
    ),
    t1min=dict(argstr='-T1min %f',
    ),
    te_value=dict(argstr='-TE %f',
    position=4,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    tis=dict(argstr='-TIs %s',
    position=14,
    sep=' ',
    ),
    tis_list=dict(argstr='-TIlist %s',
    ),
    tr_value=dict(argstr='-TR %f',
    position=5,
    ),
    voxel=dict(argstr='-voxel %d %d %d',
    position=10,
    ),
    )
    inputs = FitQt1.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FitQt1_outputs():
    output_map = dict(comp_file=dict(),
    error_file=dict(),
    m0map_file=dict(),
    mcmap_file=dict(),
    res_file=dict(),
    syn_file=dict(),
    t1map_file=dict(),
    )
    outputs = FitQt1.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

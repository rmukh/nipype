# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import FixTopology


def test_FixTopology_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        copy_inputs=dict(mandatory=True,),
        environ=dict(nohash=True, usedefault=True,),
        ga=dict(argstr="-ga",),
        hemisphere=dict(argstr="%s", mandatory=True, position=-1,),
        in_brain=dict(extensions=None, mandatory=True,),
        in_inflated=dict(extensions=None, mandatory=True,),
        in_orig=dict(extensions=None, mandatory=True,),
        in_wm=dict(extensions=None, mandatory=True,),
        mgz=dict(argstr="-mgz",),
        seed=dict(argstr="-seed %d",),
        sphere=dict(argstr="-sphere %s", extensions=None,),
        subject_id=dict(argstr="%s", mandatory=True, position=-2, usedefault=True,),
        subjects_dir=dict(),
    )
    inputs = FixTopology.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FixTopology_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = FixTopology.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

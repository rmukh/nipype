# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import AddNoise


def test_AddNoise_inputs():
    input_map = dict(
        bg_dist=dict(mandatory=True, usedefault=True,),
        dist=dict(mandatory=True, usedefault=True,),
        in_file=dict(extensions=None, mandatory=True,),
        in_mask=dict(extensions=None,),
        out_file=dict(extensions=None,),
        snr=dict(usedefault=True,),
    )
    inputs = AddNoise.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AddNoise_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = AddNoise.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import MNIBiasCorrection


def test_MNIBiasCorrection_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    distance=dict(argstr='--distance %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--i %s',
    mandatory=True,
    ),
    iterations=dict(argstr='--n %d',
    ),
    mask=dict(argstr='--mask %s',
    mandatory=False,
    ),
    no_rescale=dict(argstr='--no-rescale',
    ),
    out_file=dict(argstr='--o %s',
    hash_files=False,
    keep_extension=True,
    mandatory=False,
    name_source=['in_file'],
    name_template='%s_output',
    ),
    protocol_iterations=dict(argstr='--proto-iters %d',
    ),
    shrink=dict(argstr='--shrink %d',
    mandatory=False,
    ),
    stop=dict(argstr='--stop %f',
    mandatory=False,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    transform=dict(argstr='--uchar %s',
    mandatory=False,
    ),
    )
    inputs = MNIBiasCorrection.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_MNIBiasCorrection_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = MNIBiasCorrection.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

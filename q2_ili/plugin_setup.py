# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_ili
from ._plot import plot
from ._semantics import STLDirFmt, Model
from qiime2.plugin import Plugin, Metadata, Citations


plugin = Plugin(
    name='ili',
    version=q2_ili.__version__,
    website='https://ili.embl.de/',
    citations=Citations.load('citations.bib', package='q2_ili'),
    package='q2_ili',
    description=('This QIIME 2 plugin wraps `ili and '
                 'supports interactive visualization of 3D models'),
    short_description='Plugin for spatial mapping with `ili'
)

# type registration
plugin.register_views(STLDirFmt)
plugin.register_semantic_types(Model)
plugin.register_semantic_type_to_format(Model, artifact_format=STLDirFmt)


plugin.visualizers.register_function(
    function=plot,
    inputs={'model': Model},
    parameters={'metadata': Metadata},
    input_descriptions={
        'model': 'The model where the data will be plotted.'
    },
    parameter_descriptions={'metadata': 'Metadata used to color the model'},
    name='Visualize and interact with 3D models',
    description='Visualize and interact with 3D models colored using metadata'
)

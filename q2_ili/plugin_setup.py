# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_ili
from ._plot import plot, procrustes_plot, biplot

from qiime2.plugin import (Plugin, Metadata, Str, Citations, List, Range, Int,
                           Properties)
from q2_types.ordination import PCoAResults

PARAMETERS = {'metadata': Metadata, 'custom_axes': List[Str]}
PARAMETERS_DESC = {
    'metadata': 'The sample metadata.',
    'custom_axes': ('Numeric sample metadata columns that should be '
                    'included as axes in the ili plot.')
}

plugin = Plugin(
    name='ili',
    version=q2_ili.__version__,
    website='https://ili.embl.de/',
    citations=Citations.load('citations.bib', package='q2_ili'),
    package='q2_ili',
    description=('This QIIME 2 plugin wraps ili and '
                 'supports interactive visualization of 3D models'),
    short_description='Plugin spatial mapping with ili.'
)

plugin.visualizers.register_function(
    function=plot,
    inputs={'model': PCoAResults},
    parameters={'metadata': Metadata},
    input_descriptions={
        'pcoa': 'The principal coordinates matrix to be plotted.'
    },
    parameter_descriptions=PARAMETERS_DESC,
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generates an interactive ordination plot where the user '
                'can visually integrate sample metadata.'
)

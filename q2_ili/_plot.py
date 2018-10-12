# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources

import qiime2
import skbio
import q2templates

TEMPLATES = pkg_resources.resource_filename('q2_ili', 'assets')


def _generic_plot(output_dir: str, master: skbio.OrdinationResults,
                  metadata: qiime2.Metadata,
                  other_pcoa: skbio.OrdinationResults, plot_name,
                  custom_axes: str=None,
                  feature_metadata: qiime2.Metadata=None):

    mf = metadata.to_dataframe()

    if other_pcoa is None:
        procrustes = None
    else:
        procrustes = [other_pcoa]

    viz = ili(master, mf, feature_mapping_file=feature_metadata,
                  procrustes=procrustes, remote='.')

    if custom_axes is not None:
        viz.custom_axes = custom_axes

    if other_pcoa:
        viz.procrustes_names = ['reference', 'other']

    html = viz.make_ili(standalone=True)
    viz.copy_support_files(output_dir)
    with open(os.path.join(output_dir, 'ili.html'), 'w') as fh:
        fh.write(html)

    index = os.path.join(TEMPLATES, 'index.html')
    q2templates.render(index, output_dir, context={'plot_name': plot_name})


def plot(output_dir: str, pcoa: skbio.OrdinationResults,
         metadata: qiime2.Metadata, custom_axes: str=None) -> None:
    _generic_plot(output_dir, master=pcoa, metadata=metadata, other_pcoa=None,
                  custom_axes=custom_axes, plot_name='plot')

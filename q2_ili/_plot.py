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

from ._semantics import STLDirFmt

from distutils.dir_util import copy_tree
from shutil import copyfile


ASSETS = pkg_resources.resource_filename('q2_ili', 'assets')


def plot(output_dir: str, model: STLDirFmt,
         metadata: qiime2.Metadata) -> None:
    mf = metadata.to_dataframe()

    ili_path = os.path.join(ASSETS, 'ili')

    # copy the ili contents into the output folder
    copy_tree(ili_path, output_dir)

    stl = os.path.join(str(model.path), 'model.stl')

    # we save the data to the workers folder since that's where the files are
    # loaded from, and to avoid requests to external sites, etc.
    mf.to_csv(os.path.join(output_dir, 'js/workers', 'features.csv'))
    copyfile(stl, os.path.join(output_dir, 'js/workers', 'model.stl'))

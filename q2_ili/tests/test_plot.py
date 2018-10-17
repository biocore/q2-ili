# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import tempfile
import unittest

import pandas as pd
import qiime2 as q2


from q2_ili import plot, STLDirFmt


class PlotTests(unittest.TestCase):
    def setUp(self):
        # avoid including an STL model in the repo since we only really need
        # to test that the copying works of the directory's contents work
        self.data = tempfile.TemporaryDirectory()
        with open(os.path.join(self.data.name, 'model.stl'), 'w') as f:
            f.write('Not the STL file you are looking for')

        self.model = STLDirFmt(path=self.data.name, mode='r')
        self.metadata = q2.Metadata(
            pd.DataFrame({'val1': ['1.0', '2.0', '3.0', '4.0'],
                          'val2': ['3.3', '3.5', '3.6', '3.9']},
                         index=pd.Index(['A', 'B', 'C', 'D'], name='id')))

    def tearDown(self):
        self.data.cleanup()

    def test_plot(self):
        with tempfile.TemporaryDirectory() as output_dir:
            plot(output_dir, self.model, self.metadata)
            index_fp = os.path.join(output_dir, 'index.html')

            # check the base HTML is copied
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('Spatial Data Mapping' in open(index_fp).read())

            model_fp = os.path.join(output_dir, 'js', 'workers', 'model.stl')
            metadata_fp = os.path.join(output_dir, 'js', 'workers',
                                       'features.csv')
            # check the metadata and the model are properly copied
            self.assertTrue(os.path.exists(model_fp))
            self.assertTrue(os.path.exists(metadata_fp))

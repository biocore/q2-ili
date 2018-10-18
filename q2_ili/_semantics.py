# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import qiime2.plugin.model as model
from qiime2.plugin import SemanticType


class STLFile(model.TextFileFormat):
    def sniff(self):
        # we don't really parse this file
        return True


STLDirFmt = model.SingleFileDirectoryFormat('STLFile', 'model.stl', STLFile)
Model = SemanticType('Model')

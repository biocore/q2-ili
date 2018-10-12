# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_ili.plugin_setup import plugin as ili_plugin


class PluginSetupTests(unittest.TestCase):

    def test_plugin_setup(self):
        self.assertEqual(ili_plugin.name, 'ili')

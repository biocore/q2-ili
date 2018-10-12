# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, q2-ili development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
import versioneer

setup(
    name="q2-ili",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Yoshiki Vazquez-Baeza",
    author_email="yoshiki@ucsd.edu",
    description="Display ordination plots",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-ili=q2_ili.plugin_setup:plugin']
    },
    package_data={'q2_ili': ['assets/index.html', 'citations.bib']},
    zip_safe=False,
)

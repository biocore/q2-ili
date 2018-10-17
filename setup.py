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
    description="Display 3D models",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-ili=q2_ili.plugin_setup:plugin']
    },
    package_data={'q2_ili': ['assets/index.html', 'citations.bib'
                             'assets/ili/*.js', 'assets/ili/*.html',
                             'assets/ili/*.css', 'assets/ili/*.json',
                             'assets/ili/img/*.png', 'assets/ili/js/*.js',
                             'assets/ili/workers/*.js', 'assets/ili/lib/*.js',
                             'assets/ili/emperor/*.js',
                             'assets/ili/img/bootstrap-colorpicker/*.png',
                             'assets/ili/css/*.css', 'assets/ili/fonts/*.ttf',
                             'assets/ili/fonts/*.woff',
                             'assets/ili/fonts/*.woff2',
                             'assets/ili/images/*.png',
                             ]},
    zip_safe=False,
)

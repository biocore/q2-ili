# QIIME 2 \`ili plugin

[![Build Status](https://travis-ci.org/biocore/q2-ili.svg?branch=master)](https://travis-ci.org/biocore/q2-ili) [![Coverage Status](https://coveralls.io/repos/github/biocore/q2-ili/badge.svg?branch=master)](https://coveralls.io/github/biocore/q2-ili?branch=master)

This is a QIIME 2 plugin. For details on QIIME 2, see https://qiime2.org.

This plugin is wrapping \`ili, for more information, see https://github.com/MolecularCartography/ili.

# Installation

To install `q2-ili` you need a working QIIME 2 installation. After you have
installed QIIME 2, clone and install `q2-ili` by running these commands:

```bash
git clone --recurse-submodules https://github.com/biocore/q2-ili.git && cd q2-ili
pip install .
qiime dev refresh-cache
```

## Troubleshooting installation

If the `git` command above results in an error like the following:

```bash
error: Server does not allow request for unadvertised object...
```

you may need to update the version of `git` that is installed on your system. You can download the latest version of git [here](https://git-scm.com/downloads). 

# Requirements

In order to use this plugin, you need a 3D model in STL format and a mapping
between your samples and their coordinate locations in the model. To do this
your QIIME 2 metadata file needs to include three columns labeled `x`, `y` and
`z`. For more information see [\`ili's
documentation](https://github.com/MolecularCartography/ili).

# Example

To exemplify how to use `q2-ili`, we will use the data from [Bouslimani et al.
2015](http://www.pnas.org/content/112/17/E2120). The metabolomic features will
be colored in the model according to the site where they were collected from.
The data for this example is included in the `example-data` directory of the
repository you cloned above.

First we need to import the model as a QIIME2 artifact. The type `Model` is
installed in QIIME 2 along with this plugin, hence we can run the following
command:

```bash
qiime tools import \
--type Model \
--input-path example-data/model.stl \
--output-path model.qza
```

Next, we generate the visualization using the model and the numeric data that
we have in the metadata file:

```bash
qiime ili plot \
--i-model model.qza \
--m-metadata-file example-data/metadata.tsv \
--o-visualization visualization.qzv
```

Lastly, you can visualize and interact with this model using
[q2view](https://view.qiime2.org).

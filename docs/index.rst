``alignparse`` documentation
===================================================

``alignparse`` is a Python package written by `the Bloom lab <https://research.fhcrc.org/bloom/en.html>`_.
It is designed to align long sequencing reads (such as those from PacBio circular consensus sequencing) to `targets`, filter these alignments based on user-provided specifications, and parse out user-defined sequence `features`. 

For each read that passes the user-defined filters, the user can define what information about each feature (e.g. sequence, mutations, and sequencing accuracy) should be retained for further analyses. The `alignparse.consensus` module provides tools for such further analyses, including analyzing mutations identified in sequence features and defining consensus sequences from barcoded sequencing reads.

See below for information and examples of how to use this package.

Contents
----------
.. toctree::
   :hidden:

   self

.. toctree::
   :maxdepth: 2

   installation
   examples
   alignparse
   package_index
   acknowledgments
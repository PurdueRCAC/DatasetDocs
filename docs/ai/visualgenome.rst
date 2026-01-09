visualgenome
============

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/visualgenome``
   * - **Discipline**
     - AI / computer vision / multimodel AI
   * - **DOI**
     - `10.1007/s11263-016-0981-7 <https://doi.org/10.1007/s11263-016-0981-7>`__
   * - **Link**
     - `Access Data <https://homes.cs.washington.edu/~ranjay/visualgenome/api.html>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2017-02-06
   * - **Downloaded**
     - 2026-01-07
   * - **Data Type**
     - LMDB, SquashFS, Extracted JPG files on Ceph
   * - **Dataset Size**
     - 21G (extracted)
   * - **Number of Files**
     - 108,265 (extracted)
   * - **Usage Policy Link**
     - http://creativecommons.org/licenses/by/4.0

Description
-----------
Visual Genome is a dataset, a knowledge base, an ongoing effort to connect structured image concepts to language.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/visualgenome/2017-02-06

Usage Policy
------------
This dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Users may use, share, adapt, and redistribute the data with appropriate credit to the dataset authors and hosting repository. A link to the license must be included (https://creativecommons.org/licenses/by/4.0/), and any modifications should be clearly indicated. Users are responsible for ensuring that the dataset is appropriate for their applications.

See also: http://creativecommons.org/licenses/by/4.0

Citation
--------
Krishna, R., Zhu, Y., Groth, O. et al. Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations. Int J Comput Vis 123, 32–73 (2017). https://doi.org/10.1007/s11263-016-0981-7

BibTeX
------
.. code-block:: bibtex

   @article{Krishna2017,
     author  = {Krishna, Ranjay and Zhu, Yuke and Groth, Oliver and Johnson, Justin and Hata, Kenji and Kravitz, Joshua and Chen, Stephanie and Kalantidis, Yannis and Li, Li-Jia and Shamma, David A. and Bernstein, Michael S. and Fei-Fei, Li},
     title   = {Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations},
     journal = {International Journal of Computer Vision},
     volume  = {123},
     number  = {1},
     pages   = {32--73},
     year    = {2017},
     month   = {5},
     doi     = {10.1007/s11263-016-0981-7},
     url     = {https://doi.org/10.1007/s11263-016-0981-7},
     issn    = {1573-1405},
     abstract = {Despite progress in perceptual tasks such as image classification, computers still perform poorly on cognitive tasks such as image description and question answering. Cognition is core to tasks that involve not just recognizing, but reasoning about our visual world. However, models used to tackle the rich content in images for cognitive tasks are still being trained using the same datasets designed for perceptual tasks. To achieve success at cognitive tasks, models need to understand the interactions and relationships between objects in an image. In this paper, we present the Visual Genome dataset to enable the modeling of such relationships. We collect dense annotations of objects, attributes, and relationships within each image. Specifically, the dataset contains over 108K images where each image has an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects.}
   }

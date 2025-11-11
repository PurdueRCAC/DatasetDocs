COCO
====

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/coco``
   * - **Discipline**
     - AI / Object Segmentation / Object Detection
   * - **DOI**
     - `10.48550/arXiv.1405.0312 <https://doi.org/10.48550/arXiv.1405.0312>`__
   * - **Link**
     - `Access Data <https://cocodataset.org/#download>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2017
   * - **Downloaded**
     - 2025-11-09
   * - **Data Type**
     - LMDB, SquashFS\nExtracted files on Ceph
   * - **Dataset Size**
     - 30G (extracted)
   * - **Number of Files**
     - 410544 (extracted)
   * - **Usage Policy Link**
     - https://creativecommons.org/licenses/by/4.0/legalcode

Description
-----------
COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features: \nObject segmentation\nRecognition in context\nSuperpixel stuff segmentation\n330K images (>200K labeled)\n1.5 million object instances\n80 object categories\n91 stuff categories\n5 captions per image\n250,000 people with keypoints\n\n This dataset includes train/

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/coco/2017

Usage Policy
------------

See also: https://creativecommons.org/licenses/by/4.0/legalcode

Citation
--------
Lin, T.-Y., Maire, M., Belongie, S., Bourdev, L., Girshick, R., Hays, J., Perona, P., Ramanan, D., Zitnick, C. L., & Dollár, P. (2015). Microsoft COCO: Common objects in context. arXiv preprint arXiv:1405.0312. https://arxiv.org/abs/1405.0312

BibTeX
------
.. code-block:: bibtex

   @misc{lin2015microsoftcococommonobjects,
         title={Microsoft COCO: Common Objects in Context}, 
         author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
         year={2015},
         eprint={1405.0312},
         archivePrefix={arXiv},
         primaryClass={cs.CV},
         url={https://arxiv.org/abs/1405.0312}, 
   }

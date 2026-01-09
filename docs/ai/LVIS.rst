LVIS
====

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/LVIS``
   * - **Discipline**
     - AI / computer vision / Segmentation
   * - **DOI**
     - `10.48550/arXiv.1908.03195 <https://doi.org/10.48550/arXiv.1908.03195>`__
   * - **Link**
     - `Access Data <https://www.lvisdataset.org/dataset>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2019-08-08
   * - **Downloaded**
     - 2026-01-07
   * - **Data Type**
     - LMDB, SquashFS, Extracted JPG files on Ceph
   * - **Dataset Size**
     - 33G (extracted)
   * - **Number of Files**
     - 204631 (extracted)
   * - **Usage Policy Link**
     - https://creativecommons.org/licenses/by/4.0/

Description
-----------
Progress on object detection is enabled by datasets that focus the research community's attention on open challenges. This process led us from simple images to complex scenes and from bounding boxes to segmentation masks. LVIS is ~2 million high-quality instance segmentation masks for over 1000 entry-level object categories in 164k images. Due to the Zipfian distribution of categories in natural images, LVIS naturally has a long tail of categories with few training samples. Given that state-of-the-art deep learning methods for object detection perform poorly in the low-sample regime, we believe that our dataset poses an important and exciting new scientific challenge.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/LVIS/2019-08-08

Usage Policy
------------
The LVIS annotations along with this website are licensed under a Creative Commons Attribution 4.0 License. All LVIS dataset images come from the COCO dataset which those are licensed under Creative Commons Attribution 4.0 License.

See also: https://creativecommons.org/licenses/by/4.0/

Citation
--------
Gupta, A., Dollar, P., & Girshick, R. (2019). LVIS: A dataset for large vocabulary instance segmentation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (pp. 5356–5364).

BibTeX
------
.. code-block:: bibtex

   @inproceedings{gupta2019lvis,
     title={LVIS: A Dataset for Large Vocabulary Instance Segmentation},
     author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},
     booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},
     year={2019}
   }

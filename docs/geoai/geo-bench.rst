geo-bench
=========

:doc:`← Back to geoai <../geoai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/geoai/geo-bench-1.0``
   * - **Discipline**
     - GeoAI / Remote Sensing / Environmental Science
   * - **DOI**
     - `10.48550/arXiv.2306.03831 <https://doi.org/10.48550/arXiv.2306.03831>`__
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/recursix/geo-bench-1.0/tree/main>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2024-01-15
   * - **Downloaded**
     - 2025-09-10
   * - **Data Type**
     - ZIP
   * - **Dataset Size**
     - 33G
   * - **Number of Files**
     - 90
   * - **Usage Policy Link**
     - https://choosealicense.com/licenses/cc-by-sa-4.0/

Description
-----------
GEO-Bench: Toward Foundation Models for Earth Monitoring. Recent progress in self-supervision has shown that pre-training large neural networks on vast amounts of unsupervised data can lead to substantial increases in generalization to downstream tasks. Such models, recently coined foundation models, have been transformational to the field of natural language processing. Variants have also been proposed for image data, but their applicability to remote sensing tasks is limited. To stimulate the development of foundation models for Earth monitoring, we propose a benchmark comprised of six classification and six segmentation tasks, which were carefully curated and adapted to be both relevant to the field and well-suited for model evaluation. We accompany this benchmark with a robust methodology for evaluating models and reporting aggregated results to enable a reliable assessment of progress. Finally, we report results for 20 baselines to gain information about the performance of existing models. We believe that this benchmark will be a driver of progress across a variety of Earth monitoring tasks.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load geoai/geo-bench-1.0/2024-01-15

Usage Policy
------------
This dataset is released under the Creative Commons Attribution–ShareAlike 4.0 International (CC BY-SA 4.0) license. You may use, adapt, and build upon the data for research, educational, and commercial purposes, provided that appropriate credit is given to the original authors and source materials, including citation of the associated paper and DOI. Any derivative works must be shared under the same CC BY-SA 4.0 terms, and users must clearly indicate if changes were made. Use of this dataset is subject to applicable legal and ethical guidelines, and no warranty is provided. Please consult the LICENSE file or official license page for full license terms.

See also: https://choosealicense.com/licenses/cc-by-sa-4.0/

Citation
--------
Lacoste, A., Lehmann, N., Rodriguez, P., Sherwin, E. D., Kerner, H., Lütjens, B., Irvin, J. A., Dao, D., Alemohammad, H., Drouin, A., Gunturkun, M., Huang, G., Vazquez, D., Newman, D., Bengio, Y., Ermon, S., & Zhu, X. X. (2023). GEO-Bench: Toward foundation models for Earth monitoring. arXiv preprint arXiv:2306.03831. https://arxiv.org/abs/2306.03831

BibTeX
------
.. code-block:: bibtex

   @misc{lacoste2023geobenchfoundationmodelsearth,
         title={GEO-Bench: Toward Foundation Models for Earth Monitoring}, 
         author={Alexandre Lacoste and Nils Lehmann and Pau Rodriguez and Evan David Sherwin and Hannah Kerner and Björn Lütjens and Jeremy Andrew Irvin and David Dao and Hamed Alemohammad and Alexandre Drouin and Mehmet Gunturkun and Gabriel Huang and David Vazquez and Dava Newman and Yoshua Bengio and Stefano Ermon and Xiao Xiang Zhu},
         year={2023},
         eprint={2306.03831},
         archivePrefix={arXiv},
         primaryClass={cs.LG},
         url={https://arxiv.org/abs/2306.03831}, 
   }

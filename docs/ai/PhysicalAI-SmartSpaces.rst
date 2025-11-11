PhysicalAI-SmartSpaces
======================

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/huggingface/nvidia/PhysicalAI-SmartSpaces``
   * - **Discipline**
     - AI / Computer Vision / PhysicalAI
   * - **DOI**
     - `10.48550/arXiv.2412.00692 <https://doi.org/10.48550/arXiv.2412.00692>`__
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2024
   * - **Downloaded**
     - 2025-11-09
   * - **Data Type**
     - LMDB, SquashFS\nExtracted MP4 files on Ceph
   * - **Dataset Size**
     - 6.7M (extracted)
   * - **Number of Files**
     - 3192 (extracted)
   * - **Usage Policy Link**
     - https://choosealicense.com/licenses/cc-by-4.0/

Description
-----------
Comprehensive, annotated dataset for multi-camera tracking and 2D/3D object detection. This dataset is synthetically generated with Omniverse.\n\nThis dataset consists of over 250 hours of video from across nearly 1,500 cameras from indoor scenes in warehouses, hospitals, retail, and more. The dataset is time synchronized for tracking humans across multiple cameras using feature representation and no personal data.\n\nDataset Description\nDataset Owner(s)\nNVIDIA\n\nDataset Creation Date\nWe started to create this dataset in December, 2023. First version was completed and released as part of 8th AI City Challenge in conjunction with CVPR 2024.\n\nDataset Characterization\nData Collection Method: Synthetic\nLabeling Method: Automatic with IsaacSim\nVideo Format\nVideo Standard: MP4 (H.264)\nVideo Resolution: 1080p\nVideo Frame rate: 30 FPS

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/huggingface/nvidia/PhysicalAI-SmartSpaces/2024

Usage Policy
------------

See also: https://choosealicense.com/licenses/cc-by-4.0/

Citation
--------
Tang, Z., Wang, S., Anastasiu, D. C., Chang, M.-C., Sharma, A., Kong, Q., Kobori, N., Gochoo, M., Batnasan, G., Otgonbold, M.-E., Alnajjar, F., Hsieh, J.-W., Kornuta, T., Li, X., Zhao, Y., Zhang, H., Radhakrishnan, S., Jain, A., Kumar, R., Murali, V. N., Wang, Y., Pusegaonkar, S. S., Wang, Y., Biswas, S., Wu, X., Zheng, Z., Chakraborty, P., & Chellappa, R. (2025). The 9th AI City Challenge. In Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) (pp. 5467–5476). Honolulu, HI, USA. \n\nWang, S., Anastasiu, D. C., Tang, Z., Chang, M.-C., Yao, Y., Zheng, L., Rahman, M. S., Arya, M. S., Sharma, A., Chakraborty, P., Prajapati, S., Kong, Q., Kobori, N., Gochoo, M., Otgonbold, M.-E., Batnasan, G., Alnajjar, F., Chen, P.-Y., Hsieh, J.-W., Wu, X., Pusegaonkar, S. S., Wang, Y., Biswas, S., & Chellappa, R. (2024). The 8th AI City Challenge. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) (pp. 7261–7272). Seattle, WA, USA. \n\nWang, Y., Meinhardt, T., Cetintas, O., Yang, C.-Y., Pusegaonkar, S. S., Missaoui, B., Biswas, S., Tang, Z., & Leal-Taixé, L. (2024). MCBLT: Multi-camera multi-object 3D tracking in long videos. arXiv preprint arXiv:2412.00692.

BibTeX
------
.. code-block:: bibtex

   @InProceedings{Tang25AICity25,
   author = {Zheng Tang and Shuo Wang and David C. Anastasiu and Ming-Ching Chang and Anuj Sharma and Quan Kong and Norimasa Kobori and Munkhjargal Gochoo and Ganzorig Batnasan and Munkh-Erdene Otgonbold and Fady Alnajjar and Jun-Wei Hsieh and Tomasz Kornuta and Xiaolong Li and Yilin Zhao and Han Zhang and Subhashree Radhakrishnan and Arihant Jain and Ratnesh Kumar and Vidya N. Murali and Yuxing Wang and Sameer Satish Pusegaonkar and Yizhou Wang and Sujit Biswas and Xunlei Wu and Zhedong Zheng and Pranamesh Chakraborty and Rama Chellappa},
   title = {The 9th AI City Challenge},
   booktitle = {Proc. ICCV Workshops},
   pages = {5467--5476},
   address = {Honolulu, HI, USA},
   year = {2025}
   }
   
   @inproceedings{Wang24AICity24,
   author = {Shuo Wang and David C. Anastasiu and Zheng Tang and Ming-Ching Chang and Yue Yao and Liang Zheng and Mohammed Shaiqur Rahman and Meenakshi S. Arya and Anuj Sharma and Pranamesh Chakraborty and Sanjita Prajapati and Quan Kong and Norimasa Kobori and Munkhjargal Gochoo and Munkh-Erdene Otgonbold and Ganzorig Batnasan and Fady Alnajjar and Ping-Yang Chen and Jun-Wei Hsieh and Xunlei Wu and Sameer Satish Pusegaonkar and Yizhou Wang and Sujit Biswas and Rama Chellappa},
   title = {The 8th AI City Challenge},
   booktitle = {Proc. CVPR Workshops},
   pages = {7261--7272},
   address = {Seattle, WA, USA},
   year = {2024}
   }
   
   @misc{Wang24MCBLT,
   author = {Yizhou Wang and Tim Meinhardt and Orcun Cetintas and Cheng-Yen Yang and Sameer Satish Pusegaonkar and Benjamin Missaoui and Sujit Biswas and Zheng Tang and Laura Leal-Taix{\'e}},
   title = {MCBLT: Multi-Camera Multi-Object 3D Tracking in Long Videos},
   note = {arXiv:2412.00692},
   year = {2024}
   }

PhysicalAI-Robotics-GR00T-X-Embodiment-Sim
==========================================

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/huggingface/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim``
   * - **Discipline**
     - AI / PhysicalAI / Robotics
   * - **DOI**
     - `10.48550/arXiv.2503.14734 <https://doi.org/10.48550/arXiv.2503.14734>`__
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2025-03-18
   * - **Downloaded**
     - 2025-11-09
   * - **Data Type**
     - LMDB, SquashFS\nExtracted LeRobot files on Ceph
   * - **Dataset Size**
     - 686M (extracted)
   * - **Number of Files**
     - 843233 (extracted)
   * - **Usage Policy Link**
     - https://choosealicense.com/licenses/cc-by-4.0/

Description
-----------
A set of datasets used for post-training of GR00T N1. Each dataset is a collection of trajectories from different robot embodiments and tasks.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/huggingface/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim/2025-03-18

Usage Policy
------------

See also: https://choosealicense.com/licenses/cc-by-4.0/

Citation
--------
NVIDIA, Bjorck, J., Castañeda, F., Cherniadev, N., Da, X., Ding, R., Fan, L., Fang, Y., Fox, D., Hu, F., Huang, S., Jang, J., Jiang, Z., Kautz, J., Kundalia, K., Lao, L., Li, Z., Lin, Z., Lin, K., … Zhu, Y. (2025, March). GR00T N1: An open foundation model for generalist humanoid robots [Preprint]. arXiv. https://arxiv.org/abs/2503.14734

BibTeX
------
.. code-block:: bibtex

   @inproceedings{gr00tn1_2025,
     archivePrefix = {arxiv},
     eprint     = {2503.14734},
     title      = {GR00T N1: An Open Foundation Model for Generalist Humanoid Robots},
     author     = {NVIDIA and Johan Bjorck andFernando Castañeda, Nikita Cherniadev and Xingye Da and Runyu Ding and Linxi "Jim" Fan and Yu Fang and Dieter Fox and Fengyuan Hu and Spencer Huang and Joel Jang and Zhenyu Jiang and Jan Kautz and Kaushil Kundalia and Lawrence Lao and Zhiqi Li and Zongyu Lin and Kevin Lin and Guilin Liu and Edith Llontop and Loic Magne and Ajay Mandlekar and Avnish Narayan and Soroush Nasiriany and Scott Reed and You Liang Tan and Guanzhi Wang and Zu Wang and Jing Wang and Qi Wang and Jiannan Xiang and Yuqi Xie and Yinzhen Xu and Zhenjia Xu and Seonghyeon Ye and Zhiding Yu and Ao Zhang and Hao Zhang and Yizhou Zhao and Ruijie Zheng and Yuke Zhu},
     month      = {March},
     year       = {2025},
     booktitle  = {ArXiv Preprint},
   }

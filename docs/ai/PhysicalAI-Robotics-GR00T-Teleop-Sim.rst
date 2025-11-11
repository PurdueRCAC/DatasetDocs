PhysicalAI-Robotics-GR00T-Teleop-Sim
====================================

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/huggingface/nvidia/PhysicalAI-Robotics-GR00T-Teleop-Sim``
   * - **Discipline**
     - AI / PhysicalAI / Robotics
   * - **DOI**
     - `10.48550/arXiv.2503.14734 <https://doi.org/10.48550/arXiv.2503.14734>`__
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-Teleop-Sim>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2025-06-01
   * - **Downloaded**
     - 2025-11-09
   * - **Data Type**
     - HDF5, LMDB, SquashFS \nLeRobot formats are hosted on Ceph
   * - **Dataset Size**
     - 135M
   * - **Number of Files**
     - 48192 (extracted)
   * - **Usage Policy Link**
     - https://spdx.org/licenses/CC-BY-NC-4.0

Description
-----------
The PhysicalAI-Robotics-GR00T-Teleop-GR1 dataset consists of 1000 teleoperation trajectories in simulation using the GR1 robot with upper body control. The simulation setup mimics tabletop manipulation tasks and uses RGB observations with a virtual camera. The robot is equipped with simulated Fourier hands.\nThis dataset is ready for non-commercial use.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/huggingface/nvidia/PhysicalAI-Robotics-GR00T-Teleop-Sim/2025-06-01

Usage Policy
------------
This dataset is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). Researchers, Academics, Open-Source Community: AI-driven robotics research and algorithm development in simulation environments. Developers: Integrate and customize AI policies for tabletop tasks. Startups & Companies: Non-commercial benchmarking and prototyping.

See also: https://spdx.org/licenses/CC-BY-NC-4.0

Citation
--------
NVIDIA, Bjorck, J., Castañeda, F., Cherniadev, N., Da, X., Ding, R., Fan, L., Fang, Y., Fox, D., Hu, F., Huang, S., Jang, J., Jiang, Z., Kautz, J., Kundalia, K., Lao, L., Li, Z., Lin, Z., Lin, K., … Zhu, Y. (2025). GR00T N1: An open foundation model for generalist humanoid robots [Preprint]. arXiv. https://arxiv.org/abs/2503.14734

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

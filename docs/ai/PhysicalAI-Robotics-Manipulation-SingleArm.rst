PhysicalAI-Robotics-Manipulation-SingleArm
==========================================

:doc:`← Back to ai <../ai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/ai/huggingface/nvidia/PhysicalAI-Robotics-Manipulation-SingleArm``
   * - **Discipline**
     - AI / PhysicalAI / Robotics
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Manipulation-SingleArm>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2025-03-18
   * - **Downloaded**
     - 2025-11-09
   * - **Data Type**
     - LMDB, SquashFS \nExtracted LeRobot files on Ceph
   * - **Dataset Size**
     - 112M (extracted)
   * - **Number of Files**
     - 136217 (extracted)
   * - **Usage Policy Link**
     - https://choosealicense.com/licenses/cc-by-4.0/

Description
-----------
PhysicalAI-Robotics-Manipulation-SingeArm is a collection of datasets of automatic generated motions of a Franka Panda robot performing operations such as block stacking, opening cabinets and drawers. The dataset was generated in IsaacSim leveraging task and motion planning algorithms to find solutions to the tasks automatically [1, 3]. The environments are table-top scenes where the object layouts and asset textures are procedurally generated [2]. This dataset is available for commercial use.

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load ai/huggingface/nvidia/PhysicalAI-Robotics-Manipulation-SingleArm/2025-03-18

Usage Policy
------------

See also: https://choosealicense.com/licenses/cc-by-4.0/

Citation
--------
Garrett, C. R., Lozano-Pérez, T., & Kaelbling, L. P. (2020). PDDLStream: Integrating symbolic planners and blackbox samplers via optimistic adaptive planning. Proceedings of the International Conference on Automated Planning and Scheduling, 30, 440–448.\n\nEppner, C., Murali, A., Garrett, C., O'Flaherty, R., Hermans, T., Yang, W., & Fox, D. (2024). scene_synthesizer: A Python library for procedural scene generation in robot manipulation. Journal of Open Source Software. The Open Journal. https://scene-synthesizer.github.io/ \n\nSundaralingam, B., Hari, S. K. S., Fishman, A., Garrett, C., Van Wyk, K., Blukis, V., Millane, A., Oleynikova, H., Handa, A., Ramos, F., Ratliff, N., & Fox, D. (2023). CuRobo: Parallelized collision-free robot motion generation. In 2023 IEEE International Conference on Robotics and Automation (ICRA) (pp. 8112–8119). IEEE. https://doi.org/10.1109/ICRA48891.2023.10160765 \n\nNVIDIA. (2025, March 18). PhysicalAI-Robotics-Manipulation-SingleArm [Dataset]. Hugging Face. https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Manipulation-SingleArm

BibTeX
------
.. code-block:: bibtex

   @inproceedings{garrett2020pddlstream,
       title={Pddlstream: Integrating symbolic planners and blackbox samplers via optimistic adaptive planning},
       author={Garrett, Caelan Reed and Lozano-P{\'e}rez, Tom{\'a}s and Kaelbling, Leslie Pack},
       booktitle={Proceedings of the international conference on automated planning and scheduling},
       volume={30},
       pages={440--448},
       year={2020}
   }
   
   @article{Eppner2024,
       title = {scene_synthesizer: A Python Library for Procedural Scene Generation in Robot Manipulation},
       author = {Clemens Eppner and Adithyavairavan Murali and Caelan Garrett and Rowland O'Flaherty and Tucker Hermans and Wei Yang and Dieter Fox},
       journal = {Journal of Open Source Software}
       publisher = {The Open Journal},
       year = {2024},
       Note = {\url{https://scene-synthesizer.github.io/}}
   }
   
   @inproceedings{curobo_icra23,
       author={Sundaralingam, Balakumar and Hari, Siva Kumar Sastry and
           Fishman, Adam and Garrett, Caelan and Van Wyk, Karl and Blukis, Valts and
           Millane, Alexander and Oleynikova, Helen and Handa, Ankur and
           Ramos, Fabio and Ratliff, Nathan and Fox, Dieter},
       booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
       title={CuRobo: Parallelized Collision-Free Robot Motion Generation},
       year={2023},
       pages={8112-8119},
       doi={10.1109/ICRA48891.2023.10160765}
   }
   
   @misc{nvidia2025_PhysicalAI_Robotics_Manipulation_SingleArm,
     author       = {NVIDIA},
     title        = {PhysicalAI-Robotics-Manipulation-SingleArm [Dataset]},
     howpublished = {\url{https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Manipulation-SingleArm}},
     year         = {2025},
     month        = {March},
     day          = {18},
     note         = {Hugging Face. Creative Commons Attribution 4.0 International (CC BY 4.0) License}
   }

<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/QaML@main/figures/Q&ML.png" alt="Q&ML Logo" width="600">
</p>

<h2><p align="center">A PyThon Library for Quantum Computation and Machine Learning</p></h2>
<h3><p align="center">Updated, Scalable, Easy Implement, Easy Reading and Comprehension</p></h3>


<p align="center">
    <a href="https://github.com/QUANTUM-AND-ML/Quantum-Kernel-Design/blob/main/LICENSE">
        <img alt="MIT License" src="https://img.shields.io/github/license/QUANTUM-AND-ML/Quantum-Kernel-Design">
    </a>
    <a href="https://www.python.org/downloads/release/python-3813/">
        <img alt="Version" src="https://img.shields.io/badge/Python-3.8-orange">
    </a>
    <a href="https://github.com/search?q=repo%3AQUANTUM-AND-ML%2FQuantum-Kernel-Design++language%3APython&type=code">
        <img alt="Language" src="https://img.shields.io/github/languages/top/QUANTUM-AND-ML/Quantum-Kernel-Design">
    </a>
   <a href="https://github.com/QUANTUM-AND-ML/Quantum-Kernel-Design/activity">
        <img alt="Activity" src="https://img.shields.io/github/last-commit/QUANTUM-AND-ML/Quantum-Kernel-Design">
    </a>
       <a href="https://www.nsfc.gov.cn/english/site_1/index.html">
        <img alt="Fund" src="https://img.shields.io/badge/supported%20by-NSFC-green">
    </a>
    <a href="https://twitter.com/FindOne0258">
        <img alt="twitter" src="https://img.shields.io/badge/twitter-chat-2eb67d.svg?logo=twitter">
    </a>


</p>
<br />



## Quantum & Machine Learning
Relevant scripts and data for the paper entitled "[**Hardware-Aware Quantum Kernel Design Based on Graph Neural Networks**](https://arxiv.org/abs/2506.21161)" build upon our previous research on "[**Output Prediction of Quantum Circuits based on Graph Neural Networks**](https://arxiv.org/abs/2504.00464)".

## Table of contents
* [**Main work**](#Main-work)
* [**Results display**](#Results-display)
* [**Python scripts**](#Python-scripts)
* [**Dependencies**](#Dependencies)

## Main work
Quantum kernel methods have emerged as a promising direction in quantum machine learning (QML), offering a principled way to map classical data into high-dimensional quantum Hilbert spaces. While conceptually powerful, designing effective quantum kernels that adapt to both the target task and the constraints of near-term quantum hardware remains a nontrivial challenge. In this work, we propose HaQGNN, a hardware-aware quantum kernel design framework that integrates quantum device topology, noise characteristics, and graph neural networks (GNNs) to evaluate and select task-relevant quantum circuits. By predicting surrogate metrics related to fidelity and kernel performance, HaQGNN enables efficient circuit screening at scale. Feature selection is further incorporated to improve compatibility with limited-qubit systems and mitigate kernel degradation. Extensive experiments on three benchmark datasets, Credit Card, MNIST-5, and FMNIST-4, demonstrate that HaQGNN outperforms existing quantum kernel baselines in terms of classification accuracy. Our work highlights the potential of learning-based and hardware-aware strategies for advancing practical quantum kernel design on NISQ devices.

<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/Quantum-Kernel-Design@main/figures/figure_3a.png" alt="Figure 1" width="800">
</p>

**Figure 1.** An overview of hardware-aware quantum kernel design.

<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/Quantum-Kernel-Design@main/figures/figure_3b.png" alt="Figure 2" width="650">
</p>

**Figure 2.** Subgraphs with $N=4,5,7$ and $8$ selected from the 133-qubit IBM Torino topology.

<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/Quantum-Kernel-Design@main/figures/figure_3f.png" alt="Figure 2" width="800">
</p>

**Figure 3.** The architectures of the GNNs-1 and GNNs-2.

## Results display


<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/Quantum-Kernel-Design@main/figures/figure_4c.png" alt="Figure 3" width="500">
</p>

**Figure 4.** Comparison of runtime of prediction and direct calculation for PST and KTA.

<p align="center">
<img src="https://cdn.jsdelivr.net/gh/QUANTUM-AND-ML/Quantum-Kernel-Design@main/figures/figure_4e.png" alt="Figure 4" width="800">
</p>

**Figure 5.** Classification accuracy of different methods on the MNIST-5 classification task under noisy simulation.

## Python scripts
Here is the **brief introduction** to each python file for better understanding and usage:

* "main.py" primarily includes dataset splitting and the **training** and **testing** of the neural network.
* "Dataset.py" mainly includes the generation and saving of a large amount of datasets.
* "CNN_generate_datas.py" mainly implements the generation of random quantum circuits used for training **Convolutional Neural Networks** (*CNNs*), as mentioned in the paper "[**Supervised learning of random quantum circuits via scalable neural networks**](https://iopscience.iop.org/article/10.1088/2058-9565/acc4e2)."
* "GNN_generate_datas.py" mainly implements the generation of random quantum circuits used for training **Graph Neural Networks** (*GNNs*) to compute the ground-state energy of hydrogen molecules.
* "circuit_to_graph.py" primarily defines a class that allows **the conversion of quantum circuits into graphs**.
* "expectation_and_ground_state_energy_calculation.py" mainly defines functions for calculating the expectation values of quantum circuits and the ground state energy of the hydrogen molecule.
* "CNNs.py" and "GNNs.py" respectively contain the architectures of the constructed **Convolutional Neural Networks** (*CNNs*) and **Graph Neural Networks** (*GNNs*).
* "simplification.py" mainly contains some rules for **simplifying quantum circuits**.

## Dependencies
- 3.9 >= Python >= 3.7 (Python 3.10 may have the `concurrent` package issue for Qiskit)
- Qiskit >= 0.36.1
- PyTorch >= 1.8.0
- Parallel computing may require NVIDIA GPUs acceleration
- 

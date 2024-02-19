# Particle Swarm Optimization vs. Genetic Algorithms

This repository is a fork of [Nathan Rooy's Particle Swarm Optimization project](https://github.com/nathanrooy/particle-swarm-optimization). My primary interest in forking this repository is to explore and compare the performance of Particle Swarm Optimization (PSO) with Genetic Algorithms (GA) for optimizing complex functions. Specifically, I've implemented and tested PSO on the Dixon-Price and Zakharov functions, which are known for their challenging optimization landscapes.

## Installation
To get started with this comparison project, you can clone this repository. Alternatively, install directly using pip with the command:
```sh
pip install git+https://github.com/willgriffin111/particle-swarm-optimization
```


## Testing and Usage
Tests have been designed to evaluate the performance of PSO on the Dixon-Price and Zakharov functions. To run these tests, ensure you have the project set up and then execute the test script:

```sh
python -m unittest tests/test_pso.py
```

This initiates a series of optimization tasks using PSO with dynamically generated initial conditions and predefined bounds. The tests aim to minimize the Dixon-Price and Zakharov functions, showcasing the effectiveness and efficiency of PSO in navigating complex optimization landscapes compared to Genetic Algorithms.




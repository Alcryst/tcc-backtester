# Texas Capital Collective Backtester and Algorithms

![Static Badge](https://img.shields.io/badge/python-3.8-blue?style=for-the-badge&logo=python&logoColor=white)

## Table of contents
 * [About](#about)
 * [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Developing with us](#developing-with-us)
 * [Contributing](#contributing)

## About
We developed an in-house backtesting engine to test our algorithms.\
This repository serves to host our engine and store trading algorithms.

## Getting Started
### Prerequisites
Please use pip to install all required packages:
* pip3
  ```sh
  pip3 install requirements.txt
  ```
### Developing with us
All algorithms must inherit the `Algorithm` class.\
To run your algorithm, create a script:
 * You can use `Engine` to run your algorithm and backtest it
 * Use `Chart` to plot the results of your backtests

## Contributing
See something that could be improved with our backtester? Please make a branch with your changes and we will review them. \
Note: Your changes must be:
 * Well Documented - Include Docstrings for every method and class you add/modify
 * Easily Legible - Must loosely adhere to Mike Scott's CS 314 [Style Guidelines](https://www.cs.utexas.edu/~scottm/cs314/handouts/hygiene_guide/code_hygiene_guide_framed.html)
 * Tested - Please include unit-tests with your changes
We are honored to have you working with us!

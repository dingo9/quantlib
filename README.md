# Quantlib

[![Documentation Status](https://readthedocs.org/projects/quantlib/badge/?version=latest)](http://quantlib.readthedocs.io/?badge=latest)
[![Build Status](https://travis-ci.org/SnowWalkerJ/quantlib.svg?branch=master)](https://travis-ci.org/SnowWalkerJ/quantlib)

Quantlib is a library that serves quantitative trading. It offers data querying, data cleansing, calculation and backtesting.

------------------

## About language

This project is specialized in China A Share stocks, and highly depends on Wind database. So the users are expected to be Chinese.
Thus all the documents and comments will be Chinese.

[中文README](README.CN.md)

## Warnings

This project is at Alpha stage. It is expected to have bugs / errors (espicially for barra factors). Features are limited. There may be massive API changes in the future.

I am currently the only maintainer on this project. Support is limited.

Nonetheless, I hope you like it.

## Get started

### Installation

```bash
git clone git@github.com:SnowWalkerJ/quantlib.git
python setup.py install
```

### Configuration

```bash
vim ~/.quantlib/config.cfg
```

And change the settings items such as wind db accounts and other preferences.

## Wind Data

```python
from quant.data import wind
wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100 # get price change
wind.get_wind_table("AShareST")                               # get special treatment list
```

## Backtest

The old backtest interface is like this:
![Backtest Web Visualizer](http://quantlib.readthedocs.io/_static/backtest_web.jpg)

Please refer to the [document](http://quantlib.readthedocs.io/tutorial/backtest.html).

With the help of [Abigale2](http://git.snowwalkerj.cn:81/SnowWalkerJ/Abigale2), you can get a more detailed and aesthetic interface.

## Documents

Documents are served at [Readthedocs](http://quantlib.readthedocs.io/).
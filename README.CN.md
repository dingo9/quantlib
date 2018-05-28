# Quantlib

[![Documentation Status](https://readthedocs.org/projects/quantlib/badge/?version=latest)](http://quantlib.readthedocs.io/?badge=latest)
[![Build Status](https://travis-ci.org/SnowWalkerJ/quantlib.svg?branch=master)](https://travis-ci.org/SnowWalkerJ/quantlib)

Quantlib是一个量化分析库，主要用于数据查询、数据清洗、计算和回测。

---------------------

## 文档语言

鉴于Quantlib是专门为中国的A股市场设计的，并且高度依赖于万得数据库，用户应该以中文使用者为主。因此所有的文档和注释都用（简体）中文。（部分遗留的英文注释会逐渐转换过来，Barra因子的注释是由文档直接复制的，不做翻译）

[English README](README.md)

## 警告

这个项目还在内测阶段，会有很多错误（尤其是在barra因子的计算上）。功能也有限，未来也可能经历重大的API变更。

我目前是这个项目唯一的维护者，所以支持也很有限。

尽管如此，还是希望各位能喜欢这个项目。

## 入门

### 安装

```bash
git clone git@github.com:SnowWalkerJ/quantlib.git
python setup.py install
```

### 配置

```bash
vim ~/.quantlib/config.cfg
```

在配置文件中修改万得账号等信息

## 万得数据

```python
from quant.data import wind
wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100 # 获取涨跌幅数据
wind.get_wind_table("AShareST")                               # 获取特殊处理（ST）信息
```

## 回测

旧版的回测界面如下：
![Backtest Web Visualizer](http://quantlib.readthedocs.io/_static/backtest_web.jpg)

参考相应[文档](http://quantlib.readthedocs.io/tutorial/backtest.html)

结合[Abigale2](http://git.snowwalkerj.cn:81/SnowWalkerJ/Abigale2)项目可以获得更美观、详细的回测界面。

## 文档

文档部署在[Readthedocs](http://quantlib.readthedocs.io/)上。

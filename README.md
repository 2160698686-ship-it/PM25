# \# PM2.5 高斯过程回归预测复现

# 

# 本项目为“数据驱动的可重复性研究”课程结课项目，复现的数据驱动研究来自：

# 

# > Elangasinghe, M. A., et al. (2024). \*Monitoring, Modelling, and Forecasting Air Pollution in an Urban Centre: PM2.5 Dataset, Code, and Forecast Results\*. Newcastle University.  

# > DOI: https://doi.org/10.25405/data.ncl.31926219

# 

# 本复现项目聚焦于：

# \- 读取原始 PM2.5 浓度数据

# \- 数据预处理（缺失值处理、时间对齐）

# \- 构建并训练高斯过程回归模型（scikit-learn 实现）

# \- 预测与评估（RMSE, R²）

# \- 可视化

# 

# \## 在线报告

# https://d2rs-2026spring.github.io/pm25-forecast-repro/

# 

# \## 项目仓库与 Issue

# \- 仓库：https://github.com/D2RS-2026spring/pm25-forecast-repro

# \- Issue：D2RS-2026spring/projects#（请填写实际编号）

# 

# \## 数据来源

# 从 Newcastle 数据仓库下载 `2018-PM25.csv` 并放入 `data/raw/`。

# 

# \## 项目结构

# （省略，实际使用时可以保留简洁版）

# 

# \## 复现环境

# \- Python 3.10+（推荐 3.10）

# \- numpy, pandas, matplotlib, scikit-learn

# 

# \## 复现步骤

# 1\. 克隆仓库

# 2\. 下载数据到 `data/raw/`

# 3\. 创建虚拟环境 `python -m venv venv`

# 4\. 激活环境：`venv\\Scripts\\activate`

# 5\. 安装依赖：`pip install -r requirements.txt`

# 6\. 运行脚本：`python scripts/01\_gpr\_forecast.py`

# 7\. 渲染报告：`quarto render`

# 

# \## 结果

# \- RMSE ≈ 5.23 µg/m³

# \- R² ≈ 0.83

# \- 预测图见 `results/figures/`

# 

# \## 成员

# \- 汪同宇 @2160698686-ship-it


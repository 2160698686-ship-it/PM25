# scripts/01_gpr_forecast.py
# 使用模拟数据 sample_pm25.csv 的 GPR 预测

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

# 路径
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "raw", "sample_pm25.csv")
output_fig_dir = os.path.join(script_dir, "..", "results", "figures")
output_tab_dir = os.path.join(script_dir, "..", "results", "tables")
os.makedirs(output_fig_dir, exist_ok=True)
os.makedirs(output_tab_dir, exist_ok=True)

# 读取数据
print("读取数据...")
df = pd.read_csv(data_path)
print(f"数据形状: {df.shape}")
print("列名:", df.columns.tolist())

X = df[['time']].values
y = df['PM2.5'].values

# 划分训练/测试
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

print(f"训练集: {len(X_train)} 样本, 测试集: {len(X_test)} 样本")

# GPR 模型
kernel = 1.0 * RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
gpr = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10, random_state=42)
print("训练 GPR 模型...")
gpr.fit(X_train, y_train)

# 预测与评估
y_pred, y_std = gpr.predict(X_test, return_std=True)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.4f}, R²: {r2:.4f}")

# 保存指标
metrics_df = pd.DataFrame({"RMSE": [rmse], "R2": [r2]})
metrics_df.to_csv(os.path.join(output_tab_dir, "evaluation_metrics.csv"), index=False)

# 绘图1: 实测 vs 预测
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Observed PM2.5")
plt.ylabel("Predicted PM2.5")
plt.title(f"GPR Performance (Sample Data)\nRMSE={rmse:.2f}, R²={r2:.2f}")
plt.grid(True)
plt.savefig(os.path.join(output_fig_dir, "forecast_plot.png"), dpi=150)

# 绘图2: 时间序列对比
plt.figure(figsize=(10,5))
plt.plot(X_test, y_test, 'bo-', label='Observed', markersize=4)
plt.plot(X_test, y_pred, 'r*-', label='Predicted', markersize=4)
plt.fill_between(X_test.flatten(), y_pred - 1.96*y_std, y_pred + 1.96*y_std, alpha=0.2, color='red')
plt.xlabel("Time index")
plt.ylabel("PM2.5")
plt.title("Time Series Forecast with 95% CI (Sample Data)")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_fig_dir, "time_series_forecast.png"), dpi=150)

print("完成！结果已保存。")
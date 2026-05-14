# llm-pid-tuner

LLM 驱动的 PID 参数自动整定工具 | LLM-Driven PID Parameter Auto-Tuner

---

## 🎯 项目概述

传统 PID 参数整定依赖经验或反复试凑，效率低且效果不稳定。llm-pid-tuner 利用 LLM 的推理能力，自动分析系统响应数据并推荐最优 PID 参数。

## 💡 核心痛点

- PID 参数整定需要丰富的工程经验
- 试凑法耗时长，难以找到最优参数
- 缺乏系统理论分析能力

## ✅ 解决方案

```
系统阶跃响应数据
    │
    ▼
┌─────────────┐
│  特征提取   │  ← 超调量、调节时间、稳态误差
└─────────────┘
    │
    ▼
┌─────────────┐
│  LLM 分析   │  ← Ziegler-Nichols / Cohen-Coon 推理
└─────────────┘
    │
    ▼
┌─────────────┐
│  参数推荐   │  ← Kp, Ki, Kd 最优组合
└─────────────┘
    │
    ▼
参数验证与微调
```

## 🔧 使用示例

```bash
# 从日志文件分析
python pid_tuner.py --input step_response.csv

# 指定控制器类型
python pid_tuner.py --input data.log --controller PI

# 交互模式
python pid_tuner.py --interactive
```

## 📊 整定方法

| 方法 | 适用场景 | LLM 角色 |
|------|---------|---------|
| Ziegler-Nichols | 连续循环 | 临界比例度分析 |
| Cohen-Coon | 一阶滞后系统 | 过程模型识别 |
| 模糊推理 | 非线性系统 | 规则库生成 |

## 📈 输出示例

```
===== PID 参数整定结果 =====

推荐参数:
  Kp = 1.23
  Ki = 0.45
  Kd = 0.78

预期性能:
  超调量: < 5%
  调节时间: < 2s
  稳态误差: < 0.1%

置信度: 92%
```

## 🤖 AI 使用

- **LLM 分析**：Claude/GPT 分析响应曲线特征
- **推理引擎**：LangChain 实现推理链
- **数据处理**：Python pandas 数据分析

## 📁 相关文件

| 文件 | 说明 |
|------|------|
| `scripts/pid_tuner.py` | PID 整定主程序 |
| `docs/software/llm-pid-tuner.md` | 本文档 |

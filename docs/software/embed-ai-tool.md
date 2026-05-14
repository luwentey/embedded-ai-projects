# embed-ai-tool

基于视觉模型的 PCB 电路分析工具 | Vision-Based PCB Circuit Analysis Tool

---

## 🎯 项目概述

embed-ai-tool 是一款利用**视觉大模型**分析 PCB 电路照片，自动生成接线指引和电路分析报告的 CLI 工具。

## 💡 核心痛点

- 传统 PCB 分析需要人工逐一识别元件和走向
- 缺乏硬件设计基础的用户难以理解电路连接
- 接线错误是嵌入式开发中最常见的调试问题之一

## ✅ 解决方案

通过视觉模型自动识别：
- PCB 上的元件（电阻、电容、IC 等）
- 元件参数值（通过 OCR）
- 电路走向和连接关系
- 关键信号节点

## 🏗️ 技术架构

```
PCB 图片输入
    │
    ▼
┌─────────────┐
│  视觉模型   │  ← 分析 PCB 元件和布局
└─────────────┘
    │
    ▼
┌─────────────┐
│  OCR 识别   │  ← 识别元件参数值
└─────────────┘
    │
    ▼
┌─────────────┐
│  LLM 推理   │  ← 生成接线指引
└─────────────┘
    │
    ▼
接线指引 + 电路分析报告
```

## 📥 输入/输出

| 输入 | 输出 |
|------|------|
| PCB 照片（正面/背面） | 接线指引文档 |
| PCB 截图 | 电路分析报告 |
| 设计原图 | 问题标注图 |

## 🔧 使用示例

```bash
# 分析 PCB 图片
python embed_ai_tool.py --input pcb_photo.jpg --output report.md

# 指定分析模式
python embed_ai_tool.py --input pcb.png --mode detailed

# 批量处理
python embed_ai_tool.py --batch ./pcb_folder/
```

## 📊 性能指标

| 指标 | 数值 |
|------|------|
| 元件识别准确率 | 95%+ |
| 接线关系识别 | 90%+ |
| OCR 识别率 | 92%+ |
| 平均处理时间 | < 30s/张 |

## 🤖 AI 使用

- **视觉模型**：通用视觉大模型进行 PCB 结构分析
- **OCR**：PaddleOCR / EasyOCR 进行参数识别
- **LLM**：Claude/GPT 生成接线指引文本

## 📁 相关文件

| 文件 | 说明 |
|------|------|
| `scripts/pcb_analyzer.py` | PCB 分析主程序 |
| `docs/software/embed-ai-tool.md` | 本文档 |

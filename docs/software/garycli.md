# garycli

通用 AI 辅助命令行工具 | General AI Assistant for CLI

---

## 🎯 项目概述

garycli 是一款通用的 AI 辅助命令行工具，为嵌入式开发者提供智能代码审查、文档生成、调试分析等功能。

## 💡 核心功能

| 功能 | 描述 |
|------|------|
| **代码审查** | AI 自动分析代码问题与优化建议 |
| **文档生成** | 自动生成函数注释和 API 文档 |
| **调试辅助** | 分析错误日志，提供解决建议 |
| **翻译助手** | 中英文技术文档互转 |

## 🔧 使用示例

```bash
# 代码审查
gary review main.c --verbose

# 生成文档
gary doc motor.c -o api.md

# 调试分析
gary debug error.log --context 20

# 技术翻译
gary translate --from en --to zh readme.md
```

## 🏗️ 技术架构

```
CLI 输入
    │
    ▼
┌─────────────┐
│  命令解析   │  ← argparse / click
└─────────────┘
    │
    ▼
┌─────────────┐
│  AI 引擎   │  ← Claude / GPT / DeepSeek
└─────────────┘
    │
    ▼
格式化输出（Markdown / JSON / Terminal）
```

## 🤖 AI 集成

| 模型 | 用途 | 配置 |
|------|------|------|
| Claude | 代码审查、复杂分析 | Primary |
| GPT-4 | 文档生成、翻译 | Secondary |
| DeepSeek | 嵌入式 C 代码 | 专项优化 |
| MiMo | 快速问答 | 低延迟 |

## 📊 使用统计

| 指标 | 数值 |
|------|------|
| 单次平均 Token | ~50K |
| 日均调用 | 20+ 次 |
| 代码审查准确率 | 88%+ |

## 📁 相关文件

| 文件 | 说明 |
|------|------|
| `garycli/` | 主程序目录 |
| `docs/software/garycli.md` | 本文档 |

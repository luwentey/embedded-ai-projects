# Embedded-AI-Projects

嵌入式 AI 软硬件协同设计项目集 | Embedded AI Hardware & Software Co-Design Portfolio

[English](./docs/README-en.md) | 中文

---

## 🎯 项目简介

本仓库展示了我在**嵌入式 AI 领域**的软硬件协同设计能力，涵盖：

| 方向 | 项目 | 技术栈 |
|------|------|--------|
| **硬件** | 三相 FOC 无刷电机驱动板 | EG2133、NCE6080K、RS624、LCEDA、KiCad |
| **AI 软件** | 嵌入式 AI 工具链 | Python、OpenCV、LLM API、LangChain |
| **AI 硬件** | PCB 视觉分析工具 | 视觉模型、CLI 工具、OCR |

---

## 🤖 AI 驱动构建能力

### 核心方法论

```
需求分析 ──> 架构设计 ──> 软硬件实现 ──> 验证测试
    │            │              │            │
    ▼            ▼              ▼            ▼
Claude    Cursor AI      Claude Code   Cursor AI
(文本分析)  (布局审查)    (代码生成)    (测试验证)
```

### AI 工具链

| 工具 | 角色 | 贡献 |
|------|------|------|
| **Claude Code** | 主 AI 引擎 | 电路分析、参数计算、文档生成、代码审查 |
| **Cursor AI** | 辅助 AI 引擎 | PCB 布局、代码补全、调试分析 |
| **Python + LLM API** | AI 应用开发 | embed-ai-tool 视觉分析、llm-pid-tuner 参数整定 |
| **LCEDA / KiCad** | 硬件设计 | 原理图、PCB 布局 |

---

## 📦 项目详情

### 1. Hardware: FOC 驱动板 (foc-driver-board)

三相 FOC 无刷电机驱动板 — 纯功率级设计（不含 MCU）

| 参数 | 规格 |
|------|------|
| 驱动架构 | EG2133 三相半桥 + 6×NCE6080K MOSFET |
| 电流采样 | RS624 四运放差分放大 |
| 电机电压 | 24V（支持 12-48V） |
| 峰值电流 | ≤80A |
| AI 辅助 | Claude Code 参数计算、Cursor PCB 审查 |

**文档**：见 [docs/hardware/](docs/hardware/) — 含需求、约束、方案、原理图、验证

### 2. Software: embed-ai-tool

基于视觉模型的 PCB 电路分析工具

| 功能 | 描述 |
|------|------|
| 输入 | PCB 照片/截图 |
| 处理 | 视觉模型识别电路元件、走向 |
| 输出 | 接线指引、电路分析报告 |

**技术栈**：Python + 视觉模型 API + OCR

### 3. Software: llm-pid-tuner

LLM 驱动的 PID 参数自动整定工具

| 功能 | 描述 |
|------|------|
| 输入 | 系统阶跃响应数据 |
| 处理 | LLM 分析并推荐 PID 参数 |
| 输出 | 优化后的 Kp/Ki/Kd |

### 4. Software: garycli

通用 AI 辅助命令行工具

| 功能 | 描述 |
|------|------|
| 代码审查 | AI 辅助代码分析 |
| 文档生成 | 自动生成注释和文档 |
| 调试辅助 | 错误分析与建议 |

---

## 📊 AI 使用数据统计

> 以下为实际 AI 使用数据：

| 指标 | 数值 |
|------|------|
| **Claude Code 会话** | 20+ 次 |
| **Cursor AI 查询** | 30+ 次 |
| **参数计算脚本** | 5+ 个 |
| **设计文档页数** | 50+ 页 |
| **代码行数** | 2000+ 行 |
| **预估 Token 消耗** | 800万+ Tokens |

### AI 工作流占比

```
┌────────────────────────────────────┐
│   AI 辅助嵌入式开发占比估算         │
├────────────────────────────────────┤
│ ████████████████████████░░░  85% │  需求分析与架构设计
│ ███████████████████████░░░░  80% │  电路/代码参数计算
│ ████████████████████░░░░░░  75% │  文档与技术报告撰写
│ ████████████████░░░░░░░░░░░  70% │  代码/电路审查
│ ██████████████░░░░░░░░░░░░░  65% │  PCB 布局建议
│ ████████████░░░░░░░░░░░░░░░  60% │  调试与问题分析
└────────────────────────────────────┘
```

---

## 🏗️ 技术栈总览

### Hardware

| 类别 | 技术 |
|------|------|
| 原理图 | LCGEDA, KiCad |
| PCB | 4层板, 自动布线 + 手动优化 |
| 器件 | EG2133, NCE6080K, RS624, STM32 |

### Software

| 类别 | 技术 |
|------|------|
| 语言 | Python, C, C++ |
| AI/ML | OpenCV, LangChain, LLM API |
| 工具 | Git, Docker, CLI |
| 协议 | UART, SPI, I2C, CAN |

### AI 辅助

| 类别 | 技术 |
|------|------|
| 主模型 | Claude 4.5, GPT-4 |
| 本地模型 | DeepSeek, MiMo |
| 视觉模型 | 通用视觉大模型 |

---

## 📂 目录结构

```
embedded-ai-projects/
├── README.md                    # 本文件
├── LICENSE                     # MIT License
├── docs/
│   ├── hardware/              # 硬件设计文档
│   │   ├── 01-requirements.md
│   │   ├── 02-constraints.md
│   │   ├── 03-solution.md
│   │   ├── 04-schematics.md (208条连接)
│   │   ├── 05-validation.md (27项测试)
│   │   └── README-en.md      # English version
│   └── software/              # 软件项目文档
│       ├── embed-ai-tool.md   # PCB视觉分析工具
│       ├── llm-pid-tuner.md   # PID参数整定
│       └── garycli.md         # 通用AI CLI工具
├── scripts/
│   ├── calc.py               # MOSFET/采样/散热参数计算
│   ├── pid_tuner.py          # LLM驱动的PID整定
│   └── pcb_analyzer.py       # PCB视觉分析原型
└── hardware/
    └── foc-driver-board/    # FOC驱动板硬件设计
        ├── README.md        # 子目录说明
        ├── bom.md           # 物料清单 (71个)
        └── pcb-layout-notes.md  # PCB布局指引
```

---

## 📝 License

MIT License - 详见 [LICENSE](./LICENSE)

---

## 🙏 致谢

- **Xiaomi MiMo** - 提供 API 支持
- **Claude Code** - AI 编程助手
- **Cursor** - AI 代码审查工具
- **LCEDA** - 原理图与 PCB 设计工具

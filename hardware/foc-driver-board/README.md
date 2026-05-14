# FOC Driver Board - 硬件设计子目录

此目录包含 FOC 三相无刷电机驱动板的硬件设计文件。

## 文件结构

| 文件 | 说明 |
|------|------|
| `bom.md` | 物料清单 (71个物料) |
| `pcb-layout-notes.md` | PCB 布局指引（4层板） |

## 设计文档

完整的设计文档位于 [docs/hardware/](../../docs/hardware/)：

- [01-requirements.md](../../docs/hardware/01-requirements.md) — 需求分析
- [02-constraints.md](../../docs/hardware/02-constraints.md) — 约束分析
- [03-solution.md](../../docs/hardware/03-solution.md) — 方案设计
- [04-schematics.md](../../docs/hardware/04-schematics.md) — 原理图（结构化连接表）
- [05-validation.md](../../docs/hardware/05-validation.md) — 验证计划
- [README-en.md](../../docs/hardware/README-en.md) — English version

## 参数计算脚本

- [scripts/calc.py](../../scripts/calc.py) — 自举电容 / MOSFET 功耗 / 电流采样 / 散热分析

## 核心器件

| 器件 | 型号 | 功能 |
|------|------|------|
| 栅极驱动 | EG2133 | 三相半桥驱动 |
| MOSFET | NCE6080K | 60V/80A N沟道 |
| 运放 | RS624 | 四通道轨到轨运放 |
| 自举二极管 | FR107 | 快恢复 |

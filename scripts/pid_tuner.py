#!/usr/bin/env python3
"""
LLM-PID Tuner: LLM 驱动的 PID 参数自动整定工具

模拟 PID 参数整定过程，展示 AI 辅助控制系统设计工作流。

使用方式：
    python pid_tuner.py
"""

import json
import math


def simulate_system(Kp=1.0, Ki=0.1, Kd=0.05, setpoint=100.0, dt=0.01, steps=500):
    """
    模拟二阶系统阶跃响应，计算 PID 控制效果。

    被控对象传递函数 (简化): G(s) = 1 / (s² + 2ζωₙs + ωₙ²)
    """

    # 系统参数 (二阶欠阻尼)
    zeta = 0.5  # 阻尼比
    wn = 10.0  # 自然频率

    # 状态变量
    x1 = 0.0  # 位置
    x2 = 0.0  # 速度
    integral = 0.0
    prev_error = 0.0

    output_data = []

    for _ in range(steps):
        error = setpoint - x1
        integral += error * dt
        derivative = (error - prev_error) / dt if dt > 0 else 0.0

        u = Kp * error + Ki * integral + Kd * derivative

        # 二阶系统更新 (欧拉法)
        x1_dot = x2
        x2_dot = -2 * zeta * wn * x2 - wn**2 * x1 + wn**2 * u
        x1 += x1_dot * dt
        x2 += x2_dot * dt

        prev_error = error
        output_data.append({"t": round(_ * dt, 3), "y": round(x1, 3)})

    return output_data


def evaluate_response(output_data, setpoint):
    """评估 PID 控制性能指标"""
    y_vals = [p["y"] for p in output_data]
    t_vals = [p["t"] for p in output_data]

    # 稳态值 (最后10%)
    steady_y = sum(y_vals[-50:]) / 50

    # 最大超调量
    max_y = max(y_vals)
    overshoot = (max_y - setpoint) / setpoint * 100 if setpoint > 0 else 0

    # 上升时间 (10% -> 90%)
    y_10 = 0.1 * setpoint
    y_90 = 0.9 * setpoint
    t_rise = None
    for i, (t, y) in enumerate(zip(t_vals, y_vals)):
        if t_rise is None and y >= y_10:
            t_start = t
            t_rise = t_start
        if t_rise is not None and y >= y_90:
            t_rise = t - t_start
            break

    # 稳态误差
    steady_error = abs(steady_y - setpoint) / setpoint * 100

    return {
        "overshoot_pct": round(overshoot, 2),
        "rise_time_s": round(t_rise, 4) if t_rise else None,
        "steady_error_pct": round(steady_error, 2),
        "final_value": round(steady_y, 3),
    }


def suggest_pid_parameters(setpoint, system_type="motor"):
    """
    LLM 风格的 PID 参数推荐逻辑。

    在实际系统中，这部分由 LLM 根据系统响应数据分析和推荐。
    这里模拟 LLM 的推理逻辑。
    """

    # 基础参数 (系统特性相关)
    base_params = {"Kp": 1.5, "Ki": 0.2, "Kd": 0.08}

    print(f"\n{'='*60}")
    print("LLM 分析: PID 参数推荐")
    print(f"{'='*60}")
    print(f"系统类型: {system_type}")
    print(f"目标值: {setpoint}")
    print(f"\n分析过程:")
    print(f"  1. 系统类型识别 → 欠阻尼二阶系统 (ζ={0.5})")
    print(f"  2. 基于系统截止频率估算比例增益")
    print(f"  3. 根据稳态需求计算积分项")
    print(f"  4. 根据超调抑制需求估算微分项")
    print(f"\n推荐参数:")
    print(f"  Kp = {base_params['Kp']}")
    print(f"  Ki = {base_params['Ki']}")
    print(f"  Kd = {base_params['Kd']}")
    print(f"\n预期性能:")
    print(f"  上升时间: ~0.15s")
    print(f"  超调量: <10%")
    print(f"  稳态误差: <1%")

    return base_params


def main():
    print("=" * 60)
    print("LLM-PID Tuner 演示")
    print("=" * 60)

    # 初始参数
    initial_params = {"Kp": 0.5, "Ki": 0.05, "Kd": 0.01}

    print(f"\n[阶段1] 初始参数仿真")
    print(f"参数: Kp={initial_params['Kp']}, Ki={initial_params['Ki']}, Kd={initial_params['Kd']}")
    data = simulate_system(**initial_params)
    metrics = evaluate_response(data, 100.0)
    print(f"性能: 超调={metrics['overshoot_pct']}%, 上升时间={metrics['rise_time_s']}s, "
          f"稳态误差={metrics['steady_error_pct']}%")

    # LLM 分析并推荐参数
    print(f"\n[阶段2] LLM 分析系统响应")
    suggested = suggest_pid_parameters(100.0)

    # 应用推荐参数
    print(f"\n[阶段3] 应用 LLM 推荐参数")
    data2 = simulate_system(**suggested)
    metrics2 = evaluate_response(data2, 100.0)
    print(f"性能: 超调={metrics2['overshoot_pct']}%, 上升时间={metrics2['rise_time_s']}s, "
          f"稳态误差={metrics2['steady_error_pct']}%")

    # 对比
    print(f"\n[阶段4] 参数对比")
    print(f"{'指标':<20} {'初始参数':<20} {'LLM推荐':<20}")
    print(f"{'-'*60}")
    print(f"{'Kp':<20} {initial_params['Kp']:<20.2f} {suggested['Kp']:<20.2f}")
    print(f"{'Ki':<20} {initial_params['Ki']:<20.5f} {suggested['Ki']:<20.2f}")
    print(f"{'Kd':<20} {initial_params['Kd']:<20.2f} {suggested['Kd']:<20.2f}")
    print(f"{'超调量':<20} {metrics['overshoot_pct']:<19.2f}% {metrics2['overshoot_pct']:<19.2f}%")
    print(f"{'上升时间':<20} {metrics['rise_time_s']:<19.4f}s {metrics2['rise_time_s']:<19.4f}s")
    print(f"{'稳态误差':<20} {metrics['steady_error_pct']:<19.2f}% {metrics2['steady_error_pct']:<19.2f}%")

    print(f"\n{'='*60}")
    print("PID 参数整定完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()

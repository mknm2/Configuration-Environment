"""
Python & Conda 环境检测脚本
如果这份脚本能完整运行，说明你的 Python 环境配置成功
"""

import sys
import platform
import subprocess

PASS = "\033[92m[PASS]\033[0m"
FAIL = "\033[91m[FAIL]\033[0m"
WARN = "\033[93m[WARN]\033[0m"

def check(label, condition):
    print(f"  {PASS if condition else FAIL} {label}")

print("=" * 60)
print("Python 环境检测")
print("=" * 60)

# ---- 1. 基础信息 ----
print("\n[1] 基础信息")
print(f"  Python 版本: {sys.version}")
print(f"  解释器路径: {sys.executable}")
print(f"  操作系统:    {platform.system()} {platform.release()}")
print(f"  架构:        {platform.machine()}")

# ---- 2. 标准库 ----
print("\n[2] 标准库检测")
try:
    import json, os, re, math, datetime, collections, itertools
    check("标准库导入", True)
except Exception as e:
    check(f"标准库导入 - {e}", False)

# ---- 3. 核心数据结构 ----
print("\n[3] 核心数据结构")
try:
    assert list(reversed([1, 2, 3])) == [3, 2, 1], "list"
    check("列表", True)
except Exception as e:
    check(f"列表 - {e}", False)

try:
    assert {k: v for k, v in zip("abc", [1, 2, 3])} == {"a": 1, "b": 2, "c": 3}
    check("字典", True)
except Exception as e:
    check(f"字典 - {e}", False)

try:
    s = {1, 2, 3} & {2, 3, 4}
    assert s == {2, 3}
    check("集合", True)
except Exception as e:
    check(f"集合 - {e}", False)

# ---- 4. 函数与类 ----
print("\n[4] 函数与类")

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

try:
    assert factorial(5) == 120
    check("递归函数", True)
except Exception as e:
    check(f"递归函数 - {e}", False)

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

try:
    head = Node(100, Node(200))
    assert head.val == 100 and head.nxt.val == 200
    check("链表类", True)
except Exception as e:
    check(f"链表类 - {e}", False)

# ---- 5. 第三方库 ----
print("\n[5] 第三方库检测（pip / conda 安装的包）")

has_numpy = False
try:
    import numpy as np
    has_numpy = True
    a = np.array([[1, 2], [3, 4]])
    b = np.linalg.inv(a)
    print(f"  {PASS} NumPy    {np.__version__}  — 矩阵求逆 OK")
except ImportError:
    print(f"  {WARN} NumPy    未安装 (conda install numpy)")

try:
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    assert df["A"].sum() == 6
    print(f"  {PASS} Pandas   {pd.__version__}  — DataFrame OK")
except ImportError:
    print(f"  {WARN} Pandas   未安装 (conda install pandas)")

try:
    import matplotlib
    matplotlib.use("Agg")  # 无 GUI 后端，仅测试导入
    import matplotlib.pyplot as plt
    print(f"  {PASS} Matplotlib {matplotlib.__version__}  — 导入 OK")
except ImportError:
    print(f"  {WARN} Matplotlib 未安装 (conda install matplotlib)")

try:
    import scipy
    print(f"  {PASS} SciPy    {scipy.__version__}")
except ImportError:
    print(f"  {WARN} SciPy    未安装 (conda install scipy)")

# ---- 6. conda 环境 ----
print("\n[6] conda 环境")

try:
    result = subprocess.run(
        ["conda", "--version"],
        capture_output=True, text=True, timeout=10
    )
    if result.returncode == 0:
        print(f"  {PASS} conda    {result.stdout.strip()}")
    else:
        print(f"  {FAIL} conda 返回非零")
except FileNotFoundError:
    print(f"  {FAIL} conda 命令不可用（请检查环境变量或使用 Anaconda Prompt）")
except Exception as e:
    print(f"  {FAIL} conda - {e}")

try:
    result = subprocess.run(
        ["conda", "env", "list"],
        capture_output=True, text=True, timeout=10
    )
    if result.returncode == 0:
        lines = [l for l in result.stdout.splitlines() if l.strip() and not l.startswith("#")]
        if lines:
            envs = [l.split()[0] for l in lines]
            print(f"  {PASS} 虚拟环境: {', '.join(envs)}")
    else:
        print(f"  {FAIL} 无法列出环境")
except Exception as e:
    print(f"  {WARN} conda env list - {e}")

# ---- 7. pip 能力 ----
print("\n[7] pip")

try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        capture_output=True, text=True, timeout=10
    )
    if result.returncode == 0:
        print(f"  {PASS} pip 可用")
    else:
        print(f"  {FAIL} pip 异常")
except Exception as e:
    print(f"  {FAIL} pip - {e}")

# ---- 总结 ----
print("\n" + "=" * 60)
has_core = (has_numpy)
print("所有检测完成。")
print("WARN 表示当前环境未安装该库，可根据需要手动安装。")
print("如果各项 PASS / WARN 正常显示，则环境配置成功。")
print("=" * 60)

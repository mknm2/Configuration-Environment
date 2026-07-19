# VS Code 开发环境配置指南

Windows + VS Code 下搭建 C/C++、LaTeX、Python 三大开发环境的**手把手配置教程**，附带测试文件和开箱配置。

## 目录

| 模块 | 路径 | 指南 | 测试文件 |
|------|------|------|----------|
| C/C++ | [C C++ VSCode/](C%20C++%20VSCode/) | [Method1.md](C%20C++%20VSCode/Method1.md) | `114514.c` |
| LaTeX | [Latex-VSCode/](Latex-VSCode/) | [Method1.md](Latex-VSCode/Method1.md) | `114514.tex` |
| Python | [Python VSCode Miniconda/](Python%20VSCode%20Miniconda/) | [3.md](Python%20VSCode%20Miniconda/3.md) | `114514.py` |

## 快速开始

### C/C++

1. 阅读 [C C++ VSCode/Method1.md](C%20C++%20VSCode/Method1.md) 完成编译器和扩展安装
2. 打开 `114514.c`，编译运行
3. 输出 `Hello, World!` 即配置成功

### LaTeX

1. 阅读 [Latex-VSCode/Method1.md](Latex-VSCode/Method1.md) 完成 TeX Live 和扩展安装
2. 将 `114514.json` 的内容复制到 VS Code 工作区 `settings.json`
3. 打开 `114514.tex`，使用食谱 **XeLaTeX** 编译
4. 生成 PDF 即配置成功

### Python

1. 阅读 [Python VSCode Miniconda/3.md](Python%20VSCode%20Miniconda/3.md) 完成 Miniconda 安装和授权
2. 运行 `114514.py`：`python 114514.py`
3. 各检测项显示 `[PASS]` 即配置成功

## 项目结构

```
├── C C++ VSCode/
│   ├── Method1.md          # C/C++ 环境搭建教程
│   ├── 114514.c            # 测试代码：双向链表
│   └── *.png               # 教程配图
├── Latex-VSCode/
│   ├── Method1.md          # LaTeX 环境搭建教程
│   ├── 114514.json         # LaTeX Workshop 开箱配置
│   ├── 1.tex               # 测试文档：全功能示例
│   └── *.png               # 教程配图
├── Python VSCode Miniconda/
│   ├── 3.md                # Python/Conda 环境搭建教程 + 命令速查
│   ├── 114514.py           # 测试脚本：环境检测
│   └── *.png               # 教程配图
├── .gitignore
└── README.md
```

## 约定

- 所有教程面向 **Windows** 平台
- 编译器 / 工具版本以教程中注明的为准
- 路径中请勿使用中文，避免编译报错

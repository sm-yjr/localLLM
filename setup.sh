#!/bin/bash

# 检查 python3 命令是否存在
if ! command -v python3 &> /dev/null; then
    echo "错误: 需要安装 Python 3"
    exit 1
fi

# 创建虚拟环境
echo "创建虚拟环境..."
python3 -m venv .venv

# 激活虚拟环境
echo "激活虚拟环境..."
source .venv/bin/activate

# 升级 pip
echo "升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt

echo "设置完成！"
echo "使用 'source .venv/bin/activate' 来激活虚拟环境" 

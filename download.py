#!/usr/bin/env python3
"""
通用依赖下载脚本
用于为指定 Python 版本和平台下载 pip 包
"""

import subprocess
import argparse
import sys
import os

# 定义依赖列表
DEPENDENCIES = [
    "anthropic>=0.49.0",
    "beautifulsoup4>=4.13.3",
    "dynaconf>=3.2.10",
    "openai>=1.68.2",
    "pandas>=2.2.3",
    "prompt-toolkit>=3.0.51",
    "pygments>=2.19.2",
    "requests>=2.32.3",
    "rich>=13.9.4",
    "seaborn>=0.13.2",
    "term-image>=0.7.2",
    "tomli-w>=1.2.0",
    "tomli>=1.2.0",
    "qrcode>=8.1",
    "loguru>=0.7.3",
    "questionary>=2.1.0",
    "mcp[cli]>=1.10.0",
    "openpyxl>=3.1.5",
    "pyyaml>=6.0.2",
    "jinja2>=3.1.6",
    "charset-normalizer>=3.4.2",
    "fastapi>=0.116.1",
    "psutil>=7.0.0",
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=5.0.0",
    "pytest-mock>=3.14.0",
    "pytest-timeout>=2.3.0",
    "pytest-xdist>=3.6.0",
    "ruff>=0.8.0",
    "hatchling",
    "hatch-vcs>=0.5.0",
    "editables~=0.3"
]

def main():
    parser = argparse.ArgumentParser(description="下载指定依赖的 wheel 包")
    parser.add_argument("--dest", "-d", default="./packages", help="下载目标目录 (默认: ./packages)")
    parser.add_argument("--platform", default="manylinux_2_17_x86_64", help="目标平台 (默认: manylinux_2_17_x86_64)")
    parser.add_argument("--python-version", default="311", help="Python 版本 (如 310, 311, 313，默认: 313)")
    parser.add_argument("--index-url", default=None, help="PyPI 镜像源")

    args = parser.parse_args()

    # 构建 pip download 命令
    cmd_base = [
        sys.executable, "-m", "pip", "download",
        "-d", args.dest,
        "--platform", args.platform,
        "--only-binary=:all:",
        "--python-version", args.python_version
    ]

    if args.index_url:
        cmd_base += ["--index-url", args.index_url]

    # 确保目标目录存在
    os.makedirs(args.dest, exist_ok=True)

    print(f"🎯 将为 Python {args.python_version} 下载依赖到 {args.dest} (平台: {args.platform})")
    print(f"📦 共 {len(DEPENDENCIES)} 个依赖")

    success_count = 0
    for dep in DEPENDENCIES:
        print(f"\n📥 正在下载: {dep}")
        cmd = cmd_base + [dep]
        try:
            subprocess.check_call(cmd)
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"❌ 下载失败: {dep}, 错误: {e}")

    print(f"\n✅ 下载完成！成功: {success_count}/{len(DEPENDENCIES)}")

if __name__ == "__main__":
    main()
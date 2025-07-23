#!/usr/bin/env python3
"""
检查Python依赖是否正确安装
"""

import sys
import importlib

# 必需的Python依赖
REQUIRED_PACKAGES = [
    'llama_index',
    'llama_index.core',
    'llama_index.embeddings.openai',
    'llama_index.llms.openai',
    'llama_index.storage.storage_context',
    'llama_index.storage.docstore',
    'llama_index.storage.index_store',
    'llama_index.storage.vector_store',
    'openai',
    'nest_asyncio'
]

def check_package(package_name):
    """检查单个包是否可导入"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} - 可用")
        return True
    except ImportError as e:
        print(f"❌ {package_name} - 不可用: {e}")
        return False

def main():
    """主检查函数"""
    print("🐍 检查Python依赖...")
    print(f"Python版本: {sys.version}")
    
    success_count = 0
    total_count = len(REQUIRED_PACKAGES)
    
    for package in REQUIRED_PACKAGES:
        if check_package(package):
            success_count += 1
    
    print(f"\n📊 依赖检查结果: {success_count}/{total_count} 可用")
    
    if success_count == total_count:
        print("✅ 所有Python依赖都已正确安装")
        return 0
    else:
        print("⚠️ 部分Python依赖缺失，系统将使用回退模式")
        return 1

if __name__ == "__main__":
    sys.exit(main())
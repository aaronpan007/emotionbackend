#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查Python依赖是否正确安装
用于生产环境启动前的预检查
"""

import sys
import json

def check_dependencies():
    """检查所需的Python依赖"""
    dependencies = [
        'llama_index',
        'llama_index.core', 
        'llama_index.embeddings.huggingface',
        'dotenv',
        'pathlib',
        'logging',
        'collections',
        're',
        'nltk'
    ]
    
    results = {
        'success': True,
        'installed': [],
        'missing': [],
        'python_version': sys.version
    }
    
    for dep in dependencies:
        try:
            if '.' in dep:
                # 处理子模块导入
                parts = dep.split('.')
                module = __import__(parts[0])
                for part in parts[1:]:
                    module = getattr(module, part)
            else:
                __import__(dep)
            results['installed'].append(dep)
        except ImportError as e:
            results['missing'].append({'name': dep, 'error': str(e)})
            results['success'] = False
    
    return results

if __name__ == "__main__":
    try:
        result = check_dependencies()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0 if result['success'] else 1)
    except Exception as e:
        error_result = {
            'success': False,
            'error': str(e),
            'python_version': sys.version
        }
        print(json.dumps(error_result, indent=2, ensure_ascii=False))
        sys.exit(1)
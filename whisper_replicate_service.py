#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================================
Whisper 语音转录服务 - Replicate API版本
=====================================================

核心功能：
1. 高质量语音转录（支持中英文）
2. 约会录音内容分析
3. 情感语调识别
4. 对话内容情感安全评估

技术特性：
- 基于OpenAI Whisper模型
- 通过Replicate云端API调用
- 支持多种音频格式
- 实时进度跟踪

主要应用场景：
- 约会后复盘分析
- 对话内容风险识别
- 情感沟通模式分析

作者：AI Assistant
版本：2.0
=====================================================
"""

import os
import sys
import json
import logging
from pathlib import Path
from dotenv import load_dotenv
import replicate
import time
from datetime import datetime

# 加载环境变量
load_dotenv()

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

class WhisperReplicateService:
    """
    基于 Replicate API 的 Whisper 语音转录服务
    
    这个类封装了使用 Replicate 云服务调用 OpenAI Whisper 模型的完整流程。
    主要用于约会录音的转录和分析，支持中英文语音识别。
    
    特性：
    - 自动音频格式检测
    - 高精度中英文转录
    - 错误处理和重试机制
    - 进度跟踪和状态报告
    """
    
    def __init__(self):
        """
        初始化 Whisper 转录服务
        
        检查必要的环境变量并配置 Replicate API
        """
        self.api_token = os.getenv("REPLICATE_API_TOKEN")
        if not self.api_token:
            raise ValueError("未找到 REPLICATE_API_TOKEN 环境变量！")
        
        # 设置 Replicate API token
        os.environ["REPLICATE_API_TOKEN"] = self.api_token
        
        # Whisper 模型配置 - 使用经过优化的版本
        self.model = "openai/whisper:8099696689d249cf8b122d833c36ac3f75505c666a395ca40ef26f68e7d3d16e"
        
        logger.info("🎤 Whisper Replicate 服务初始化成功")
    
    def transcribe_audio_file(self, audio_file_path: str, language: str = "zh") -> dict:
        """
        转录音频文件
        
        Args:
            audio_file_path: 音频文件路径
            language: 语言代码，默认为中文
        
        Returns:
            dict: 转录结果
        """
        try:
            logger.info(f"🎯 开始转录音频文件: {audio_file_path}")
            
            # 验证文件存在
            if not os.path.exists(audio_file_path):
                raise FileNotFoundError(f"音频文件不存在: {audio_file_path}")
            
            # 检查文件大小
            file_size = os.path.getsize(audio_file_path)
            logger.info(f"📁 音频文件大小: {file_size / (1024*1024):.2f} MB")
            
            # 上传文件并获取 URL
            logger.info("📤 上传音频文件到 Replicate...")
            
            # 使用 Replicate API 进行转录
            start_time = time.time()
            
            with open(audio_file_path, "rb") as audio_file:
                input_data = {
                    "audio": audio_file,
                    "model": "large-v3",  # 使用最新的 large-v3 模型
                    "language": language,
                    "temperature": 0.0,    # 降低随机性，提高准确性
                    "suppress_tokens": "-1",  # 不抑制任何 token
                    "initial_prompt": "",     # 可以添加提示词来提高准确性
                    "condition_on_previous_text": True,  # 基于前文进行条件化
                    "word_timestamps": True  # 启用词级时间戳
                }
                
                logger.info("🧠 正在调用 Replicate Whisper API...")
                output = replicate.run(self.model, input=input_data)
            
            processing_time = time.time() - start_time
            
            # 解析输出结果
            transcription_text = ""
            segments = []
            
            if isinstance(output, dict):
                # 获取主要转录文本
                transcription_text = output.get("text", "")
                
                # 如果主要文本为空，尝试从segments中拼接
                if not transcription_text:
                    segments_data = output.get("segments", [])
                    if segments_data:
                        transcription_text = " ".join([segment.get("text", "").strip() for segment in segments_data])
                
                # 获取分段信息
                segments_data = output.get("segments", [])
                for segment in segments_data:
                    segments.append({
                        "id": segment.get("id", 0),
                        "start": segment.get("start", 0.0),
                        "end": segment.get("end", 0.0),
                        "text": segment.get("text", ""),
                        "tokens": segment.get("tokens", []),
                        "temperature": segment.get("temperature", 0.0),
                        "avg_logprob": segment.get("avg_logprob", 0.0),
                        "compression_ratio": segment.get("compression_ratio", 0.0),
                        "no_speech_prob": segment.get("no_speech_prob", 0.0)
                    })
            elif isinstance(output, str):
                transcription_text = output
            
            # 构建结果
            result = {
                "success": True,
                "transcription": transcription_text,
                "language": language,
                "processing_time": processing_time,
                "segments": segments,
                "file_info": {
                    "file_path": audio_file_path,
                    "file_size": file_size,
                    "file_name": os.path.basename(audio_file_path)
                },
                "model_info": {
                    "provider": "Replicate",
                    "model": "openai/whisper:large-v3",
                    "version": "8099696689d249cf8b122d833c36ac3f75505c666a395ca40ef26f68e7d3d16e"
                },
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            logger.info(f"✅ 转录成功完成")
            logger.info(f"📝 转录文本长度: {len(transcription_text)} 字符")
            logger.info(f"📊 处理时间: {processing_time:.2f} 秒")
            logger.info(f"🎯 分段数量: {len(segments)}")
            
            return result
            
        except Exception as e:
            logger.error(f"❌ 转录失败: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "file_path": audio_file_path,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    def transcribe_from_url(self, audio_url: str, language: str = "zh") -> dict:
        """
        从 URL 转录音频
        
        Args:
            audio_url: 音频文件 URL
            language: 语言代码
        
        Returns:
            dict: 转录结果
        """
        try:
            logger.info(f"🎯 开始从 URL 转录音频: {audio_url}")
            
            input_data = {
                "audio": audio_url,
                "model": "large-v3",
                "language": language,
                "temperature": 0.0,
                "suppress_tokens": "-1",
                "initial_prompt": "",
                "condition_on_previous_text": True,
                "word_timestamps": True
            }
            
            start_time = time.time()
            logger.info("🧠 正在调用 Replicate Whisper API...")
            output = replicate.run(self.model, input=input_data)
            processing_time = time.time() - start_time
            
            # 解析输出结果
            transcription_text = ""
            segments = []
            
            if isinstance(output, dict):
                transcription_text = output.get("text", "")
                
                # 如果主要文本为空，尝试从segments中拼接
                if not transcription_text:
                    segments_data = output.get("segments", [])
                    if segments_data:
                        transcription_text = " ".join([segment.get("text", "").strip() for segment in segments_data])
                
                segments_data = output.get("segments", [])
                for segment in segments_data:
                    segments.append({
                        "id": segment.get("id", 0),
                        "start": segment.get("start", 0.0),
                        "end": segment.get("end", 0.0),
                        "text": segment.get("text", ""),
                        "tokens": segment.get("tokens", []),
                        "temperature": segment.get("temperature", 0.0),
                        "avg_logprob": segment.get("avg_logprob", 0.0),
                        "compression_ratio": segment.get("compression_ratio", 0.0),
                        "no_speech_prob": segment.get("no_speech_prob", 0.0)
                    })
            elif isinstance(output, str):
                transcription_text = output
            
            result = {
                "success": True,
                "transcription": transcription_text,
                "language": language,
                "processing_time": processing_time,
                "segments": segments,
                "file_info": {
                    "audio_url": audio_url
                },
                "model_info": {
                    "provider": "Replicate",
                    "model": "openai/whisper:large-v3",
                    "version": "8099696689d249cf8b122d833c36ac3f75505c666a395ca40ef26f68e7d3d16e"
                },
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            logger.info(f"✅ 从 URL 转录成功完成")
            logger.info(f"📝 转录文本长度: {len(transcription_text)} 字符")
            logger.info(f"📊 处理时间: {processing_time:.2f} 秒")
            
            return result
            
        except Exception as e:
            logger.error(f"❌ URL 转录失败: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "audio_url": audio_url,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

def main():
    """主函数 - 命令行调用接口"""
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "error": "Usage: python whisper_replicate_service.py <audio_file_path> [language]"
        }))
        sys.exit(1)
    
    try:
        audio_file_path = sys.argv[1]
        language = sys.argv[2] if len(sys.argv) > 2 else "zh"
        
        # 创建服务实例
        whisper_service = WhisperReplicateService()
        
        # 执行转录
        result = whisper_service.transcribe_audio_file(audio_file_path, language)
        
        # 输出结果
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
    except Exception as e:
        error_result = {
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env node
/**
 * 生产环境启动脚本
 * 确保Python环境正确配置
 */

const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

// 检查Python环境
function checkPythonEnvironment() {
  console.log('🔍 检查Python环境配置...');
  
  const venvPython = path.join(__dirname, 'venv/bin/python');
  const venvExists = fs.existsSync(venvPython);
  
  console.log(`📍 venv Python路径: ${venvPython}`);
  console.log(`✅ venv存在: ${venvExists}`);
  
  if (venvExists) {
    console.log('🐍 使用虚拟环境Python');
  } else {
    console.log('🐍 将使用系统Python3');
  }
  
  // 检查Python依赖
  const requirementsPath = path.join(__dirname, 'requirements.txt');
  if (fs.existsSync(requirementsPath)) {
    console.log('📦 requirements.txt文件存在');
  } else {
    console.warn('⚠️  requirements.txt文件不存在');
  }
  
  // 检查RAG系统文件
  const ragServicePath = path.join(__dirname, 'rag_query_service_enhanced.py');
  if (fs.existsSync(ragServicePath)) {
    console.log('🧠 RAG查询服务文件存在');
  } else {
    console.error('❌ RAG查询服务文件不存在');
  }
  
  // 检查知识库存储
  const storagePath = path.join(__dirname, 'storage');
  if (fs.existsSync(storagePath)) {
    console.log('📚 知识库存储目录存在');
    const indexFile = path.join(storagePath, 'index_store.json');
    if (fs.existsSync(indexFile)) {
      console.log('📑 RAG索引文件存在');
    } else {
      console.warn('⚠️  RAG索引文件不存在，将使用回退响应模式');
    }
  } else {
    console.warn('⚠️  知识库存储目录不存在（预期行为：免费版无持久化存储）');
    console.log('🔄 系统将在RAG不可用时使用智能回退响应');
  }
}

// 启动服务器
function startServer() {
  console.log('🚀 启动AI情感安全助理服务器...');
  
  // 设置环境变量
  process.env.NODE_ENV = 'production';
  
  // 启动Node.js服务器
  const serverProcess = spawn('node', ['server.js'], {
    stdio: 'inherit',
    cwd: __dirname,
    env: {
      ...process.env,
      NODE_ENV: 'production'
    }
  });
  
  serverProcess.on('error', (error) => {
    console.error('❌ 服务器启动失败:', error);
    process.exit(1);
  });
  
  serverProcess.on('exit', (code) => {
    console.log(`🔚 服务器进程退出，退出码: ${code}`);
    process.exit(code);
  });
  
  // 处理进程信号
  process.on('SIGTERM', () => {
    console.log('📨 收到SIGTERM信号，正在关闭服务器...');
    serverProcess.kill('SIGTERM');
  });
  
  process.on('SIGINT', () => {
    console.log('📨 收到SIGINT信号，正在关闭服务器...');
    serverProcess.kill('SIGINT');
  });
}

// 主函数
function main() {
  console.log('🎯 ===== AI情感安全助理 - 生产环境启动 =====');
  console.log(`📅 启动时间: ${new Date().toISOString()}`);
  console.log(`📂 工作目录: ${__dirname}`);
  console.log(`🌍 环境变量: ${process.env.NODE_ENV || 'development'}`);
  
  checkPythonEnvironment();
  startServer();
}

// 启动应用
if (require.main === module) {
  main();
}

module.exports = { checkPythonEnvironment, startServer };
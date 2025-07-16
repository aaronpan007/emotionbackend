# 后端 - AI情感安全助理 API

## 项目描述
Node.js + Express 后端API服务，提供AI分析和知识库查询功能。

## 核心功能
- 图片分析（GPT-4o Vision）
- 音频转录（Whisper）
- RAG知识库查询
- 异步任务管理

## 技术栈
- Node.js + Express
- OpenAI GPT-4o API
- Replicate API
- LlamaIndex (Python)
- Cloudflare R2

## 开发环境启动
```bash
# 安装Node.js依赖
npm install

# 安装Python依赖
pip install -r requirements.txt

# 构建知识库索引
python build_rag_system.py

# 启动服务器
npm run dev
```

## 生产环境部署
推送代码到GitHub后，在Render创建Web Service进行部署。

## 环境变量配置
```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=your_api_base_url
REPLICATE_API_TOKEN=your_replicate_token
CLOUDFLARE_R2_ACCESS_KEY_ID=your_r2_access_key
CLOUDFLARE_R2_SECRET_ACCESS_KEY=your_r2_secret_key
CLOUDFLARE_R2_BUCKET_NAME=your_bucket_name
CLOUDFLARE_R2_ENDPOINT=your_r2_endpoint
```

## API端点
- `POST /api/analyze-images` - 图片分析
- `POST /api/post-date-debrief` - 约会复盘
- `GET /api/task-status/:taskId` - 查询任务状态 
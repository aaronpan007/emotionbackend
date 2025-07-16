# 🚀 Render 平台部署指南

## 📋 部署前准备

### 1. 确保文件准备就绪
确认 `backend/` 目录包含以下文件：
- ✅ `render.yaml` - Render 部署配置
- ✅ `package.json` - Node.js 依赖配置
- ✅ `requirements.txt` - Python 依赖配置
- ✅ `server.js` - 主服务器文件
- ✅ `env.production.template` - 环境变量模板

### 2. 准备环境变量
请准备好以下 API 密钥和配置信息：
- `OPENAI_API_KEY` - OpenAI API 密钥
- `REPLICATE_API_TOKEN` - Replicate API 令牌
- `CLOUDFLARE_R2_*` - Cloudflare R2 存储配置（如果使用）

---

## 🛠️ Render 部署步骤

### 方法一：通过 render.yaml 一键部署（推荐）

1. **推送代码到 GitHub**
   ```bash
   # 在 backend/ 目录下
   git init
   git add .
   git commit -m "Initial backend deployment"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-backend-repo.git
   git push -u origin main
   ```

2. **访问 Render 官网**
   - 打开 [render.com](https://render.com)
   - 点击 "Get Started" 或 "Sign Up"
   - 使用 GitHub 账号登录

3. **创建新服务**
   - 在 Dashboard 点击 "New +"
   - 选择 "Blueprint"
   - 连接你的 GitHub 仓库
   - 选择包含 `render.yaml` 的仓库

4. **配置部署**
   - Render 会自动读取 `render.yaml` 配置
   - 确认服务名称：`ai-emotional-safety-backend`
   - 确认分支：`main`
   - 点击 "Apply"

### 方法二：手动创建 Web Service

1. **创建 Web Service**
   - 在 Dashboard 点击 "New +"
   - 选择 "Web Service"
   - 连接 GitHub 仓库

2. **基本配置**
   ```
   Name: ai-emotional-safety-backend
   Runtime: Node
   Build Command: npm install && pip install -r requirements.txt
   Start Command: npm start
   Plan: Free (或根据需要选择付费计划)
   ```

3. **高级设置**
   ```
   Node Version: 18
   Health Check Path: /api/health
   ```

---

## 🔧 环境变量配置

在 Render Dashboard 的 "Environment" 标签页中，添加以下环境变量：

### 必需变量
```
OPENAI_API_KEY = sk-your-actual-openai-api-key
OPENAI_API_BASE = https://api.openai.com/v1
REPLICATE_API_TOKEN = r8_your-actual-replicate-token
NODE_ENV = production
```

### 可选变量（如果使用 Cloudflare R2）
```
CLOUDFLARE_R2_ACCESS_KEY_ID = your-r2-access-key
CLOUDFLARE_R2_SECRET_ACCESS_KEY = your-r2-secret-key
CLOUDFLARE_R2_BUCKET_NAME = your-bucket-name
CLOUDFLARE_R2_ENDPOINT = https://your-account-id.r2.cloudflarestorage.com
```

### CORS 配置
```
FRONTEND_URL = https://your-frontend-app.vercel.app
```

---

## 📊 部署监控

### 1. 检查部署状态
- 在 Render Dashboard 查看 "Events" 标签
- 观察构建日志中的成功消息
- 确认服务状态为 "Live"

### 2. 测试 API 端点
部署成功后，测试以下端点：

```bash
# 健康检查
curl https://your-app-name.onrender.com/api/health

# RAG 系统状态
curl https://your-app-name.onrender.com/api/rag-status
```

### 3. 查看日志
- 在 Render Dashboard 的 "Logs" 标签查看实时日志
- 确认看到类似以下的启动消息：
  ```
  🚀 AI情感安全助理 API服务器已启动
  📡 服务地址: https://your-app.onrender.com
  ✅ RAG知识库系统: 已就绪
  ```

---

## 🔒 安全注意事项

1. **环境变量安全**
   - 绝不在代码中硬编码 API 密钥
   - 定期轮换 API 密钥
   - 使用最小权限原则

2. **域名配置**
   - 在生产环境中正确配置 CORS
   - 限制前端域名访问

3. **监控和告警**
   - 设置 Render 的邮件通知
   - 监控 API 使用量和费用

---

## 🐛 常见问题排查

### 构建失败
- 检查 `package.json` 中的依赖版本
- 确认 `requirements.txt` 中的 Python 包可安装
- 查看构建日志中的具体错误信息

### 服务启动失败
- 检查端口配置（Render 自动设置 PORT 环境变量）
- 确认所有必需的环境变量已设置
- 查看应用日志中的错误信息

### API 调用失败
- 验证 OpenAI API 密钥是否有效
- 检查 CORS 配置是否正确
- 确认前端 API 调用地址是否正确

### 知识库相关问题
- 确认 Cloudflare R2 配置正确
- 检查知识库文件是否已上传
- 验证 Python 依赖是否安装成功

---

## 📞 支持

如果遇到问题：
1. 查看 Render 官方文档：[render.com/docs](https://render.com/docs)
2. 检查本项目的 `backend/README.md`
3. 查看应用日志获取详细错误信息

---

## 🎉 部署成功后

1. **更新前端配置**
   - 将 Render 提供的 URL 添加到前端的环境变量中
   - 格式：`https://your-app-name.onrender.com`

2. **测试完整流程**
   - 上传测试图片
   - 进行约会复盘分析
   - 验证所有功能正常

3. **配置自定义域名**（可选）
   - 在 Render Dashboard 中添加自定义域名
   - 配置 DNS 记录

恭喜！你的 AI 情感安全助理后端服务已成功部署到 Render 平台！🎊 
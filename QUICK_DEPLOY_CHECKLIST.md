# 🚀 Render 快速部署检查清单

## ✅ 部署前检查

- [ ] 确认 `render.yaml` 文件存在
- [ ] 确认 `package.json` 配置正确
- [ ] 确认 `requirements.txt` 存在
- [ ] 准备好 OpenAI API Key
- [ ] 准备好 Replicate API Token

## 📝 5分钟快速部署步骤

### 1. 推送到 GitHub（2分钟）
```bash
git init
git add .
git commit -m "Backend ready for Render deployment"
git remote add origin https://github.com/yourusername/your-backend-repo.git
git push -u origin main
```

### 2. Render 配置（3分钟）
1. 访问 [render.com](https://render.com) 并登录
2. 点击 "New +" → "Blueprint"
3. 选择你的 GitHub 仓库
4. Render 自动读取 `render.yaml` 配置
5. 点击 "Apply"

### 3. 设置环境变量（1分钟）
在 Render Dashboard 添加：
```
OPENAI_API_KEY = sk-your-actual-key
REPLICATE_API_TOKEN = r8-your-actual-token
NODE_ENV = production
```

### 4. 验证部署
等待构建完成后，访问：
```
https://your-app-name.onrender.com/api/health
```

## 🔗 获取后端URL

部署成功后，你的后端URL格式为：
```
https://ai-emotional-safety-backend.onrender.com
```

将此URL配置到你的前端环境变量中！

---
*预计总部署时间：5-10分钟* ⏱️ 
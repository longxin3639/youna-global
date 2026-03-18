# GitHub 上传指南

## 📦 需要上传的文件

### 核心 HTML 文件
- ✅ `index.html` - 首页
- ✅ `about.html` - About 页面
- ✅ `services.html` - Services 页面
- ✅ `contact.html` - Contact 页面

### 资源文件
- ✅ `assets/` - 包含所有图片、CSS 和 JavaScript
  - `style.css` - 主样式表
  - `script.js` - JavaScript 脚本
  - `*.png` - 所有 logo 和图标（28 个）
  - `*.jpg` - 图片资源

### SEO 文件
- ✅ `robots.txt` - SEO robots 配置
- ✅ `sitemap.xml` - 网站地图

## ⚠️ 不需要上传的文件

- ❌ `update_icons.py` - Python 工作脚本
- ❌ `test-menu.html` - 测试文件
- ❌ `.workbuddy/` - WorkBuddy 项目配置
- ❌ 任何 `.md` 开头的工作文档

## 📤 上传步骤

### 方法 1: 使用 Git 命令（推荐）

```bash
# 1. 进入项目目录
cd C:\Users\kls-dy\WorkBuddy\20260317150741

# 2. 初始化 git（如果还没有）
git init

# 3. 添加远程仓库
git remote add origin https://github.com/longxin3639/youna-global.git

# 4. 添加所有需要的文件
git add index.html about.html services.html contact.html robots.txt sitemap.xml
git add assets/

# 5. 创建首次提交
git commit -m "Initial commit: youna-global website"

# 6. 推送到 GitHub
git push -u origin main
```

### 方法 2: 手动上传

1. 访问 https://github.com/longxin3639/youna-global
2. 点击 "Add file" → "Upload files"
3. 选择以下文件夹和文件上传：
   - 根目录的所有 `.html` 文件
   - `robots.txt`
   - `sitemap.xml`
   - `assets/` 整个文件夹

## ✨ 文件准备完成

所有核心文件都已准备好，现在可以按上述步骤上传到 GitHub 了！

---
**最后更新**: 2026-03-18

# blitz.cloud

- **原链接：** <https://blitz.cloud/>
- **分类：** 免费资源
- **标签：** `容器` `Docker` `免费托管` `欧盟`
- **收录日期：** 2026-11-05

## 这是什么

blitz.cloud 是德国雷根斯堡软件公司 BlitzWorks 运营的应用托管平台，服务器和备份都在欧盟境内。注册后你会得到一个属于自己的子域名地址（如 名字.prod.page），可以一键安装应用商店里的开源应用、运行任意公开 Docker 镜像，或从 GitHub 等仓库自动构建部署。它与 Blitz.js、StackBlitz 无关。

## 主要功能 / 要点

- 免费版：0 欧元、无需信用卡、无期限，5 个应用、512MB 内存、10GB 存储、1 个托管数据库，备份保留 7 晚
- 应用商店 119 个开源应用（WordPress、Ghost、Vaultwarden、n8n、Open WebUI 等）一键安装
- 支持 Docker Hub / ghcr.io 公开镜像（需 amd64），以及 GitHub、GitLab、Codeberg、Gitea 仓库推送即部署，没有 Dockerfile 会自动生成
- 托管 PostgreSQL 17、MariaDB 11.4、Redis（Valkey 8），自动 HTTPS
- 每个应用独立 gVisor 沙箱、默认拒绝的网络策略、加密环境变量与备份，支持通行密钥和两步验证
- 可通过 MCP 让 Claude、ChatGPT、Cursor 等 AI 助手帮你部署和查日志

## 适合谁

想免费自建博客、密码管理器、监控面板、n8n 自动化等小服务，或在意数据留在欧盟的个人用户和开发者。

## 怎么用

1. 在官网点“Deploy your app”注册，领取自己的地址
2. 选择应用商店的应用、填 Docker 镜像名，或连接 GitHub 仓库
3. 等待页面显示上线，拿到 https 链接即可使用

## 注意事项

- 需注册账号；免费版应用 15 分钟无人访问会休眠，下次访问再唤醒，需要 7×24 在线、自定义域名需升级 Pro（7 欧元/月）
- 免费版控制台会展示 Google 广告
- 免费套餐条款可能调整，重要数据请自行额外备份
- 托管 Vaultwarden 等敏感服务时务必开启两步验证并设置强密码

---

[← 返回导航首页](../../README.md)

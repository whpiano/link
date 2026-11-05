# Cloudflare-Tunnel-Panel

- **原链接：** https://github.com/eooce/Cloudflare-Tunnel-Panel
- **分类：** GitHub 开源项目
- **标签：** `隧道` `Cloudflare` `Workers`
- **收录日期：** 2026-11-05

## 这是什么

eooce 开源的 Cloudflare Tunnel（Argo Tunnel）网页管理面板，GPL-3.0 协议。整个项目只有一个 `_worker.js` 文件（Worker 代码 + 内嵌管理页面），部署在 Cloudflare Workers 上，无需构建、无外部依赖，用来集中管理多个 Cloudflare 账号下的隧道。

## 主要功能 / 要点

- 密码登录，会话 Cookie 签名有效 7 天，登录接口有防爆破延时
- 多账号管理：顶栏切换账号，各账号的隧道、路由、提醒互相隔离
- 隧道列表与状态（在线 / 降级 / 离线 + 运行时长），新建、编辑、删除隧道，查看启动 Token
- 新建隧道时自动配置 DNS CNAME；支持多条"域名 + 路径 → 本地服务"路由
- 可选 Telegram 上下线提醒，状态变化才推送；可配 Cron 无人值守检查
- 支持 PWA，可装到桌面或手机主屏
- 存储推荐 D1，也可回退 KV

## 适合谁

用 Cloudflare Tunnel 做内网穿透、手里有多个账号或多条隧道，想要一个比官方后台更集中的管理界面的站长和自建服务玩家。

## 怎么用

在 Cloudflare Dashboard 创建 Worker，粘贴 `_worker.js` 内容；在设置中添加环境变量 `CF_API_TOKEN`、`CF_ACCOUNT_ID`、`PASSWORD`（可选绑定 D1 数据库）；部署后访问 Worker 域名输入密码登录。API Token 所需权限 README 中有详细表格。

## 注意事项

- 需要 Cloudflare 账号和托管在 Cloudflare 的域名；Workers、D1、KV 免费额度有限制
- 面板持有可编辑 DNS 和隧道的 API Token，隧道启动 Token 可被用来接管流量——务必设置强密码和 `SESSION_SECRET`，作者也建议加 Cloudflare Access 二次防护
- 部署前最好自己读一遍代码，第三方代码会接触你的账号凭据

---

[← 返回导航首页](../../README.md)

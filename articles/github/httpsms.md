# httpsms

- **原链接：** <https://github.com/NdoleStudio/httpsms>
- **分类：** GitHub 开源项目
- **标签：** `短信` `SMS 网关` `Android` `API`
- **收录日期：** 2026-11-05

## 这是什么

httpSMS 是 NdoleStudio 开源的项目（AGPL-3.0 协议，GitHub 约 6.3k Star），可以把你的安卓手机变成短信网关：你向一个简单的 HTTP API 发请求，手机就会代你发出短信；手机收到的短信也可以转发到你的 Webhook 地址。作者来自喀麦隆，因为当地难以购买虚拟号码，才做了这个用真实手机收发短信的方案。

项目包含三部分：安卓 App（Kotlin）、后端 API（Go + Fiber）和网页控制台（Nuxt），既有官方托管服务 httpsms.com，也可自行部署。

## 主要功能 / 要点

- 通过 HTTP API 发送短信，收到的短信转发到 Webhook
- 端到端加密（AES-256），密钥只存在手机上
- 发送限速（如每分钟 3 条），避免一次性群发
- 消息过期设置：手机未及时收到推送时可设超时并收到通知
- 提供 Go、JavaScript/TypeScript 客户端库
- 支持 Docker 自托管（需配置 Firebase、SMTP、Cloudflare Turnstile 等）

## 适合谁

- 需要程序化发送验证码、通知短信的个人开发者或小团队
- 所在地区难买虚拟号码、想用自己手机号收发短信的用户
- 想做短信自动化（如短信转发到服务器）的人

## 怎么用

1. 简单用法：在 httpsms.com 注册，在安卓手机安装官方 App 并登录，在网页设置中获取 API Key，然后调用 API 发短信。
2. 自托管：按 README 准备 Firebase 项目、SMTP 服务等，用 docker compose 构建运行，并自行编译安卓 App。

## 注意事项

- 使用官方托管服务需要注册账号，短信内容会经过其服务器（可开启端到端加密降低风险）；短信费用由你的手机卡运营商收取。
- App 需要短信收发权限，只从官方渠道（GitHub Releases 或官网）下载安装包。
- 请遵守当地法律和运营商规定，不要用于群发营销或骚扰短信，否则号码可能被封。

---

[← 返回导航首页](../../README.md)

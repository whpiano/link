# InstaBox

- **原链接：** <https://instabox.sh/>
- **分类：** 免费资源
- **标签：** `服务器` `VPS` `Agent 沙箱`
- **收录日期：** 2026-11-05

## 这是什么

InstaBox 是一个为 AI Agent 提供云端 Linux 机器（沙箱）的服务。每台机器是一个 Firecracker 微型虚拟机（Debian 13），默认 4 vCPU / 8 GiB 内存，带 20 GiB 持久化磁盘。可以通过 CLI、HTTP API、TypeScript / Python SDK 或 MCP 来创建机器、执行命令、传文件。

原导航站描述为「可以免费申请 5 个 VPS 供 agent 使用，30 分钟不使用就休眠」。但官网文档（llms.txt）目前写的免费计划限制是：**1 台机器、5 个快照**、闲置 30 分钟自动暂停、单次最长运行 480 分钟。「5 个」可能是旧政策或把快照数量误当成机器数，以官网为准。

## 主要功能 / 要点

- 默认模板 agent-browser：预装 Docker、Node.js、Bun、Python、Go、Rust、Java、桌面环境和 Chromium
- 免费计划还可使用 android 模板（容器方式运行 Android 14，可 adb 安装 APK）和 ci 模板
- 快照、Fork（秒级复制机器）、端口公开为 HTTPS 地址、SSH 登录、远程桌面
- 暂停时保留内存状态，可随时恢复
- 付费计划 Pro 每月 20 美元起，另按 CPU、内存、存储、流量用量计费

## 适合谁

- 需要给 Claude Code、Codex 等 Agent 一个隔离执行环境的开发者
- 想在云端快速起一台临时 Linux 机器做测试、跑浏览器自动化或测安卓 App 的人

## 怎么用

官网提供的快速开始方式是通过 npx 运行其 CLI 完成登录并创建机器，或在网页后台创建 API Key 后调用 HTTP API。具体命令请看官网文档（instabox.sh/docs）。

## 注意事项

- 需注册登录；免费档限 1 台机器，闲置 30 分钟自动休眠，免费政策可能随时调整。
- 官方快速开始命令会同时往本机 Claude / Gemini 等 Agent 的技能目录安装 skills，执行前请确认是否需要（可加参数跳过）。
- 不要在云端机器中存放未加密的重要密钥或隐私数据；API Key 泄露可能导致他人使用你的资源。

---

[← 返回导航首页](../../README.md)

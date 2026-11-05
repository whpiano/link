# Tailscale-Termux-CLI

- **原链接：** <https://github.com/bropines/tailscale-termux-cli>
- **分类：** GitHub 开源项目
- **标签：** `tailscale` `termux` `安卓`
- **收录日期：** 2026-11-05

## 这是什么

tailscale-termux-cli 是 bropines 维护的开源项目，提供打过补丁的官方 Tailscale CLI（tailscale 与 tailscaled），让它在 Android 11 及以上的 Termux 里以用户态网络运行，无需 Root 或 /dev/net/tun。

## 主要功能 / 要点

- 打包成 .deb 与 pacman 包，集成 termux-services，可随 Termux 会话自动启动守护进程
- 默认在 127.0.0.1:1055 开启带用户名密码认证的 SOCKS5 代理（凭据自动生成）
- 提供 tailscale-socks5、tailscale-test（诊断）、tailscaled-log 等辅助命令
- README 说明：Tailscale 1.104.0 起官方已原生支持 Termux，本项目剩余价值主要是完整网卡枚举、SOCKS5 认证与打包，未来可能归档

## 适合谁

想把安卓手机接入自己的 Tailscale 内网、或在手机上跑服务并远程访问的 Termux 用户。

## 怎么用

README 提供一行远程安装脚本，也可从 Releases 手动下载对应架构的包并校验 SHA256 或签名后安装；安装后执行 tailscale up 登录，用 tailscale status 查看状态。遇到问题先运行 tailscale-test。

## 注意事项

- 免费开源（Tailscale 源码为 BSD-3-Clause），使用需要 Tailscale 账号
- “curl | bash” 一行安装会直接执行远程脚本，建议先阅读脚本或用校验和/签名验证
- 节点会向控制面报告为 CLI 客户端（DeviceModel=Termux），公司 tailnet 可能有设备合规策略
- 安卓回环地址不按应用隔离，不要随意关闭 SOCKS5 认证，否则手机上任何 App 都能经代理进入你的内网
- 非 Tailscale 官方项目

---

[← 返回导航首页](../../README.md)

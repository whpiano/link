# ds-harness-remote

- **原链接：** <https://github.com/liguobao/ds-harness-remote/tree/main>
- **分类：** GitHub 开源项目
- **标签：** `dsh` `DeepSeek` `远程访问`
- **收录日期：** 2026-11-05

## 这是什么

ds-harness-remote 是 liguobao 开发的社区开源项目（MIT，约 1.8k 星），基于 DeepSeek Harness（DSH）插件机制。它让你用 PC、安卓、网页等客户端，通过端到端加密的 P2P 网络远程使用家里或公司电脑上的 DSH，以及 Codex、Cursor、Claude Code 等工作区。

## 主要功能 / 要点

- Host 端无需公网 IP 或端口映射，连接按 局域网 → P2P → TURN → Relay 依次回退
- 业务流量使用 Noise 协议端到端加密，项目称服务端只能看到必要的连接元数据
- 支持远程浏览工作区文件、远程终端、切换模型，多个客户端可同时连同一台 Host
- 客户端：DSH 桌面插件、Web、安卓 APK、iOS（TestFlight 内测）、Linux 一键安装

## 适合谁

日常用 DeepSeek Harness 或 Codex 等编程 Agent，想在外出时用手机或浏览器继续操作本机会话的开发者。

## 怎么用

在 DSH 桌面版的扩展/插件管理里从 npm 安装 README 标明的版本（写作时为 ds-harness-remote@0.6.3），重启后在侧边栏打开 Remote 并登录；另一台设备装同一插件或直接用 Web/安卓客户端登录同一账号，选择在线 Host 即可。

## 注意事项

- 默认使用项目方托管的服务器 dsh.r2049.cn，需要账号；账号密码注册需邀请码，也可用知乎/GitHub/Google 授权
- 远程终端以 Host 用户身份运行，账号一旦泄露等于电脑被远程控制，务必保管好账号并及时移除不用的设备
- Linux 安装器以 root 运行服务，README 提醒只对可信账号开放
- 非 DeepSeek 官方产品；也支持自建服务端

---

[← 返回导航首页](../../README.md)

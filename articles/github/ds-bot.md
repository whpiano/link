# DeepSeek-Bot（DS Bot）

- **原链接：** <https://github.com/Fei2411/DeepSeek-Bot>
- **分类：** GitHub 开源项目
- **标签：** `dsh` `Bot` `多智能体`
- **收录日期：** 2026-11-05

## 这是什么

DS Bot 是一个基于 DeepSeek Harness（DSH）的社区开源项目，既是 DSH 插件，也提供自带 DSH 的桌面应用。它把 DSH 变成一组长期存在的 Bot：有一个权限很高的“主 Bot”（Chief）帮你创建和管理其他 Bot，Bot 之间可以互发消息、拉群协作。原链接 Fei2411/DeepSeek-Bot 现已跳转到 Fei2411/DS-Bot，Apache-2.0 协议，约 5600 star。

## 主要功能 / 要点

- 主 Bot：管理其他 Bot 和群聊，第一次打开时引导你完成设置
- 群聊：每个群有管理员 Bot，可 @ 指定 Bot，Bot 之间可以互相派活；群有独立记忆，可按阶段跑“目标”任务
- Bot 记忆：记住你的偏好，可在详情页管理
- 能力库：共享 MCP 服务、技能包；本地 MCP 命令需你批准才能运行
- 用量统计、Office 文件（docx/pptx/xlsx）创建与编辑
- 数据保存在本机 DSH 目录（默认 ~/.dsh）

## 适合谁

已经在用或想尝试 DeepSeek Harness、想让多个 AI 角色分工协作（写作、编程等）的进阶用户。

## 怎么用

1. 桌面版：在 GitHub Releases 下载对应系统安装包（Windows exe、macOS zip、Linux AppImage/deb）
2. 插件版：在 DSH Desktop「插件 → 添加插件」中填包名 ds-bot 安装，并先在 DSH 里配置至少一个模型
3. 也可用 Docker 部署在 NAS 或服务器
4. 打开后先和主 Bot 对话，让它帮你建 Bot 和群聊

## 注意事项

- 需要 DeepSeek 账号或 API Key，DeepSeek 按用量计费；群聊协作会明显增加 Token 消耗
- 非 DeepSeek 官方产品；Windows 安装包目前未签名，会触发系统警告，README 建议核对 SHA256 后再信任
- Bot 可以读写文件、执行命令，主 Bot 权限很高，重要操作请自己把关；Docker 部署时只挂载必要目录
- 项目仍为预览版（v0.2 preview），可能有 bug

---

[← 返回导航首页](../../README.md)

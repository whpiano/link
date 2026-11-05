# DSH-Android

- **原链接：** https://github.com/jackwener/DSH-Android
- **分类：** GitHub 开源项目
- **标签：** `Android` `DeepSeek` `手机Agent` `开源`
- **收录日期：** 2026-11-05

## 这是什么

DSH-Android 是 GitHub 用户 jackwener 开源的安卓 App（Apache-2.0 协议），把 DeepSeek Harness（dsh）这个 AI Agent 引擎直接内嵌进 App 进程运行。装一个 APK，不需要 root、不需要电脑或 Termux，就能让 AI 替你在手机上读屏、操作 App、整理文件、修改系统设置、执行自动化任务。项目声明是社区项目，与 DeepSeek 官方无关联。

## 主要功能 / 要点

- 操作手机 App：基于无障碍服务读屏、点击、滑动、输入，示例包括发微信、抓取小红书内容、在招聘或购物 App 上操作
- 文件处理：查找、整理、重命名、压缩解压，能读 PDF / Word / Excel / PPT 文字
- 系统设置：亮度、音量、勿扰、闹钟、Wi-Fi、蓝牙、通知读取与回复、媒体控制
- 自动化：定时或按条件（连上 Wi-Fi、充电、到达某地、收到通知）触发任务
- 除 DeepSeek 外可接入 OpenAI、Claude、Gemini、Kimi、通义千问等或任意 OpenAI 兼容接口
- 可选 Shizuku，Android 14+ 支持在虚拟屏幕上操作的“不打扰模式”；也可远程连接电脑上的 dsh

## 适合谁

想体验“手机 Agent”的安卓用户、AI 爱好者，以及想研究 Agent 在移动端落地的开发者。

## 怎么用

1. 从项目 Releases 页面下载 APK（仅支持 Android 10 及以上、arm64 设备，安装包约 110 MB）
2. 登录 DeepSeek 账号或填入 API Key，也可在设置里添加其他模型服务商
3. 用自然语言下达任务，App 会在需要时引导开启相应权限
4. 可选：在设置中安装并启用 Shizuku 解锁更多系统能力

## 注意事项

- 需要 DeepSeek 账号或 API Key，调用模型会产生 API 费用
- App 需要无障碍、通知读取、短信等高敏感权限，能看到屏幕内容和聊天信息，隐私风险较高，建议不要在装有重要账户的主力机上随意授权
- 不在 Google Play 分发，安装时可能被 Play 保护机制拦截；只从官方 Releases 下载，并核对发布说明中的 SHA-256
- 让 AI 代为发消息、下单、投简历等操作可能误操作或违反对应 App 的用户协议，务必全程留意、随时可暂停
- README 中提到可关闭 adb 安装校验的命令，这会降低系统安全防护，非必要不要执行

---

[← 返回导航首页](../../README.md)

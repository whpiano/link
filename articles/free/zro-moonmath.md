# Zro

- **原链接：** <https://zro.moonmath.ai/>
- **分类：** 免费资源
- **标签：** `白嫖` `DeepSeek` `GLM` `API`
- **收录日期：** 2026-11-05

## 这是什么

Zro 是 MoonMath.ai 的私有推理平台，面向编程 Agent 提供 DeepSeek 与 GLM 系列开源模型的 API。官网称请求“零留存”、不用客户数据训练，并提供兼容 OpenAI 与 Anthropic 的接口。

## 主要功能 / 要点

- 模型：DeepSeek V4.1 Flash、GLM-5.3、GLM-5.3 Flash，另有标为“Uncensored（无审查）”的 Dolly、Abyss 安全变体
- Free 档：GLM-5.3 Flash 与 DeepSeek V4.1 Flash 每日免费用量，每天重置
- 付费：Pro $20/月（含 $40 用量）、Max $60/月，也可买 90 天有效的用量包
- 可通过 npm 包 @moonmath-ai/zro 一键接入 Claude Code、Codex CLI 等工具，Cursor、Cline 可手动配置

## 适合谁

想用 DeepSeek/GLM 跑 Claude Code、Codex 等编程 Agent，又想先免费试用的开发者。

## 怎么用

在官网注册（Start free）并创建 API Key；在支持 OpenAI 兼容接口的客户端里把 Base URL 设为官网文档给出的地址、填入 Key 和模型名即可。也可按文档用其 CLI 登录后启动对应工具。

## 注意事项

- 需要注册账号；免费额度的具体数量以控制台为准，免费政策随时可能调整或取消
- “零留存”为官方自述，无法独立核验，敏感代码请自行权衡
- 平台提供“无审查”模型，使用须遵守法律与服务条款
- 第三方服务的 API Key 要妥善保管，不要写进公开仓库

---

[← 返回导航首页](../../README.md)

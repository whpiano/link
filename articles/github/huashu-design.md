# huashu-design

- **原链接：** <https://github.com/alchaincyf/huashu-design>
- **分类：** GitHub 开源项目
- **标签：** `设计` `Agent Skill` `PPT` `原型`
- **收录日期：** 2026-11-05

## 这是什么

huashu-design（Huashu Design）是 AI 博主“花叔”（花生，alchaincyf）开源的一个设计类 Agent Skill：在 Claude Code、Codex、Cursor、DeepSeek Harness 等支持 skills 的 agent 里打一句话，就能拿回 HTML 原生的网页、可点击 App 原型、可编辑 PPTX、动画视频、信息图等交付物。仓库约 2.8 万 star，自 2026-05-14 起改为 MIT 协议，个人和商用都免费。

## 主要功能 / 要点

- 交互原型：单文件 HTML、iPhone 机身外框、可点击、Playwright 验证
- 演讲幻灯片：HTML deck + 可编辑 PPTX（真文本框）
- 时间轴动画：导出 MP4 / GIF，可配 BGM
- 信息图、小红书 3:4 图文（3.1 新增 8 种范式）
- 设计方向顾问：六个候选缩略图挑三版；92 种带样张的风格库；5 维度设计评审
- 品牌资产协议、外观账本、设计体检（design_lint）等机制，核心链路本地运行

## 适合谁

会用 Claude Code / Codex / Cursor / DSH 等 AI 编程 agent，又需要快速出 PPT、原型、宣传动画、信息图的产品经理、独立开发者、自媒体作者。

## 怎么用

1. 按 README 用 skills CLI 安装到你的 agent（README 提示旧版 CLI 可能只同步单文件，装完需检查子目录是否完整）
2. DSH 用户也可以在「插件 → 添加插件」里填 GitHub 仓库地址安装
3. 在 agent 里直接用自然语言下需求，例如“做一份某主题演讲 PPT，推荐 3 个风格方向让我选”

## 注意事项

- 开源免费（MIT），但运行时消耗你自己 agent / 模型的额度；部分云能力（TTS 配音、AI 评审）需要你自己的厂商 Key，默认关闭
- README 自述核心链路本地运行、无遥测，记录只存本机 ~/.huashu-design/；安装任何第三方 skill 前仍建议自己看一下脚本内容
- 导出 PDF/视频需本机有 Chrome/Edge、Node、ffmpeg 等依赖
- 作者坦言这是“80 分的 skill”：不支持导入 Figma 图层编辑、复杂 3D/物理动画做不了

---

[← 返回导航首页](../../README.md)

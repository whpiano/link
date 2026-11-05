# CFNext

- **原链接：** https://github.com/PAICNI/CFNext
- **分类：** GitHub 开源项目
- **标签：** `节点` `Cloudflare` `Workers` `代理`
- **收录日期：** 2026-11-05

## 这是什么

CFNext 是 GitHub 用户 PAICNI 发布的开源项目（约 2.8k Star），定位为“部署在 Cloudflare Workers / Pages 的多功能代理订阅管理面板”。它用单个脚本在 Cloudflare 上同时实现 VLESS / Trojan / XHTTP 等多协议代理和图形化配置面板，并对外输出 Clash、sing-box、Karing、v2rayN 等格式的订阅。

## 主要功能 / 要点

- 图形化面板：通过自定义路径进入，支持深浅色主题
- 三种运行模式：Worker、MASQUE、家宽（基于 VPN Gate 的 OpenVPN 节点）
- 内置节点优选、节点数量控制、轮询下发，按地区 / 运营商 / IP 版本筛选
- 支持 ECH、落地代理（ProxyIP）、出站代理、前置节点
- 提供前后端分离部署形态，可管理多个后端
- 有 Cloudflare 额度监控、Telegram 用量通知、配置导入导出等

## 适合谁

熟悉 Cloudflare Workers、了解代理协议与订阅客户端的技术用户。

## 怎么用

1. 在 Cloudflare 后台创建 Worker 或 Pages 项目
2. 按 README 选择对应代码形态上传，并绑定名为 K 的 KV 命名空间
3. 设置面板入口路径等必填环境变量后部署
4. 访问面板设置管理密码，再把订阅地址导入客户端

## 注意事项

- 这类项目用于搭建网络代理，可能违反 Cloudflare 服务条款，存在账号被封禁的风险；也请遵守所在地法律法规
- 作者推荐部署的是“小说混淆版”等混淆代码，普通用户难以审计其中逻辑；明文版作者注明仅供阅读、不建议直接部署
- README 顶部含“机场”推广链接（带 register?code= 邀请码），这是带邀请码的推广链接，与项目本身无关，请自行甄别
- 代理节点会经手你的全部流量，请勿用于登录敏感账户，也不要把订阅地址和面板密码泄露给他人
- Cloudflare 免费额度有限，用量超限可能导致服务中断

---

[← 返回导航首页](../../README.md)

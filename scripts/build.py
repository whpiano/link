#!/usr/bin/env python3
"""根据 links.json 重新生成 README.md（导航首页）。用法：python3 scripts/build.py"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "links.json").read_text(encoding="utf-8"))
links = data["links"]
out = [f"# {data['title']}", "", f"> {data['description']}", ""]
out.append(f"共收录 **{len(links)}** 个链接。点「说明」看我写的中文文章，点「原链接」直达网站。")
out.append("")
cats = [c for c in data["categories"] if any(l["category"] == c["id"] for l in links)]
if cats:
    out.append("**分类：** " + " · ".join(f"[{c['icon']} {c['name']}](#{c['id']})" for c in cats))
    out.append("")
else:
    out += ["_还没有收录链接，敬请期待。_", ""]
for c in cats:
    items = sorted([l for l in links if l["category"] == c["id"]], key=lambda l: l["added"], reverse=True)
    out += [f'<a id="{c["id"]}"></a>', "", f"## {c['icon']} {c['name']}", "",
            "| 名称 | 简介 | 链接 |", "| --- | --- | --- |"]
    for l in items:
        tags = " ".join(f"`{t}`" for t in l.get("tags", []))
        warn = " ⚠️" if l.get("risk") else ""
        out.append(f"| **[{l['name']}]({l['article']})**{warn} | {l['summary']} {tags} | [说明]({l['article']}) · [原链接]({l['url']}) |")
    out.append("")
out += ["---", "", "⚠️ 表示文章里标注了风险（如需钱包签名、疑似钓鱼、需付费等），请先读说明。", "",
        "文章模板见 [articles/TEMPLATE.md](articles/TEMPLATE.md)；数据源是 [links.json](links.json)，运行 `python3 scripts/build.py` 可重新生成本页。", ""]
(root / "README.md").write_text("\n".join(out), encoding="utf-8")
print("README.md regenerated:", len(links), "links")

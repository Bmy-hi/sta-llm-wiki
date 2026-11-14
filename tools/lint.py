#!/usr/bin/env python3
"""STA LLM Wiki 健檢（規則見 CLAUDE.md）。

用法：python3 tools/lint.py
檢查項目：
  1. 每個 concepts 頁有「> 來源：」行，且引用的 S 編號都存在於 raw/
  2. 每個 concepts 頁的「## 重點」條列都以 [S#] 結尾
  3. concepts 頁之間與 index.md 的相對連結都找得到檔案
  4. wiki/index.md 列出了所有 concepts 頁
  5. 簡報每張 slide 都有 data-wiki，且指到存在的 concepts 頁
  6. 簡報中 data-calc 的算式重算後與顯示的數字一致
  7. wiki/log.md 每筆標題符合「## [YYYY-MM-DD] 類型 | 說明」
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CONCEPTS = WIKI / "concepts"
RAW = ROOT / "raw"
SLIDES = ROOT / "slides" / "index.html"
LOG_TYPES = {"discuss", "ingest", "compile", "lint", "query", "slides", "fix"}

errors = []


def err(where, msg):
    errors.append(f"[{where}] {msg}")


raw_ids = {p.name.split("-")[0] for p in RAW.glob("S*.md")}
pages = sorted(CONCEPTS.glob("*.md"))

for page in pages:
    text = page.read_text(encoding="utf-8")
    name = f"concepts/{page.name}"

    # 1. 來源行
    m = re.search(r"^> 來源：(.+?)(?:｜|$)", text, re.M)
    if not m:
        err(name, "缺少「> 來源：」行")
    else:
        for sid in re.findall(r"S\d+", m.group(1)):
            if sid not in raw_ids:
                err(name, f"來源 {sid} 不存在於 raw/")

    # 2. 重點條列都要有引用
    sec = re.search(r"^## 重點\n(.*?)(?=^## )", text, re.M | re.S)
    if not sec:
        err(name, "缺少「## 重點」段落")
    else:
        for line in sec.group(1).splitlines():
            if line.startswith("- "):
                cite = re.search(r"\[(S\d+)\]\s*$", line)
                if not cite:
                    err(name, f"重點條列缺少 [S#] 引用：{line[:40]}…")
                elif cite.group(1) not in raw_ids:
                    err(name, f"引用 {cite.group(1)} 不存在")

    # 3. 相對連結
    for target in re.findall(r"\]\(([^)#]+\.md)\)", text):
        if not (page.parent / target).resolve().exists():
            err(name, f"連結失效：{target}")

# 3+4. index.md
index = (WIKI / "index.md").read_text(encoding="utf-8")
for target in re.findall(r"\]\(([^)#]+\.md)\)", index):
    if not (WIKI / target).resolve().exists():
        err("index.md", f"連結失效：{target}")
for page in pages:
    if f"concepts/{page.name}" not in index:
        err("index.md", f"沒有列出 concepts/{page.name}")

# 5+6. 簡報
if not SLIDES.exists():
    err("slides", "slides/index.html 不存在")
else:
    html = SLIDES.read_text(encoding="utf-8")
    slides = re.findall(r'<section class="slide"([^>]*)>', html)
    if not slides:
        err("slides", "找不到任何 section.slide")
    for i, attrs in enumerate(slides, 1):
        m = re.search(r'data-wiki="([^"]*)"', attrs)
        if not m or not m.group(1).strip():
            err("slides", f"第 {i} 張缺少 data-wiki")
            continue
        for f in m.group(1).split(","):
            f = f.strip()
            if not (CONCEPTS / f).exists():
                err("slides", f"第 {i} 張的 data-wiki 指到不存在的頁面：{f}")
    for expr, shown in re.findall(r'<span data-calc="([^"]+)">([^<]+)</span>', html):
        if not re.fullmatch(r"[\d.+\-*/() ]+", expr):
            err("slides", f"算式含不允許的字元：{expr}")
            continue
        value = eval(expr)  # 只含數字與運算子，已在上一行檢查
        try:
            shown_v = float(shown.replace("−", "-").replace("+", "").split()[0])
        except ValueError:
            err("slides", f"顯示值不是數字：{shown}")
            continue
        if abs(value - shown_v) > 0.006:
            err("slides", f"算式 {expr} = {value:.4g}，但簡報寫 {shown}")
    print(f"  slides: {len(slides)} 張，{len(re.findall('data-calc', html))} 個算式")

# 7. log 格式
log = (WIKI / "log.md").read_text(encoding="utf-8")
for line in log.splitlines():
    if line.startswith("## "):
        m = re.fullmatch(r"## \[(\d{4}-\d{2}-\d{2})\] (\w+) \| .+", line)
        if not m:
            err("log.md", f"標題格式錯誤：{line}")
        elif m.group(2) not in LOG_TYPES:
            err("log.md", f"未知的類型：{m.group(2)}")

print(f"  concepts: {len(pages)} 頁，raw: {len(raw_ids)} 篇")
if errors:
    print(f"\nFAILED：{len(errors)} 個問題")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("\nALL CHECKS PASSED")

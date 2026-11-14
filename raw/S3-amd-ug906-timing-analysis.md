# S3 — AMD UG906: Vivado Design Analysis and Closure Techniques

- 來源：AMD, Vivado Design Suite User Guide UG906（多個版本的線上文件頁）
- 網址：
  - https://docs.amd.com/r/2021.1-English/ug906-vivado-design-analysis/Setup/Recovery-Relationship
  - https://docs.amd.com/r/2025.2-English/ug906-vivado-design-analysis/Timing-Path-Summary
  - https://docs.amd.com/r/2022.2-English/ug906-vivado-design-analysis/Table-Columns
  - https://docs.amd.com/r/2023.2-English/ug906-vivado-design-analysis/Setup-Area-Max-Delay-Analysis
- 擷取日期：2026-11-14
- 擷取狀態：部分。Timing-Path-Summary 頁直接抓取只拿到導覽選單，正文是從搜尋結果摘要取得；已改用 Setup/Recovery-Relationship 頁補齊公式。
- 類型：工具型（官方文件）

## 重點筆記（自己的話）

- Setup 的 data required time = capture 時脈緣時間 + 目的端時脈路徑延遲 − clock uncertainty − setup time。
- Setup 的 data arrival time = launch 時脈緣時間 + 來源端時脈路徑延遲 + datapath delay。
- Setup slack = required − arrival；Hold slack = arrival − required。正的代表滿足路徑要求。
- 同一個時脈（無相位差）時，路徑要求（path requirement）對 setup 是一個週期，對 hold 是 0 ns。
- setup 分析用最大延遲值，hold 分析用最小延遲值。
- recovery / removal 是對非同步腳位（preset / clear）的檢查，算法分別同 setup / hold。
- Timing summary 的指標：
  - WNS：所有 setup 路徑中最差的 slack，可正可負。
  - TNS：每個終點最差的違規值加總；全部通過時為 0。
  - WHS / THS：同樣的概念用在 hold。
- 找問題路徑可用 report_design_analysis 看 logic levels、logic delay 比例、clock skew 等特徵。

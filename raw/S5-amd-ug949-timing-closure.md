# S5 — AMD UG949: UltraFast Design Methodology（時序收斂）

- 來源：AMD, UltraFast Design Methodology Guide UG949
- 網址：
  - https://docs.amd.com/r/2023.1-English/ug949-vivado-design-methodology/Reviewing-Timing-Slack
  - https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Fixing-Large-Hold-Violations-Prior-to-Routing
  - https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Consider-Pipelining-Up-Front
  - https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Improving-Logic-Levels
- 擷取日期：2026-11-14
- 擷取狀態：完整（搜尋結果內含相關段落）
- 類型：工具型（官方文件）

## 重點筆記（自己的話）

- 簡化的 slack 式子：
  - setup slack = 路徑要求 − datapath delay(max) + clock skew − clock uncertainty − setup time
  - hold slack = 路徑要求 + datapath delay(min) − clock skew − clock uncertainty − hold time
- 分析違規時要看哪一項貢獻最大。約束正確的前提下，setup 違規最常見的主因是 datapath delay，hold 違規最常見的主因是 clock skew。
- logic levels 太多的路徑在佈局前就會不過或勉強過；即使假設 net delay 為 0 仍不過的路徑，不可能靠後端工具收斂。
- 修 setup：早一點規劃 pipelining（太晚加會讓 latency 差異擴散到整個電路）；也可用 retiming 把暫存器從 logic level 少的路徑移到多的路徑，平衡每段的邏輯。
- 修 hold：小的 hold 違規通常由 router 繞線自動修；大的（約 > 0.4 ns）可在佈線前用 phys_opt_design 的 hold fix 插入 LUT1 延遲，前提是該路徑 setup slack 夠。

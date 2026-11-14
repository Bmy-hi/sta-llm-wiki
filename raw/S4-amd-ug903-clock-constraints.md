# S4 — AMD UG903: Vivado Using Constraints（時脈約束）

- 來源：AMD, Vivado Design Suite User Guide UG903
- 網址：
  - https://docs.amd.com/r/2023.2-English/ug903-vivado-using-constraints/About-Clocks
  - https://docs.amd.com/r/2025.2-English/ug903-vivado-using-constraints/Primary-Clocks-Examples
  - https://docs.amd.com/r/2025.2-English/ug903-vivado-using-constraints/Example-One-Simple-Division-by-2
  - https://docs.amd.com/r/2025.2-English/ug903-vivado-using-constraints/Recommended-Constraints-Sequence
- 擷取日期：2026-11-14
- 擷取狀態：完整（搜尋結果內含相關段落）
- 類型：工具型（官方文件）

## 重點筆記（自己的話）

- 時脈由 period（ns）與 waveform（一個週期內上升緣、下降緣的絕對時間列表，個數必為偶數，第一個是上升緣）描述。
  - 例：10 ns、50% duty → waveform {0 5}；8 ns、75% duty、上升緣在 2 ns → waveform {2 8}。
- 主時脈用 create_clock 定義在輸入埠，例如板子上 10 ns 的 sysclk。
- 差動時脈只在正端定義主時脈，兩端都定義會產生不實際的跨時脈域路徑。
- 由暫存器除頻得到的時脈要用 create_generated_clock（例如 -divide_by 2），描述它和 master clock 的關係，而不是重新給 period。
- 虛擬時脈（virtual clock）不接在電路上，用來寫 I/O delay 約束。
- 對合成結果真正有影響的 setup 相關約束主要是 create_clock 與 create_generated_clock。
- 建議順序：主時脈 → 虛擬時脈 → generated clock → clock groups → …；XDC 檔的順序有影響。

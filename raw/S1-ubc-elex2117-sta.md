# S1 — UBC ELEX 2117 Lecture: Static Timing Analysis

- 來源：Ed Casas, ELEX 2117 Digital Techniques 2, UBC（2025 Winter）
- 網址：https://people.ece.ubc.ca/~edc/2117.jan2025/lec9.pdf
- 擷取日期：2026-11-14
- 擷取狀態：完整（PDF 文字可讀）
- 類型：教科書型

## 重點筆記（自己的話）

- D 型正反器有兩個時序要求：setup time（時脈上升緣前資料要先穩定多久）與 hold time（上升緣後資料要再維持多久）。兩者都是「要求」，由設計者負責滿足。
- hold time 通常比 setup time 短很多，常常是 0。
- 違反 setup/hold 可能造成 metastability：輸出停在不確定的中間狀態，比 tCO 更久才穩定。
- tCO：時脈緣到 Q 輸出改變的延遲；tPD：組合邏輯的傳播延遲，每多一個邏輯功能就加一些。
- 可用的 setup 時間 = 時脈週期 − tCO(max) − tPD(max)。
- slack = 可用 setup 時間 − 要求的 setup 時間；正的代表滿足。
- STA 是合成流程的一步，找出所有暫存器到暫存器路徑中最大的 tPD。
- 時序不過：改設計，或放寬要求（例如降低時脈頻率）。
- clock skew（時脈到不同正反器的時間不同）也必須納入分析。
- 講義練習題：50 MHz、tCO = 2 ns、tPD(max) = 15 ns、要求 tSU = 5 ns，問 slack 與最高頻率（講義未附答案，由 wiki 自行計算）。

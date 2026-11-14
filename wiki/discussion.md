# 先討論：範圍與決定

> 本頁是「先討論、後生成」的紀錄：寫 wiki 之前先講好要做什麼、不做什麼。

## 第 1 輪：主題（2026-11-14）

- AI 提議：FPGA 靜態時序分析（Static Timing Analysis, STA）。理由：和我修的數位系統設計（Verilog / FPGA）直接相關，也和我做過的 ICCAD clock tree 題目相關。
- 我（使用者）確認：用 STA，repo 名稱 sta-llm-wiki。

## 第 2 輪：讀者與深度

- 讀者：寫過 Verilog、但**沒看過時序報告**的大二學生。
- 要教到：看得懂 Vivado timing summary 的 WNS / TNS / WHS / THS，知道 setup 和 hold 各自怎麼修。
- 不教：OCV / AOCV、多 corner、跨時脈域細節、ASIC sign-off（太深，留到未來 ingest）。

## 第 3 輪：來源策略

- 至少 5 篇，分兩類：**教科書型**（講清楚觀念與公式）+ **工具型**（AMD 官方文件，講報告與修法）。
- 預計可能衝突的地方：不同來源的 skew 正負號約定。決定：全站用 AMD 的約定（見 CLAUDE.md 第 5 節），其他來源的寫法放在「容易搞混」。

## 第 4 輪：簡報大綱（先定大綱再生成）

1. 為什麼需要 STA → 2. setup / hold → 3. timing path → 4. slack 公式 → 5. 算一題（setup）→ 6. 算一題（hold）→ 7. skew 與 uncertainty → 8. 看懂 Vivado 報告 → 9. 約束時脈（create_clock）→ 10. 修 setup → 11. 修 hold → 12. 總結 → 13. 小測驗

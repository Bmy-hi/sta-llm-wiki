# 操作紀錄（append-only）

## [2026-11-14] discuss | 主題、讀者、範圍、簡報大綱
- 結果：主題定為 FPGA 靜態時序分析，讀者為沒看過時序報告的大二學生；記錄於 discussion.md

## [2026-11-14] ingest | 嘗試 halbleiter.org STA Setup & Hold
- 結果：失敗，公式與修法在付費牆後；捨棄，不寫 raw

## [2026-11-14] ingest | S1 UBC ELEX 2117 Static Timing Analysis
- 結果：完整；setup/hold 定義、可用 setup 時間、slack、練習題

## [2026-11-14] ingest | S2 WPI ECE 574 Timing Analysis
- 結果：完整；launch/capture path、skew、hold 條件、工具報告

## [2026-11-14] ingest | S3 AMD UG906 Design Analysis
- 結果：部分；Timing-Path-Summary 頁只抓到目錄，改用 Setup/Recovery-Relationship 等頁補齊

## [2026-11-14] ingest | S4 AMD UG903 Using Constraints
- 結果：完整；create_clock、waveform、generated clock、約束順序

## [2026-11-14] ingest | S5 AMD UG949 UltraFast Methodology
- 結果：完整；簡化 slack 式、setup/hold 主因、pipelining、LUT1 hold fix

## [2026-11-14] compile | 7 個概念頁
- 結果：sta-overview、setup-hold、slack、clock-skew-uncertainty、timing-report、clock-constraints、fixing-violations
- 發現 S2 與 S5 的 skew 正負號寫法不同 → CLAUDE.md 定符號約定，差異寫進「容易搞混」

## [2026-11-14] lint | 第 1 次
- 結果：7 頁引用通過；2 個錯誤（workflow.md、slides 尚未建立）

## [2026-11-14] slides | 教學簡報 15 張
- 結果：依 discussion.md 第 4 輪大綱，從 index.md 查詢相關頁生成

## [2026-11-14] lint | 第 2 次
- 結果：17 個算式正確；1 個錯誤（workflow.md 尚未建立）；故意改錯一個正負號，lint 成功抓到

## [2026-11-14] lint | 第 3 次
- 結果：ALL CHECKS PASSED

# Wiki 目錄：FPGA 靜態時序分析

> AI 做任何 query 前先讀這頁，再只打開相關頁面。

## 概念頁（concepts/）

| 頁面 | 一句話 | 來源 |
|---|---|---|
| [STA 概觀](concepts/sta-overview.md) | 不跑模擬，把每條路徑的延遲加起來檢查 | S1 S2 S3 |
| [Setup 與 Hold](concepts/setup-hold.md) | 上升緣前要穩、上升緣後別變 | S1 S2 |
| [Slack](concepts/slack.md) | 要求時間與到達時間的差，含 3 個計算例 | S1 S3 S5 |
| [Skew 與 Uncertainty](concepts/clock-skew-uncertainty.md) | 時脈到不同正反器的時間差 | S1 S2 S3 S5 |
| [看懂時序報告](concepts/timing-report.md) | WNS / TNS / WHS / THS | S2 S3 S5 |
| [時脈約束](concepts/clock-constraints.md) | create_clock、generated clock | S4 |
| [怎麼修違規](concepts/fixing-violations.md) | setup 減延遲、hold 加延遲 | S1 S2 S5 |

## 來源（raw/）

| 編號 | 來源 | 類型 |
|---|---|---|
| S1 | [UBC ELEX 2117 Static Timing Analysis](../raw/S1-ubc-elex2117-sta.md) | 教科書 |
| S2 | [WPI ECE 574 Timing Analysis](../raw/S2-wpi-ece574-timing.md) | 教科書 |
| S3 | [AMD UG906 Design Analysis](../raw/S3-amd-ug906-timing-analysis.md) | 官方文件 |
| S4 | [AMD UG903 Using Constraints](../raw/S4-amd-ug903-clock-constraints.md) | 官方文件 |
| S5 | [AMD UG949 UltraFast Methodology](../raw/S5-amd-ug949-timing-closure.md) | 官方文件 |

## 其他

- [先討論紀錄](discussion.md)
- [操作紀錄 log](log.md)
- [loop / graph 設計與反思](../docs/workflow.md)

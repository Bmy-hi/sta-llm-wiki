# 看懂時序報告（WNS / TNS / WHS / THS）
> 來源：S2, S3, S5 ｜ 更新：2026-11-14

## 一句話
Vivado 的 Timing Summary 用四個數字告訴你「最糟的路徑差多少」和「總共差多少」。

## 重點
- WNS（Worst Negative Slack）：所有 setup 路徑中最差的 slack，可以是正的。[S3]
- TNS（Total Negative Slack）：每個終點取最差的違規值再加總；全部通過時是 0。[S3]
- WHS / THS：同樣的意義，用在 hold（及 removal）。[S3]
- 除了最差的那條，其他關鍵路徑也要看；report_design_analysis 可列出 logic levels、logic delay 比例、clock skew。[S3]
- 路徑報告會逐級列出每個 cell 的延遲與累積 arrival time，最後算出 slack。[S2]
- 讀違規路徑時，對照簡化的 slack 式子找出貢獻最大的一項。[S5]

## 公式
    全部通過  ⇔  WNS ≥ 0 且 WHS ≥ 0（此時 TNS = THS = 0）

## 例子
假設三個終點的 setup slack 是 −0.3、−0.1、+0.5 ns：
- WNS = −0.3 ns
- TNS = (−0.3) + (−0.1) = −0.4 ns（+0.5 不算，因為只加違規的）

## 容易搞混
- WNS 的名字有 Negative，但**數值可以是正的**，正的代表最差的路徑也還有餘裕。
- TNS 只加違規值；TNS 很大但 WNS 很小，代表「很多路徑各差一點」，修法和「一條路徑差很多」不同。

## 相關頁面
- [slack](slack.md)
- [怎麼修違規](fixing-violations.md)

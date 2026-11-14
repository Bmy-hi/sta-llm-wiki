# 怎麼修時序違規（Timing Closure）
> 來源：S1, S2, S5 ｜ 更新：2026-11-14

## 一句話
先用公式找出「哪一項」吃掉最多時間，再對症下藥：setup 多半是邏輯太長，hold 多半是 skew。

## 重點
- 「收斂時序」就是反覆修改設計，直到所有路徑的 slack 都是正的；也可以放寬要求，例如降低時脈頻率。[S1]
- 約束正確的前提下，setup 違規最常見主因是 datapath delay，hold 違規最常見主因是 skew。[S5]
- 即使假設 net delay 為 0 仍不過的路徑，後端工具不可能救，必須改 RTL。[S5]
- 修 setup：提早規劃 pipelining，太晚才加會讓 latency 不一致擴散到整個電路。[S5]
- 修 setup：retiming 可把暫存器從邏輯層數少的路徑移到層數多的路徑，平衡各段。[S5]
- 修 hold：小違規通常由 router 繞線自動修；大違規（約 > 0.4 ns）可在佈線前插入 LUT1 延遲，前提是 setup slack 夠。[S5]
- 降低頻率修不了 hold，因為 hold 條件裡沒有週期。[S2]

## 公式
用 [slack](slack.md) 的簡化式逐項比較：

    setup slack = T − datapath(max) + skew − uncertainty − tSU
    hold  slack = datapath(min) − skew − uncertainty − tH

## 例子
**setup**：[slack](slack.md) 例 1 的 tPD = 15 ns 太長（slack = −2）。加一級 pipeline 把它切成 8 ns + 7 ns 兩段，最慢的一段 slack = 20 − 2 − 8 − 5 = **+5 ns**，代價是多一個週期的 latency。

**hold**：[slack](slack.md) 例 3 的 hold slack = −0.05 ns。在資料路徑插入 0.2 ns 延遲後 datapath(min) = 0.5，hold slack = 0.5 − 0.2 − 0.05 − 0.1 = **+0.15 ns**；同一條路徑的 setup 也要重算，確認還有餘裕。

## 容易搞混
- 修 hold 是「加延遲」，修 setup 是「減延遲」，兩者會互相拉扯，所以修完一個要重檢另一個。
- 降頻只是「放寬要求」，不是修好電路。

## 相關頁面
- [slack](slack.md)
- [看懂時序報告](timing-report.md)
- [skew 與 uncertainty](clock-skew-uncertainty.md)

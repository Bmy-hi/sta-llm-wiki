# S2 — WPI ECE 574 Lecture: Timing Analysis

- 來源：Patrick Schaumont, ECE 574 (Fall 2023), Worcester Polytechnic Institute
- 網址：https://schaumont.dyn.wpi.edu/ece574f23/_sources/06timing.rst.txt
- 擷取日期：2026-11-14
- 擷取狀態：完整
- 類型：教科書型（偏 ASIC）

## 重點筆記（自己的話）

- launch path：時脈到發送端（launch）正反器的路徑；capture path：時脈到接收端（capture）正反器的路徑。
- clock skew：同一個時脈緣到達 launch 與 capture 正反器的時間差。
- 本來源把 skew 當成時脈不確定量（uncertainty），永遠當作「扣掉」可用時間。
- setup 條件：週期 T 必須大於 clk-to-Q + 資料路徑延遲 + setup + skew；所以最小週期由最慢的資料路徑決定。
- hold 條件：skew + hold < clk-to-Q + 資料路徑延遲（要用最快的路徑）；違反時 capture 端會在「同一個」緣就吃到新資料，看起來像跳過一個週期。
- hold 條件與週期無關；降低頻率修不好 hold。（由上式沒有 T 可推得）
- 理想 skew 是 0；用 H-tree 等 clock tree 讓 skew 接近 0。
- STA 工具報告：late 報告（setup）slack = required − arrival；early 報告（hold）slack = arrival − required。路徑報告會逐級列出每個 cell 的延遲與累積 arrival time。
- 路徑分四種：input→output、input→register、register→register、register→output。

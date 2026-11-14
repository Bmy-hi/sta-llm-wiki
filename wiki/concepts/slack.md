# Slack（時序餘裕）
> 來源：S1, S3, S5 ｜ 更新：2026-11-14

## 一句話
slack = 「要求的時間」和「實際到達時間」的差；正的代表有餘裕、過，負的代表違規。

## 重點
- 教科書版：slack = 可用 setup 時間 − 要求 setup 時間，可用 setup 時間 = T − tCO(max) − tPD(max)。[S1]
- 工具版（setup）：slack = data required time − data arrival time。[S3]
- 工具版（hold）：slack = data arrival time − data required time。[S3]
- 同時脈時，路徑要求對 setup 是一個週期，對 hold 是 0。[S3]
- 簡化式可以直接看出哪一項拖累 slack（見下方公式）。[S5]

## 公式
全站符號約定：skew = 目的端時脈延遲 − 來源端時脈延遲。

    Setup:
      arrival  = launch 緣 + 來源端時脈延遲 + datapath(max)
      required = capture 緣 + 目的端時脈延遲 − uncertainty − tSU
      slack    = required − arrival
               = T − datapath(max) + skew − uncertainty − tSU

    Hold:
      arrival  = launch 緣 + 來源端時脈延遲 + datapath(min)
      required = 同一個緣 + 目的端時脈延遲 + uncertainty + tH
      slack    = arrival − required
               = datapath(min) − skew − uncertainty − tH

（datapath 已包含 clock-to-Q。）

## 例子
**例 1（教科書版，數字來自 S1 練習題）**：50 MHz（T = 20 ns）、tCO = 2、tPD(max) = 15、tSU = 5
- 可用 setup = 20 − 2 − 15 = 3 ns
- slack = 3 − 5 = **−2 ns** → 不過
- 最小週期 = 2 + 15 + 5 = 22 ns → fmax ≈ 45.45 MHz

**例 2（工具版 setup）**：T = 10、來源端時脈延遲 2.0、datapath(max) 7.2、目的端時脈延遲 1.8、uncertainty 0.1、tSU 0.05
- arrival = 0 + 2.0 + 7.2 = 9.2
- required = 10 + 1.8 − 0.1 − 0.05 = 11.65
- slack = 11.65 − 9.2 = **+2.45 ns**；用簡化式：10 − 7.2 + (−0.2) − 0.1 − 0.05 = 2.45 ✔

**例 3（工具版 hold）**：來源端時脈延遲 1.9、datapath(min) 0.3、目的端時脈延遲 2.1、uncertainty 0.05、tH 0.1
- arrival = 1.9 + 0.3 = 2.2；required = 2.1 + 0.05 + 0.1 = 2.25
- slack = 2.2 − 2.25 = **−0.05 ns** → hold 不過（主因是 skew = +0.2）

## 容易搞混
- **符號約定不同**：S5 的 setup 式是「+ skew」（skew 可正可負），S2 則把 skew 當成永遠扣掉的不確定量。本 wiki 用 S5 / AMD 的約定。
- setup 和 hold 的 slack 式子「減的方向」相反，但意義一樣：正的就是過。

## 相關頁面
- [setup 與 hold](setup-hold.md)
- [skew 與 uncertainty](clock-skew-uncertainty.md)
- [看懂時序報告](timing-report.md)

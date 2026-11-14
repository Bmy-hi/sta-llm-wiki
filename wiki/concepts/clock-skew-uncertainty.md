# 時脈偏斜與不確定量（Clock Skew / Uncertainty）
> 來源：S1, S2, S3, S5 ｜ 更新：2026-11-14

## 一句話
同一個時脈緣到達不同正反器的時間不一樣（skew），再加上 jitter 等不確定因素（uncertainty），都會吃掉或改變可用時間。

## 重點
- 時脈經過不同的繞線延遲，到達各正反器的時間不同，這就是 clock skew，必須納入分析。[S1]
- skew 是同一個時脈緣到 launch 與 capture 正反器的時間差。[S2]
- setup 分析中，uncertainty 從 required time 扣掉。[S3]
- 約束正確時，hold 違規最常見的主因就是 skew。[S5]
- 理想 skew 是 0，實務上用 H-tree 等 clock tree 讓 skew 接近 0。[S2]
- 一條路徑的正 skew，對反方向路徑就是負 skew，回授路徑特別要注意。[S2]

## 公式
    skew = 目的端時脈延遲 − 來源端時脈延遲
    setup slack 中：+ skew（正 skew 幫 setup）
    hold  slack 中：− skew（正 skew 害 hold）

## 例子
來源端時脈延遲 1.9 ns、目的端 2.1 ns → skew = +0.2 ns。
- 對 setup：多了 0.2 ns 可用時間。
- 對 hold：要求資料多維持 0.2 ns，若 datapath(min) 只有 0.3 ns 就可能不過（見 [slack](slack.md) 例 3）。

## 容易搞混
- **正 skew 對 setup 是好事、對 hold 是壞事**；同一個 skew 會在兩種檢查上方向相反。
- S2 把 skew 當成不確定量，永遠往壞處算；AMD 工具則分開列 skew（有正負）和 uncertainty（永遠扣）。

## 相關頁面
- [slack](slack.md)
- [setup 與 hold](setup-hold.md)
- [怎麼修違規](fixing-violations.md)

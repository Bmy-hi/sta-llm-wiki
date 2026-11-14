# Setup time 與 Hold time
> 來源：S1, S2 ｜ 更新：2026-11-14

## 一句話
正反器在時脈上升緣「前」要資料先穩定（setup），在上升緣「後」要資料別太快變（hold）。

## 重點
- setup time：D 輸入在上升緣之前至少要穩定 tSU。[S1]
- hold time：D 輸入在上升緣之後至少要維持 tH；通常比 setup 短很多，常常是 0。[S1]
- 兩者都是「要求」，是設計者要滿足的；tCO（clock-to-Q）則是元件保證的「反應」。[S1]
- 違反任一個，正反器可能進入 metastability：輸出卡在中間電位很久才穩定。[S1]
- setup 看「最慢」的資料路徑，決定最小週期；hold 看「最快」的資料路徑。[S2]
- hold 違規時，capture 端在同一個緣就吃到新資料，電路看起來像跳過一個週期。[S2]

## 公式
- setup：T > tCO + tPD(max) + tSU + skew （S2 把 skew 當作永遠扣掉的不確定量）
- hold：tCO + tPD(min) > tH + skew

## 例子
時脈 100 MHz（T = 10 ns）。如果最慢的路徑 tCO + tPD = 9.98 ns、tSU = 0.05 ns，加起來 10.03 ns > 10 ns，setup 就不過。

## 容易搞混
- **hold 式子裡沒有 T**：降低時脈頻率可以救 setup，但**救不了 hold**。
- setup 用 max 延遲、hold 用 min 延遲，不要用同一個數字算兩種。

## 相關頁面
- [slack](slack.md)
- [skew 與 uncertainty](clock-skew-uncertainty.md)
- [怎麼修違規](fixing-violations.md)

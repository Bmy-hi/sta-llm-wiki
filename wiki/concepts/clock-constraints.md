# 時脈約束（create_clock / XDC）
> 來源：S4 ｜ 更新：2026-11-14

## 一句話
STA 要先知道「時脈多快、長什麼樣」才能算路徑要求，這件事由 XDC 約束檔中的 create_clock 告訴工具。

## 重點
- 時脈由 period（ns）和 waveform（一個週期內各個緣的絕對時間，第一個是上升緣）描述。[S4]
- 板子進來的主時脈用 create_clock 定義在輸入埠上。[S4]
- 差動時脈只在正端定義，否則會產生不實際的跨時脈域路徑。[S4]
- 用暫存器除頻出來的時脈要用 create_generated_clock 描述和 master clock 的關係。[S4]
- 對合成結果真正有影響的 setup 相關約束主要是 create_clock 與 create_generated_clock。[S4]
- 約束有建議順序：主時脈 → 虛擬時脈 → generated clock → clock groups。[S4]

## 公式
    frequency = 1 / period；100 MHz ↔ period 10 ns

## 例子
    # 100 MHz、50% duty 的板子時脈
    create_clock -name sys_clk -period 10 [get_ports clk]

    # 用暫存器 REGA 除 2 得到的時脈
    create_generated_clock -name clkdiv2 -source [get_ports clk] -divide_by 2 [get_pins REGA/Q]

## 容易搞混
- 沒寫 create_clock 時，工具不知道週期，這些路徑根本不會被檢查；報告看起來「全過」反而是警訊。
- generated clock 不要再給 period，而是描述它怎麼從 master clock 變出來。

## 相關頁面
- [STA 概觀](sta-overview.md)
- [slack](slack.md)

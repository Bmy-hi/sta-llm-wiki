# 靜態時序分析（Static Timing Analysis, STA）
> 來源：S1, S2, S3 ｜ 更新：2026-11-14

## 一句話
不跑模擬，直接把「每一條暫存器到暫存器的路徑」延遲加起來，檢查資料是否在時脈規定的時間窗內到達。

## 重點
- STA 是合成 / 實作流程的一步，會找出所有暫存器間路徑的最大延遲來算 slack。[S1]
- 一條 timing path 有三段：launch 時脈路徑、資料路徑、capture 時脈路徑。[S2]
- 路徑依起訖點分為 input→register、register→register、register→output、input→output 四種。[S2]
- 每條路徑都做兩種檢查：setup（用最大延遲）與 hold（用最小延遲）。[S3]
- 對非同步腳位（preset / clear）的對應檢查叫 recovery / removal。[S3]
- STA 的前提是時脈約束正確；約束錯，報告再漂亮也沒用。[S4]

## 公式
見 [slack](slack.md)。

## 例子
一個 8 位元計數器：暫存器 Q → 加法器 → 暫存器 D 就是一條 register→register 路徑，STA 會把加法器最長的進位鏈當作最大延遲。

## 容易搞混
- STA 不是時序模擬：它不看輸入向量，所以會檢查到模擬沒跑到的路徑。
- STA 不處理非同步訊號的正確性（跨時脈域要另外設計）。

## 相關頁面
- [setup 與 hold](setup-hold.md)
- [slack](slack.md)
- [時脈約束](clock-constraints.md)

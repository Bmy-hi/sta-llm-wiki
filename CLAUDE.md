# CLAUDE.md — STA LLM Wiki（FPGA 靜態時序分析）

這是本專案的「員工手冊」（schema）。AI 每次開工前**先讀完本檔**，再讀 wiki/index.md 與 wiki/log.md 最後 5 筆，知道 wiki 裡有什麼、上次做到哪裡。

架構採用 Karpathy 的 LLM Wiki 模式：**raw（不可改的來源）→ wiki（AI 維護的知識庫）→ 產出（教學簡報）**，由本檔規定規則。

## 0. 交辦三件事

| | 內容 |
|---|---|
| **要什麼成品** | (1) wiki/ 裡有來源引用的概念頁 (2) slides/index.html 教學簡報，內容**只能**來自 wiki |
| **有什麼限制** | raw/ 一律不可修改內容（只能新增）；不得寫出來源沒有的事實；不得大段複製來源原文（著作權），一律用自己的話整理 |
| **怎麼算做完** | python3 tools/lint.py 全部通過（輸出 ALL CHECKS PASSED），且 wiki/log.md 已追加紀錄 |

不清楚就先問；**先討論、後生成**：新主題或新來源都要先把範圍與重點寫進 wiki/discussion.md，經使用者確認後才寫 wiki 頁。

## 1. 目錄結構

    /
    ├── CLAUDE.md              本檔（schema）
    ├── README.md
    ├── index.html             GitHub Pages 首頁
    ├── wiki.html              Markdown 閱讀器（wiki.html?p=wiki/index.md）
    ├── raw/                   來源擷取筆記（S1…S5），不可改
    ├── wiki/
    │   ├── index.md           所有頁面的目錄 + 一句話摘要
    │   ├── log.md             append-only 操作紀錄
    │   ├── discussion.md      先討論：範圍、讀者、決定
    │   └── concepts/          概念頁（一個概念一頁）
    ├── slides/index.html      教學簡報（由 wiki 產生）
    ├── docs/workflow.md       loop / graph 設計、執行紀錄、反思
    └── tools/lint.py          自動檢查

## 2. raw/ 來源規則

- 檔名：S編號-簡稱.md，例如 S3-amd-ug906-timing-analysis.md。編號只增不減。
- 內容：來源標題、網址、擷取日期、**擷取狀態**（完整 / 部分 / 失敗）、用自己的話寫的重點筆記。
- 擷取後**馬上檢查**內容是否真的拿到（付費牆、只拿到目錄、空白頁都算失敗），失敗就換來源，不得用記憶補。

## 3. wiki 概念頁格式（wiki/concepts/kebab-case.md）

每頁固定順序：

    # 中文名稱（English）
    > 來源：S1, S3 ｜ 更新：YYYY-MM-DD
    ## 一句話
    ## 重點          每個條列結尾必須有 [S編號]
    ## 公式          （沒有就寫「無」）
    ## 例子
    ## 容易搞混
    ## 相關頁面      用相對連結，例如 [slack](slack.md)

## 4. 三個操作

**Ingest（放入新來源）**
1. 在 discussion.md 寫下「這篇來源要補什麼、和現有頁面有什麼關係」。
2. 擷取 → 立刻檢查內容 → 寫 raw/S編號-*.md。
3. 更新或新增 concepts/ 頁面；一篇來源通常會改到 2–5 頁。
4. 若和既有內容**矛盾**（例如正負號約定不同），寫進該頁「容易搞混」，不要偷偷統一。
5. 更新 index.md，追加 log.md，跑 lint。

**Query（問問題 / 做簡報）**：先讀 index.md → 只讀相關頁面 → 回答要標出用了哪些頁。好的答案可以存回 wiki 變成新頁。

**Lint（健檢）**：python3 tools/lint.py，檢查引用、連結、目錄、簡報數字。

## 5. 符號約定（全站統一）

- 時脈偏斜 skew = 目的端（capture）時脈延遲 − 來源端（launch）時脈延遲。
- Setup slack = data required time − data arrival time；Hold slack = data arrival time − data required time。
- slack ≥ 0 代表過；單位一律 ns。

## 6. 簡報規則（slides/index.html）

- 單一 HTML，無外部相依；每張是 section.slide，用方向鍵翻頁。
- 每張都要有 data-wiki 屬性，列出內容來自哪些 concepts 頁（用逗號分隔，只寫檔名）。
- 簡報裡每個計算結果用 span data-calc="算式" 包起來，lint 會重算並比對。
- 教學順序：動機 → 觀念 → 公式 → 算一題 → 看工具報告 → 怎麼修 → 總結與小測驗。

## 7. log.md 格式

每筆一個標題，可以用 grep 解析：

    ## [YYYY-MM-DD] ingest | S3 AMD UG906
    - 結果：…

類型只用 discuss / ingest / compile / lint / query / slides / fix。

## 8. 不可以做的事

- 不可修改 raw/ 既有檔案、不可刪除 log.md 紀錄。
- 不可在簡報中加入 wiki 沒有的事實；要加，先回頭 ingest。
- 不可修改本檔規則，除非使用者明確要求。

# 24 篇 SEO 内容计划 · 进度核对报告

核对日期：2026-09-01
核对人：WorkBuddy（SEO 内容团队主理人）
核对依据：research/content-strategy-2026-06-11.md（原始规划）+ git 提交历史 + sitemap.xml + blog.html

---

## 一、总体进度

| 指标 | 数值 |
|------|------|
| 计划总数 | 24 篇 |
| 已完成并上线 | 13 篇 |
| 未开始 | 9 篇 |
| 需重写（主题已被旧文占位） | 2 篇 |
| 完成率 | 54% |
| 时间进度 | Month 4 起点（2026-09-01），完全符合原定节奏 |

结论：进度正常，不落后。原计划 Month 1-3（6 月至 8 月）共 12 篇已全部交付，且额外提前完成了 Month 6 的 A21 宠物用品篇。当前正停在 Month 4 物流专题的起点。

---

## 二、已完成 13 篇明细

| # | 文章 | 文件名 | 首次提交 |
|---|------|--------|----------|
| A1 | How Much Does a China Sourcing Agent Cost in 2026 | blog-sourcing-agent-cost-guide-2026.html | 2026-06-12 |
| A2 | Sourcing Agent vs Alibaba vs DIY | blog-sourcing-agent-vs-alibaba.html | 2026-07-07 |
| A3 | How to Verify a Chinese Factory: 8-Step Audit Checklist | blog-verify-chinese-factory-audit-checklist.html | 2026-07-07 |
| A4 | Trading Company or Manufacturer? | blog-trading-company-or-manufacturer-china.html | 2026-07-10 |
| A5 | The Hidden Costs of Importing from China | blog-hidden-costs-importing-china.html | 2026-07-14 |
| A6 | China Supplier Payment Terms: T/T, L/C, OA | blog-china-supplier-payment-terms.html | 2026-07-17 |
| A7 | How to Get Factory-Direct Pricing | blog-factory-direct-pricing-china.html | 2026-07-23 |
| A8 | Sample Evaluation Guide | blog-sample-evaluation-guide-china.html | 2026-07-24 |
| A9 | GPS Tracker Wholesale China | blog-gps-tracker-wholesale-china.html | 2026-07-24 |
| A10 | How to Source Consumer Electronics from China | blog-source-consumer-electronics-china.html | 2026-07-31 |
| A11 | Custom Apparel Manufacturing in China | blog-custom-apparel-manufacturing-china.html | 2026-08-04 |
| A12 | Private Label Products from China | blog-private-label-manufacturing-china.html | 2026-08-22 |
| A21 | Pet Supplies Wholesale from China | blog-pet-supplies-wholesale-china.html | 2026-08-12 |

配套产出：drafts/ 有 12 份稿件，research/ 有 11 份 brief，reports/ 有 14 份 SEO 审计报告。

---

## 三、未完成 11 篇

| # | 文章 | 原定时间 | 状态 |
|---|------|----------|------|
| A13 | Sea Freight from China: Cost and Timeline Guide | Month 4 (9-10月) | 未开始 |
| A14 | DDP Shipping from China Explained | Month 4 | 未开始 |
| A15 | 40ft vs LCL: Which Container Size Saves Money | Month 4 | 未开始 |
| A16 | Customs Clearance Documentation | Month 4 | 未开始 |
| A17 | Section 301 Tariffs 2026 Update | Month 5 (10-11月) | 未开始，但 blog-import-china-tariff-guide-2026.html 已部分覆盖 |
| A18 | EU GPSR Compliance | Month 5 | 未开始 |
| A19 | How to Diversify Your China Supply Chain | Month 5 | 需决策，见下方问题 3 |
| A20 | Canton Fair Autumn 2026 Buyer's Guide | Month 5 | 未开始，时间窗口紧张 |
| A22 | 2026 Year-End China Sourcing Review | Month 6 (11-12月) | 未到期 |
| A23 | Source TikTok Trending Products from China | Month 6 | 需重写，见下方问题 4 |
| A24 | China OEM Manufacturing from Scratch | Month 6 | 未开始 |

---

## 四、发现的问题（按优先级）

### 问题 1：一篇孤儿文章，用户点不到（建议本周修）

blog-china-plus-one-vs-china-only-2026.html 只存在于 sitemap.xml 中，blog.html 列表页没有它的卡片。

影响：Google 能抓到，但站内没有任何入口，用户和爬虫都无法从列表页触达，内链权重为零。blog.html 目前有 34 张卡片，实际文章 35 篇，缺的正是这一篇。

修法：在 blog.html 补一张卡片即可，五分钟的事。

### 问题 2：10 个页面已上线但未提交索引（建议本周清）

indexing_queue.json 的 pending 队列积压 10 条，其中 1 条是文章（blog-how-to-choose-ppf-manufacturer-china.html），其余 9 条是产品页（童装、T恤、卫衣、睡衣、宠物项圈 3 款、智能猫砂盆、彩色PPF）。

影响：页面上线了但没向 Google 提交，等于白做，要等自然发现。

### 问题 3：A19 主题已被两篇旧文占坑（需要你决策）

策略要求写一篇「How to Diversify Your China Supply Chain Without Leaving China」，但站上已有两篇高度重叠的旧文：

- china-plus-one-why-china-still-wins-2026.html（2026-05-22）
- blog-china-plus-one-vs-china-only-2026.html（2026-06-04）

三篇同主题会造成关键词自相残杀（cannibalization）。三个选项：
- 选项 A：不写 A19，把两篇旧文合并成一篇权威版，301 重定向另一篇
- 选项 B：写 A19，但换角度（比如聚焦"不离开中国的前提下做多工厂备份"），与旧文做差异化并互相内链
- 选项 C：跳过 A19，把这个名额换成一个新主题

我的建议是 A，省时且能集中权重。

### 问题 4：A23 TikTok 旧文仍在拉错流量（优先级高于新写）

策略文档第 7 节早已指出：blog-tiktok-shop-china-sourcing.html 现在吸引的是中国卖家（想学 TikTok Shop 运营），不是你的目标客户（海外买家想从中国进货）。

这篇每天在拉非目标流量、拉低整站受众精准度。建议不要等到 Month 6，提前重写。

### 问题 5：A20 广交会秋交会时间窗口紧

秋交会通常在 10 月中旬开幕。现在是 9 月 1 日，只剩 6 周。SEO 文章从发布到有排名一般需要 4-8 周，正好卡线。建议把 A20 提前到 Month 4 末尾先发，抢在搜索量起来之前占位。

---

## 五、建议的下一步

按投入产出比排序：

1. 【5分钟】补上 blog.html 缺失的那张卡片（问题 1）
2. 【10分钟】清空 indexing_queue.json 的 10 条 pending（问题 2）
3. 【本周】启动 Month 4 物流专题，A13 海运成本打头（这是 Month 4 的 hub 文章，其余三篇都往它内链）
4. 【9月中旬】插队重写 A23 TikTok 篇（问题 4，止损性质）
5. 【9月下旬】A20 广交会秋交会篇（问题 5，抢时间窗口）
6. 【待你决策】A19 走哪个选项（问题 3）

---

## 六、备注

- git 最后一次提交是 2026-08-22（27a9d51），本地工作区干净，与 origin/main 一致，无未推送内容。
- 文件 mtime 全部为 2026-08-28，是重装系统后恢复文件导致的，不能作为创建时间依据。本报告所有日期均以 git 首次提交记录为准。
- 本次核对为只读操作，未修改任何文件。

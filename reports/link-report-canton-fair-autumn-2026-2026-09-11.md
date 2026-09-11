# Link and Content-Health Report: A20 Canton Fair Autumn 2026

- Article under review: drafts/canton-fair-autumn-2026-2026-09-11.md
- Planned publish location: /blog/blog-canton-fair-autumn-2026-guide.html
- Report date: 2026-09-11
- Author: link-strategist (Youna Global SEO content team)
- Basis: brief-canton-fair-autumn-2026-2026-09-11.md, the two existing Canton Fair articles, blog.html, sitemap.xml, and direct on-disk file verification.
- Scope note: this report only analyzes. No draft file and no site file was modified.
- Formatting note: every character in this report is pure ASCII. No em dash, en dash, glyph arrows, emoji, or curly quotes.

---

## 1. Existing link validation (all 10 markdown links)

Method: for each of the 10 markdown links in the draft, I confirmed (a) the target file exists on disk, and (b) the relative form is correct for a document that will be published from inside the /blog/ directory.

Resolution rules applied:
- Sibling blog article: bare filename, for example blog-negotiate-moq-china.html, resolving to /blog/blog-negotiate-moq-china.html.
- Root-level page: ../ prefix, for example ../services.html, resolving to /services.html.
- Other subdirectory: ../ prefix, for example ../landing/china-trade-show.html, resolving to /landing/china-trade-show.html.

| # | Draft line | Link text (anchor) | Href as written | Resolves to | File exists on disk | Relative form correct from /blog/ | Verdict |
|---|-----------|--------------------|-----------------|-------------|---------------------|-----------------------------------|---------|
| 1 | 63 | Canton Fair sourcing agent service | ../landing/sourcing-agent-canton-fair.html | /landing/sourcing-agent-canton-fair.html | Yes | Yes (../ for a subdirectory) | PASS |
| 2 | 132 | how to tell a real factory from a trading company at the Canton Fair | blog-canton-fair-guide.html | /blog/blog-canton-fair-guide.html | Yes | Yes (bare sibling) | PASS |
| 3 | 140 | China trade show support | ../landing/china-trade-show.html | /landing/china-trade-show.html | Yes | Yes (../ for a subdirectory) | PASS |
| 4 | 148 | 8-step factory verification checklist | blog-verify-chinese-factory-audit-checklist.html | /blog/blog-verify-chinese-factory-audit-checklist.html | Yes | Yes (bare sibling) | PASS |
| 5 | 152 | how to negotiate MOQ with Chinese suppliers | blog-negotiate-moq-china.html | /blog/blog-negotiate-moq-china.html | Yes | Yes (bare sibling) | PASS |
| 6 | 152 | pre-shipment inspection checklist | blog-qc-inspection-checklist.html | /blog/blog-qc-inspection-checklist.html | Yes | Yes (bare sibling) | PASS |
| 7 | 156 | complete guide to importing from China | blog-how-to-import-from-china.html | /blog/blog-how-to-import-from-china.html | Yes | Yes (bare sibling) | PASS |
| 8 | 193 | browse our China sourcing services | ../services.html | /services.html | Yes | Yes (../ for a root page) | PASS |
| 9 | 193 | what buyers found at the 139th Canton Fair | blog-canton-fair-2026-recap.html | /blog/blog-canton-fair-2026-recap.html | Yes | Yes (bare sibling) | PASS |
| 10 | 193 | get a transparent quote | ../contact.html | /contact.html | Yes | Yes (../ for a root page) | PASS |

Result: 10 of 10 links pass. No broken targets, no missing files, and no incorrect relative forms. The draft uses exactly 10 markdown links, matching the count given in the task.

Anchor quality spot check: all 10 anchors are descriptive, keyword-relevant, and free of vague wording such as "click here" or "read more". No anchor repeats the same wording for a different target, and no target is linked twice.

---

## 2. Additional internal link recommendations (4)

All four targets below were verified to exist on disk. Each recommendation places the new link in a paragraph that currently holds zero or one link, so no paragraph exceeds the two-links-per-paragraph guideline. Where an existing paragraph already carries two links, I give the exact relocation needed.

| # | Target (site root relative) | Href to use in file | Suggested anchor text | Exact placement in the draft | Why it earns a link |
|---|-----------------------------|---------------------|-----------------------|------------------------------|---------------------|
| A1 | /landing/china-factory-visit.html | ../landing/china-factory-visit.html | arrange a China factory visit | Section "Questions that separate a real factory from a trading company" (line 132), attached to the first sentence "Ask where the factory is and whether you can visit it." | Turns the guide's abstract test ("can I visit the factory?") into a concrete next step. It is the cluster landing page for factory visits and is the natural conversion path for a reader who wants the visit arranged for them. This paragraph currently holds one link (on its final sentence), so adding this one keeps the paragraph at two. |
| A2 | /blog/blog-sample-evaluation-guide-china.html | blog-sample-evaluation-guide-china.html | how to evaluate product samples before a bulk order | Section "From sample to bulk order" (line 152), attached to "Order physical samples from your top two or three suppliers and compare them side by side, not one at a time." | The section tells the reader to order and compare samples but never explains how. This article is the missing depth. Placement note: this paragraph currently carries two links (the MOQ link and the QC link). To stay within two links per paragraph, move the existing "pre-shipment inspection checklist" link down into the later shipping sentence ("Before any bulk order ships ...") and put the new sample link on the samples sentence. |
| A3 | /blog/blog-trading-company-or-manufacturer-china.html | blog-trading-company-or-manufacturer-china.html | how to choose between a factory and a trading company | Section "Common First-Timer Mistakes", attached to the bullet "Skipping booth verification and treating every polished booth as a factory." | This section currently has zero links, so the addition also improves link distribution. Different from the fair-specific method in blog-canton-fair-guide.html, this is the general 2026 decision framework for choosing a supplier type, which is the reader's next question after the fair. |
| A4 | /blog/blog-sourcing-agent-vs-alibaba.html | blog-sourcing-agent-vs-alibaba.html | how a sourcing agent compares with doing it yourself | Section "Frequently Asked Questions", in the answer to "Is the Canton Fair worth it for importers?", attached to "If you cannot attend, a local agent can walk the floor on your behalf." | The FAQ currently has zero links and already raises the agent option. This comparison article answers the reader's follow-up question (agent, Alibaba, or DIY) without being a pure sales page, so it adds informational value and improves distribution into the back third of the article. |

Optional fifth (only if the editor wants a denser late section): /blog/blog-china-supplier-payment-terms.html with anchor "how Chinese supplier payment terms work", attached to "compare the total package: unit price, MOQ, lead time, packaging, and payment terms." in the "From sample to bulk order" paragraph. I am not counting it in the four above because that paragraph is already at its two-link limit once A2 is applied; if used, apply the A2 relocation first and do not also add this link to the same paragraph.

---

## 3. External authority sources (3)

These are third-party, non-competitor sources that strengthen the guide's credibility and match the fastest-snippet facts the draft relies on. The draft currently cites no external source at all, which is the single biggest link gap versus competing guides.

| # | Source | What to cite it for | Suggested placement | Why it is worth citing |
|---|--------|---------------------|---------------------|------------------------|
| E1 | Canton Fair official site, cantonfair.org.cn | Official session dates and phases, pre-registration, buyer badge, off-site badge collection points, and the fair app. | Section "Key dates and the three phases" (line 29 area) and Section "Online pre-registration step by step" (line 91 area). | It is the organizer's own domain and the primary source for every date, phase, and registration claim in the draft. Citing it lets a reader verify facts directly and signals the page is current for the 140th session. |
| E2 | China Ministry of Commerce, mofcom.gov.cn | The official confirmation of the 140th session dates, the three-phase structure, and the roughly 1.55 million square meter scale. | Section "Why the 140th Canton Fair Is Worth Planning For" (line 25 area), next to the scale and session claims. | It is a government source that independently confirms the session facts and the milestone framing, which is exactly the session-specific detail competitors lack. Use the notice wording as a primary citation rather than a secondary blog. |
| E3 | China National Immigration Administration, nia.gov.cn (or the nearest Chinese embassy or consulate page) | Current visa-free entry policy and business visa and invitation letter requirements. | Section "Visa and invitation letter for non-visa-free countries" (line 100 area), on the sentence "Rules do change, so verify the current requirements with your nearest Chinese embassy or consulate before you book." | Visa rules are the one part of the guide that changes without notice. Linking an official immigration authority supports the draft's own advice to verify and protects the reader from acting on stale information. |

Notes: keep all three as plain outbound links with descriptive anchor text. Do not link competitor domains (for example yiwubuying.com, sourcingyuan.com, cantonfair.co, or travel blogs) even where they cover the same topics; cite the official sources above instead. Verify each deep URL opens at publish time, since government and organizer pages are renumbered between sessions.

---

## 4. Topic cluster link map

Cluster: B (Trade Shows). The Canton Fair portion of the cluster is a three-article set plus two cluster landing pages. A20 is the forward-looking "planning" node that sits between the evergreen method article and the spring retrospective.

Member roles:
- Pillar (sourcing fundamentals): /blog/blog-how-to-import-from-china.html. The top of the funnel that A20 links out to as "the right next read".
- Cluster landing page A (conversion): /landing/sourcing-agent-canton-fair.html.
- Cluster landing page B (conversion): /landing/china-trade-show.html.
- Supporting article 1 (evergreen method): /blog/blog-canton-fair-guide.html. Owns "how to evaluate suppliers on the floor" and the factory-versus-trading-company method.
- Supporting article 2 (spring retrospective): /blog/blog-canton-fair-2026-recap.html. Owns "what happened at the 139th session".
- A20 (this article, forward-looking): /blog/blog-canton-fair-autumn-2026-guide.html. Owns dates, phases, registration, the preparation countdown, and the phase-to-category map.

Desired link flow (who links to whom):
- A20 links OUT to: pillar blog-how-to-import-from-china.html; supporting article 1 blog-canton-fair-guide.html; supporting article 2 blog-canton-fair-2026-recap.html; the verification, MOQ, and QC articles; both cluster landing pages; ../services.html; ../contact.html. This is already done in the draft (10 links above) plus the four additions in section 2.
- Supporting article 1 (blog-canton-fair-guide.html) should link TO A20 with anchor "preparing for Canton Fair Autumn 2026". It currently links only to the import pillar and the MOQ article in its sidebar, so the A20 link is a net-new edge.
- Supporting article 2 (blog-canton-fair-2026-recap.html) should link TO A20 with anchor "how to prepare for the next Canton Fair in October 2026". It currently forwards readers to the next session in body text but without a link, so this closes an existing dead end.
- Cluster landing pages (both) should link TO A20 and to supporting article 1, so the conversion pages pass readers into the informational hub rather than only receiving traffic from it.

Cross-links inside the triad:
- guide <-> recap: link both ways (they already reference each other in related-article sidebars).
- guide <-> A20 and recap <-> A20: link both ways per the two edges above.
- A20 is the only node that owns the "October 2026" time orientation, so both other articles should point their "next session" or "prepare for autumn" wording at it.

Weight-flow picture:
    pillar (how-to-import)  <-- A20
        ^
        |
    landing A (sourcing-agent-canton-fair)  -->  A20  -->  landing B (china-trade-show)
        ^                                            |
        |                                            v
    guide (evergreen)  <-->  A20  <-->  recap (spring retrospective)

Missing connections to create in a later phase: guide to A20, recap to A20, and both landing pages to A20. These are the three edges that turn three isolated pages into one connected Canton Fair cluster.

---

## 5. Content health score

Overall score: 78 / 100.

| Dimension | Weight | Score (0-100) | Weighted | Notes |
|-----------|--------|---------------|----------|-------|
| Link completeness | 25% | 70 | 17.5 | Strong internal linking (10 links, all valid). The gap is external links: zero outbound authority citations, while every top competitor cites at least the official fair site. |
| Anchor text quality | 20% | 92 | 18.4 | Descriptive, varied, keyword-relevant, no vague anchors, no duplicate anchors. Excellent. |
| Cluster connectivity | 20% | 78 | 15.6 | A20 points to both existing Canton Fair articles, the pillar, and both landing pages. Backlinks from the two existing articles to A20 are not yet applied and must wait for the A20 file to exist. |
| Link distribution | 15% | 68 | 10.2 | Links cluster in the middle and back thirds; the first third carries only one link (line 63). The four additions in section 2 partly fix this, adding coverage to the FAQ and the mistakes section. |
| User value | 10% | 90 | 9.0 | Every link helps the reader take the next step (verify, negotiate, inspect, or convert). No filler links. |
| Competitor benchmark | 10% | 70 | 7.0 | Internal-link depth is at or above competitor standard. External citations and the practical "getting there and around" logistics block are below standard. |

Interpretation: the draft is link-healthy and readable, with excellent anchor discipline and sound cluster intent. To reach the mid-80s, add the three external authority citations (section 3), apply the four internal additions (section 2), and add a short logistics block (see section 6) so the first third of the article carries more of the internal linking weight.

---

## 6. Competitor gap note

Comparable trade-show and Canton Fair guides that rank today (for example heyshenzhen.com's survival guide, yiwubuying.com's autumn buyer guide, and trip.com's autumn dates guide) all front-load practical logistics that this draft skips. Where A20 already wins is the phase-to-category map and the fair-to-order handoff; neither of those is covered by the competitors. The gaps below are what competitors rank for that A20 does not yet cover:

1. Getting to the venue and getting around it. Competitors give metro detail (Line 8 to Pazhou or Xingangdong, the Line 8 and Line 11 interchange at Pazhou, the ride from Baiyun airport and from Guangzhou South railway station), taxi and ride-hailing guidance, and entrance or gate mapping by exhibition area (A, B, C, D). A20 only says to anchor a hotel search near Pazhou and to collect the badge off-site; it never explains how the reader reaches the complex or moves between halls.
2. Where to stay, in specifics. Competitors name hotel options and districts (Pazhou versus Tianhe versus Yuexiu), the two-to-three-times fair-period rate inflation, the two-month-plus booking lead time, and minimum-stay rules. A20 gives no hotel guidance beyond the venue address.
3. Money and payments on the ground. Competitors cover carrying CNY cash in small bills, linking an international card to Alipay, currency exchange points, and metro passes. A20 covers payment app setup but not cash, exchange, or transit payment.
4. On-site survival detail. Competitors cover eating outside the noon peak, food court queues, hall air-conditioning, and the cumulative number of steps walked. A20 covers the field kit but not the on-site rhythm.
5. Business-card and note etiquette specifics. Competitors push for 200-plus cards, bilingual cards, and a WeChat QR on the card. A20 says "plenty of them" without the bilingual or QR specifics.

Recommendation: add a compact "Getting to Pazhou and around the complex" subsection inside "What to Bring and How to Set Up" (or immediately after it), 120 to 180 words, naming the metro stations and the airport and railway connections. That single block closes gaps 1 and part of 3, creates a natural home for the Metro or official travel external citation (section 3, E-optional), and adds a second internal-link opportunity into the first half of the article. Gaps 2 and 4 can be closed with one or two sentences each.

---

## 7. A20 cross-link confirmation (brief section 6.4)

The brief records four mutual cross-links between A20 and the two existing Canton Fair articles. Status of each:

| Cross-link | Direction | Anchor text in brief | Present in files today | Safe to apply now? |
|-----------|-----------|----------------------|------------------------|--------------------|
| 1 | A20 to Article 1 (blog-canton-fair-guide.html) | how to tell a real factory from a trading company at the Canton Fair | Yes, present in the A20 draft at line 132; target exists. | Safe now. It is part of the A20 file and points to an existing file. |
| 2 | A20 to Article 2 (blog-canton-fair-2026-recap.html) | what buyers found at the 139th Canton Fair | Yes, present in the A20 draft at line 193; target exists. | Safe now. Same reason as link 1. |
| 3 | Article 1 to A20 | preparing for Canton Fair Autumn 2026 | No. Neither existing article links to A20 yet. | Only AFTER the A20 HTML file exists and is deployed. Until then the target /blog/blog-canton-fair-autumn-2026-guide.html returns 404. |
| 4 | Article 2 to A20 | how to prepare for the next Canton Fair in October 2026 | No. Neither existing article links to A20 yet. | Only AFTER the A20 HTML file exists and is deployed. Until then the target returns 404. |

Explicit statement: cross-links 1 and 2 are inside A20 and point to files that already exist, so they are safe to apply at any time. Cross-links 3 and 4 are backlinks FROM the two existing articles TO the not-yet-created A20 file, so they must be applied only after the A20 HTML file exists at /blog/blog-canton-fair-autumn-2026-guide.html and is live. Applying 3 or 4 before then would introduce two broken internal links. The correct sequence is: (a) generate and deploy the A20 HTML file, (b) validate that the URL resolves, then (c) add the two backlinks in the same release that publishes A20.

---

## 8. Implementation checklist

- [ ] Confirm all 10 existing links still pass (they do at the time of this report).
- [ ] Add internal links A1 to A4 from section 2, applying the paragraph relocation noted in A2.
- [ ] Add external authority citations E1 to E3 from section 3, verified live at publish time.
- [ ] Add the "Getting to Pazhou" logistics block from section 6 to close the competitor gap.
- [ ] Publish the A20 HTML file at /blog/blog-canton-fair-autumn-2026-guide.html.
- [ ] Only after A20 is live, add cross-links 3 and 4 (Article 1 and Article 2 back to A20).
- [ ] Re-check that no paragraph exceeds two links after the additions.
- [ ] Confirm every anchor is descriptive and none mentions a markup, a sourcing-fee percentage, a commission, or any "+20%" style pricing rule.
- [ ] Confirm pure ASCII across the article and all new anchors.

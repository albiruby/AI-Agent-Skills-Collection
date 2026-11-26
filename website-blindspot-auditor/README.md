# Website Blind-Spot Auditor

**Audit adaptif dan berbasis bukti untuk website dan web application — menemukan yang terlewat oleh review, checklist, dan happy-path testing.**

Skill ini tidak mengaudit semua project dengan cara yang sama. Agent membaca konteks produk dan stack terlebih dahulu, memilih domain dan adapter yang relevan, lalu melacak data, izin, uang, konten, dan kegagalan lintas layer.

## Kenapa skill ini berbeda

- **Context before checklist.** Tidak ada asumsi Next.js, WordPress, Supabase, atau teknologi tertentu.
- **Capability-led.** Domain yang tidak relevan ditandai *Not Applicable* dengan alasan, bukan dipaksakan.
- **Evidence over volume.** Temuan diverifikasi; hipotesis tetap dilabeli sebagai hipotesis.
- **Cross-layer.** Menelusuri UI → auth → business logic → database → async → cache → user.
- **Read-only by default.** Tidak mengubah kode, data, konfigurasi, atau production tanpa izin eksplisit.
- **Honest coverage.** Coverage matrix, skor, dan limitasi menjadi bagian dari hasil.

## Kapan dipakai

Gunakan untuk permintaan seperti:

- "Audit project ini dan cari blind spot yang mungkin terlewat."
- "Stress-test checkout kami; jangan ubah kode."
- "Cari apa yang belum kami tes sebelum launch."
- "Verifikasi apakah temuan audit sebelumnya benar-benar sudah diperbaiki."

**Bukan** pengganti perbaikan kode spesifik, penetration test, atau sertifikasi kepatuhan.

Jika di koleksi ini juga ada `production-readiness-audit-skills`:

- Skill ini untuk **discovery adaptif** dan pencarian blind spot.
- Pack tersebut untuk **gate pre-launch terstruktur** dengan domain tetap dan verdict.
- Keduanya bisa dipakai berurutan: temukan di sini, tutup secara formal di sana.

## Mode audit

| Mode | Gunakan saat | Output |
|---|---|---|
| **Deep Audit** (default) | Permintaan audit luas tanpa target sempit | Laporan penuh + coverage |
| **Focused Audit** | Satu fitur/route/integrasi menjadi fokus | Laporan fokus + risiko adjacent |
| **Blind-Spot Hunt** | "Apa yang terlewat?", pre-mortem, asumsi | Hipotesis berperingkat + temuan |
| **Re-audit / Verification** | Mengecek perbaikan dan regresi | Status per temuan + regresi |

Runbook tiap mode ada di `references/13-mode-runbooks.md`.

## Isi paket

```text
website-blindspot-auditor/
  SKILL.md
  references/
    01-operating-model.md
    02-reconnaissance-and-context.md
    03-adaptive-selection.md
    04-audit-domains.md              # 13 domain briefs
    05-project-profiles.md           # 13 profil + blind spot tersering
    06-blindspot-methods.md          # 14 metode penalaran
    07-cross-layer-analysis.md
    08-edge-case-library.md          # 200+ skenario
    09-evidence-and-prioritization.md
    10-safety-and-scope.md
    11-adapter-authoring.md
    12-validation.md
    13-mode-runbooks.md
    14-intake-and-scoping.md
    15-check-command-cookbook.md
    16-coverage-and-completion.md
  adapters/
    nextjs-vercel.md
    wordpress.md
    ecommerce-and-payments.md
    supabase-postgres.md
    static-spa.md
    ai-enabled-product.md
  templates/
    intake-and-scope.md
    audit-plan.md
    audit-report.md
    exec-summary.md
    remediation-plan.md
    re-audit.md
    evidence-log.md
    coverage-matrix.md
    findings.schema.json
  examples/
    worked-example-saas.md
    worked-example-ecommerce.md
  evals/
    cases/ (3 studi kasus)
    scorecard.md
```

## Cara memasang

1. Salin folder `website-blindspot-auditor` ke direktori skills yang dipakai agent kamu.
2. Pastikan agent dapat membaca `SKILL.md`, `references/`, `adapters/`, dan `templates/`.
3. Panggil sesuai mekanisme platform (skill discovery, system prompt, atau paste langsung).

Tidak ada dependency runtime. Semua panduan bersifat workflow; akses tools tetap tergantung harness.

## Cara memakai

**Deep audit**

> Audit project ini secara menyeluruh. Mulai dari konteks produk, lalu telusuri flow kritis, izin, data, dan operasi. Jangan ubah apa pun.

**Focused**

> Audit checkout flow ini: harga, diskon, stok, webhook, refund. Test mode saja. Jelaskan batas cakupan.

**Blind-spot hunt**

> Lakukan pre-mortem pada aplikasi ini. Apa asumsi yang belum diuji dan skenario yang kemungkinan besar terlewat? Bedakan hipotesis dari temuan.

**Re-audit**

> Ini laporan audit sebelumnya. Verifikasi temuan mana yang fixed, partial, atau regressed. Cek juga regresi di flow sekitar.

## Output yang dihasilkan

- Executive summary satu halaman (`templates/exec-summary.md`).
- Laporan findings dengan severity, confidence, evidence, verification steps, dan acceptance criteria.
- Coverage matrix + skor + unknown register.
- Remediation plan dengan urutan, dependency, dan regression risk.
- `findings.schema.json` untuk konsumsi tracker/otomasi.
- Re-audit report dengan status per temuan.

## Adapter stack

| Adapter | Fokus |
|---|---|
| `nextjs-vercel` | Server actions, RSC, caching/ISR, `NEXT_PUBLIC_`, preview, deploy skew |
| `wordpress` | Capability vs nonce, REST/AJAX, XSS, upload, cache, wp-cron |
| `ecommerce-and-payments` | Harga, stok, checkout, webhook, refund, entitlement |
| `supabase-postgres` | RLS, tenant isolation, storage/realtime, constraint, migration |
| `static-spa` | Routing/SEO, bundle exposure, API trust, service worker |
| `ai-enabled-product` | Prompt injection, tool authz, output handling, RAG, biaya, evals |

Adapter hanya dimuat jika didukung bukti. Tanpa adapter, skill tetap berjalan lewat jalur unknown-technology.

## Evaluasi kualitas

`evals/` berisi 3 studi kasus dengan seeded issue, distractor, dan scorecard. Gunakan untuk mengukur recall, precision, evidence discipline, safety, dan coverage honesty. Ini sampel pengujian, bukan sertifikasi.

## Prinsip keamanan

Audit default bersifat read-only. Jangan menguji sistem pihak ketiga atau production tanpa otorisasi. Jangan mengubah kode, database, konfigurasi, dependency, atau data tanpa izin eksplisit. Jangan pernah menuliskan secret atau data pribadi ke laporan.

## Kompatibilitas

Metodologi inti technology-agnostic, tetapi kemampuan aktual bergantung pada tools harness: filesystem, shell, browser automation, test runner, akses database, dan log. Jika capability tidak tersedia, agent harus menyatakan limitasi, bukan mengarang hasil.

## Versi

Lihat [`CHANGELOG.md`](CHANGELOG.md). Versi saat ini: **2.0.0**.

# Website Blind-Spot Auditor

**Universal, adaptive audit skill for websites and web applications.**

Skill ini dirancang agar bisa dipakai pada project dengan tech stack dan use case berbeda-beda. Agent akan memeriksa konteks project terlebih dahulu, lalu memilih domain audit yang sesuai. Skill tidak mengasumsikan Next.js, React, Node.js, Sanity, PostgreSQL, atau teknologi tertentu.

## Isi paket

- `SKILL.md` — entry point dan instruksi utama untuk AI Agent.
- `references/` — metodologi, domain audit, adaptive selection, blind-spot methods, safety, dan validasi.
- `templates/` — template rencana audit, laporan audit, dan coverage matrix.

## Cara memasang

1. Ekstrak folder `website-blindspot-auditor`.
2. Salin folder tersebut ke direktori skills yang digunakan AI Agent kamu.
3. Pastikan Agent dapat membaca `SKILL.md` dan file di folder `references/` serta `templates/`.
4. Aktifkan atau panggil skill sesuai mekanisme platform Agent.

Format menggunakan struktur `SKILL.md` dengan YAML frontmatter dan referensi Markdown relatif. Platform AI Agent dapat memiliki aturan lokasi folder, konfigurasi discovery, atau mekanisme aktivasi yang berbeda. Jika platform memerlukan manifest tambahan, buat wrapper platform-specific tanpa mengubah metodologi inti.

## Contoh penggunaan

- “Audit project ini dan cari blind spot yang berpotensi terlewat.”
- “Lakukan deep audit pada website ini, termasuk security, UX, backend, dan production readiness.”
- “Blind-spot hunt untuk checkout flow. Jangan ubah kode.”
- “Audit integrasi CMS dan frontend, terutama cache invalidation, preview, dan content lifecycle.”
- “Review aplikasi ini untuk edge cases dan cross-layer failure.”

Mode default adalah **Deep Audit**. Agent dapat menjalankan Focused Audit atau Blind-Spot Hunt ketika diminta.

## Prinsip keamanan

Audit default bersifat read-only. Jangan gunakan skill untuk menguji sistem pihak ketiga atau production tanpa otorisasi yang sesuai. Jangan mengubah kode, database, konfigurasi, dependency, atau data tanpa izin eksplisit.

## Catatan kompatibilitas

Metodologi inti bersifat technology-agnostic, tetapi tidak semua platform memiliki tool yang sama. Kemampuan browser automation, terminal, test runner, database access, atau log access bergantung pada lingkungan Agent. Skill tetap dapat melakukan audit statis dan melaporkan keterbatasan ketika tool tertentu tidak tersedia.

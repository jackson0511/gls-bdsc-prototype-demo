# GLS · Demo prototype bảo dưỡng / sửa chữa

Static HTML demo for customer review:

| File | Mô tả |
|------|--------|
| `index.html` | Trang chọn demo |
| `console.html` | Prototype console web |
| `mobile.html` | Prototype mobile kỹ thuật viên |

Không cần build. Cần internet để tải Tailwind CDN.

## Cách 1 — Repo riêng (khuyến nghị)

Trong thư mục này:

```bash
cd docs/gls-pwms-fleet-bdsc-plan/demo-github-pages
git init
git add .
git commit -m "docs: add BD/SC static prototype demo for GitHub Pages"
gh repo create gls-bdsc-prototype-demo --public --source=. --remote=origin --push
```

Bật Pages:

1. GitHub repo → **Settings** → **Pages**
2. **Build and deployment** → Source: **Deploy from a branch**
3. Branch: `main` · folder: `/ (root)` → Save

URL sau vài phút:

`https://<user-or-org>.github.io/gls-bdsc-prototype-demo/`

- Console: `.../console.html`
- Mobile: `.../mobile.html`

## Cách 2 — Đẩy từ repo Plugins hiện tại

Nếu giữ trong monorepo:

1. Push branch có thư mục `docs/gls-pwms-fleet-bdsc-plan/demo-github-pages`
2. Settings → Pages → Deploy from branch
3. Folder: `/docs` **không** trỏ đúng subfolder này — GitHub Pages chỉ hỗ trợ `/` hoặc `/docs` ở root repo.

Do đó với monorepo nên dùng **GitHub Actions** (file workflow mẫu bên dưới) hoặc tách repo riêng (Cách 1).

### Workflow mẫu (Actions → Pages)

Tạo file tại root repo Plugins: `.github/workflows/bdsc-demo-pages.yml`

```yaml
name: Deploy BD/SC demo
on:
  push:
    branches: [main]
    paths:
      - 'docs/gls-pwms-fleet-bdsc-plan/demo-github-pages/**'
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages-bdsc
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/gls-pwms-fleet-bdsc-plan/demo-github-pages
      - id: deployment
        uses: actions/deploy-pages@v4
```

Sau đó Settings → Pages → Source: **GitHub Actions**.

## Cập nhật demo sau khi sửa prototype gốc

Từ thư mục plan:

```bash
cp 10-prototype-bdsc-console.html demo-github-pages/console.html
cp 11-prototype-mobile-ktv.html demo-github-pages/mobile.html
# rồi chạy lại script gỡ docs-backbar / gắn banner demo nếu cần
git add demo-github-pages && git commit -m "docs: refresh BD/SC prototype demo" && git push
```

Hoặc chạy generator (nếu có) rồi push.

## Bảo mật / nội dung

- Đây là prototype UI + dữ liệu giả — không chứa secret API.
- Repo **public**: ai có link cũng xem được. Dùng **private + Pages** (GitHub Team/Enterprise) nếu cần giới hạn.

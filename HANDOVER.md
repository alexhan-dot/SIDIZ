# SIDIZ KR→AU 마이그레이션 — 작업 지시서 (Claude Code 인수인계)

작성일: 2026-08-29. 새 Claude Code 세션은 이 문서 하나로 맥락을 복원한다.
**작업 시작 전 반드시 아래 "0. 연결 확인"을 먼저 실행할 것.**

---

## 0. 연결 확인 (매 세션 시작 시)

| 대상 | 값 | 확인 방법 |
|---|---|---|
| 작업 디렉터리 | `…\PlusUp\SIDIZ\kr.sidiz theme` | 이 파일이 있는 곳 |
| Git 원격 | `https://github.com/alexhan-dot/SIDIZ.git` (Public) | `git remote -v` |
| Shopify 스토어 | `desker-9264.myshopify.com` = www.sidiz.au | Shopify MCP `get-shop-info` |
| 관리자 핸들 | `admin.shopify.com/store/fursysau/...` | 브라우저 로그인 확인 |
| **작업 대상 테마** | `SIDIZ AU - T90 draft` **#192452231490** | GraphQL `themes` 쿼리 |
| Sep-2026 테마 | #192581239106 (UNPUBLISHED, 사용자가 직접 게시) | 〃 |
| Shopify CLI | 4.7.0 | `shopify version` |

```bash
git -C "." log --oneline -5   # 최근 커밋이 a3d5ccb(T60 AIR) 이후인지
```

```bash
shopify theme list --store desker-9264.myshopify.com
```

**⚠️ 핵심 주의: #192452231490은 현재 라이브(MAIN) 테마다.**
`theme push`는 곧 라이브 반영이며 `--allow-live`가 필요하다. ACTIVE 상품에
templateSuffix가 걸려 있으면 템플릿 푸시 즉시 공개 페이지가 바뀐다.
세션 첫 푸시 전 오너 확인을 받을 것.

---

## 1. 작업 방식 (반드시 스킬 사용)

프로젝트 스킬 **`kr-product-migration`** 이 파이프라인 전체(Phase 0~8)와
함정 17건을 정의한다. 상품 하나 = 스킬 1회 실행. 임의 절차 금지.

- 스킬 파일: `.claude/skills/kr-product-migration/SKILL.md`
- 스크립트: `scripts/` (모두 KR 핸들 인자, 예: `python scripts/extract_all_sections.py t50-2`)
- 섹션 추출은 `extract_all_sections.py` 사용 (단일 추출 스크립트는 중복 섹션 유실)
- 가격: `data/pricing/price-list.csv` (KRW→AUD, $100+는 x99 / 미만은 x9 올림)
- 상품 생성은 항상 **DRAFT**, 게시는 오너만
- KR 리뷰/인플루언서 이관 금지(ACL), 한국 특허는 "Korean Patent No."로 표기
- 영/호주식 스펠링(colour, grey…), metric only, GST 포함가

---

## 2. 지금까지 완료된 것

### 상품/템플릿 (라이브 테마 #192452231490)
| 모델 | 상품 | 템플릿 | 미디어 셀프호스팅 |
|---|---|---|---|
| T90 | `t90-ergonomic-office-chair` (ACTIVE) | `product.t90.json` (22섹션) | 동영상 23개 완료(AU Files, HLS), **정지이미지 ~69건 KR CDN 잔존** |
| T60 | `t60-ergonomic-office-chair` (ACTIVE) | `product.t60.json` (21섹션) | 미착수(전부 KR CDN) |
| T60 AIR | `sidiz-t60-air-…` (ACTIVE, 기존 상품에 템플릿만 추가) | `product.t60-air.json` (25섹션) | 미착수 |
| T50 2세대 | `sidiz-t50-2nd-…` (ACTIVE, $699 기존가 유지) | `product.t50-2.json` (24섹션) | 미착수 (KR 영상 18개) |
| T50 AIR 2세대 | `sidiz-t50-air-2nd-…` (ACTIVE) | `product.t50-air-2.json` (25섹션, t50-2 파생 — `scripts/build_t50_air_2_template.py`) | 미착수 |

추가 도구: `scripts/validate_template.py <handle>` — 템플릿 설정/블록을 섹션
스키마와 대조 + 25섹션 상한 검사. **푸시 전 필수 실행** (스킬 gotcha 18).
KR T50-2 페이지의 서드파티 YouTube 임베드 섹션은 복제 불가로 생략 — 오너 확인.

- T60 AIR는 KR 27섹션을 25섹션 제한에 맞게 접은 구조(스킬 gotcha 14).
- T60 AIR 페이지의 PRE-ORDER Wave 1 박스는 기존 프리오더 프로그램 데이터 — 건드리지 말 것.
- 마지막 눈검증: DOM 검증 통과, **픽셀 눈검증은 오너 확인 대기** (스크롤 상태
  브라우저 캡처가 흰 화면으로 나오는 문제 — gotcha 17).

### 인프라/섹션
- `sidiz-*` 섹션 29+개 (KR 컴파일 CSS 375개 포팅, 51개 CSS 변수 `sidiz-root-variables.css`)
- 헤더: fixed + blur, `data-header-scheme`로 텍스트만 흑/백 전환
- 스와치: `snippets/sidiz-swatch.liquid` (inline SVG, capture로 drop→text)
- URL 미디어 설정: `sidiz-pdp-hero`/`sidiz-content-row`/`sidiz-gallery`가
  `image_url`(+`_mobile`)/`video_url`/`poster_url` 문자열을 받도록 수정됨 (gotcha 15)
- `sidiz-product-view-vertical` 신규 (KR product_view_vertical 대응)

### Sep-2026 테마 (게시는 오너 몫)
- 스프링세일 sale_mode(할인율·재고 실계산) + 프리오더 브리지 + 안내바 완료.
- 기록 사본: `data/sep-2026/`. **월요일(2026-08-31) 오너가 직접 게시.**

### 홈페이지 수정 (2026-08-29 라이브 반영)
- S-Culture 카드 사진 cover-fit(배경 이음새 제거), 저널 제목 56px/카드 20px.

### 기타
- 전 상품 인벤토리 대조 완료: AU 98개 vs KR 카탈로그 88개(`data/kr-catalogue/products.csv`).

---

## 3. 앞으로 할 것 (우선순위 순)

### A. 다음 마이그레이션 대상 — 스킬로 진행
상품은 이미 존재(ACTIVE), **템플릿만 없음** → 업데이트 경로(T60 AIR 방식):

1. ~~T50 2세대~~ / ~~T50 AIR 2세대~~ / ~~T20~~ / ~~GX(gx-work)~~ /
   ~~MUUVE~~ / ~~LINIE~~ / ~~IBLE~~ — 완료 (2026-08-29, 각각
   product.<suffix>.json + scripts/build_*_template.py)
2. 잔여 순서: gx-joy(주의: AU에 GX 상품 2개 존재 — sidiz-gx-joy-explorer가
   suffix "gx"를 씀. KR엔 gx-work 페이지 하나뿐이라 중복 여부 오너 확인 필요)
   → ringo-gen2 → trevo → atti → molti → stepo → pillo → fungus → oui →
   mane → plit → button → ega → 굿즈(bag/spray)
   ringo-gen2 → trevo → atti → molti → stepo → pillo → fungus → oui → mane →
   plit → button → ega → 굿즈(bag/spray)
   (각각 AU 핸들은 `sidiz-*`로 존재, templateSuffix 확인 후 `product.<suffix>.json` 작성)

### B. 신규 생성 대상 (KR에만 있음 — DRAFT로 생성)
- `plit-cover` (PLIT 좌판 커버 — 파츠형)
- `t60-lda` (T60 LDA 구성 — 기존 T60 상품에 옵션으로 합칠지 오너 확인)
- `atti-desk` (ATTI 책상)
- `pacbag2507q`(벌크 B2B)는 스킵 권장 — 오너 확인

### C. 미디어 셀프호스팅 일괄 작업 (별도 큰 작업)
- T90 정지이미지 ~69건 + T60/T60 AIR 전체 → AU Files 업로드 후 템플릿 repoint
- 절차: 스킬 Phase 5 (`plan_video_upload.py` → stagedUploads(서명 바이트 길이 매칭)
  → `repoint_videos_to_au.py`). 이미지도 동일 파이프라인.

### D. 오너 승인/응답 대기 중 (임의 진행 금지)
- **Re:LIFE 9건, Tottenham 3건**: 스킬 Phase 0 제외 대상 — 승인 후 진행
- **법무 문서 26건**: KR vs AU 비교표 작성 → 차이 승인 → 반영 (미착수)
- **T60 가격 붕괴**: KR 469k/439k 두 옵션이 모두 $499로 수렴(헤드레스트 무료꼴)
  — 가격 정책 응답 대기
- **assembly_guide(크리에이터 리뷰) 섹션**: 호주 크리에이터 콘텐츠 필요
- **8개 진성 480p 영상**: SIDIZ 본사에 마스터 요청 권고
- **별도 구매(add-ons)**: 상품 추가하면서 자연스럽게 연결 (오너 지시)

### E. 소소한 미결
- sticky nav 앵커 일부(fitting/comfort/faq 등) 타깃 섹션에 id 없음 (T60/T60 AIR 공통)
- 언커밋 파일: `K-Content GTM/`, `_claude_review/`, `sidiz-listing.csv` — 커밋 여부 오너 확인

---

## 4. 데이터 위치 지도

```
.claude/skills/kr-product-migration/SKILL.md   ← 파이프라인 + 함정 17건 (필독)
scripts/                                       ← 파이프라인 스크립트 (KR 핸들 인자)
theme/                                         ← 라이브 테마 소스 (push/pull 대상)
theme/templates/product.{t90,t60,t60-air}.json ← 완료된 KR 복제 템플릿
data/kr-catalogue/products.csv                 ← KR 전 상품 88개 (대조 기준)
data/kr-raw/page-<handle>.html                 ← 저장된 KR 원본 페이지
data/products/<handle>/                        ← 모델별 산출물(sections/, en-content.md, media…)
data/pricing/price-list.csv                    ← 361 variants KRW→AUD 확정가
data/sep-2026/                                 ← Sep-2026 테마 변경 기록 사본
```

## 5. 자주 쓰는 명령

```bash
cd theme && shopify theme check --fail-level error
```

```bash
cd theme && shopify theme push --store desker-9264.myshopify.com --theme 192452231490 --nodelete --allow-live --only templates/product.<handle>.json
```

```bash
cd theme && shopify theme pull --store desker-9264.myshopify.com --theme 192452231490 --only templates/index.json
```

프리뷰(에디터): `https://admin.shopify.com/store/fursysau/themes/192452231490/editor?previewPath=/products/<handle>`

검증 순서: JSON valid → theme check(기존 에러 2건 제외: sidiz-header/sidiz-video)
→ 푸시 → 라이브 URL DOM 검증(단일 H1, 스와치, 깨진 이미지 0, JSON-LD)
→ 오너 눈검증 요청.

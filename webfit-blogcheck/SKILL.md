---
name: webfit-blogcheck
description: Use when a completed or draft Webfit experience-based Naver blog article needs morphology, keyword balance, E-E-A-T, evidence, factuality, structure, or publication-readiness verification.
---

# 웹핏 경험 기반 블로그 검수

## 목적

`webfit-blog`으로 만든 원고를 독립적으로 검수한다. 형태소 수치와 EEAT 근거를 실제 자료에 대조해 `통과 / 수정 필요 / 확인 불가`로 판정한다. 검수 요청만으로 원고를 수정·저장·업로드·게시하지 않는다.

## 작업공간 준비

현재 위치 또는 상위 폴더에서 `웹핏_경험기반_통합콘텐츠_GPT_지침.md`와 `경험_자산/`이 함께 있는 프로젝트 루트를 찾는다. 통합 지침, 검수할 원고, 연결된 EXP 파일의 본문을 실제로 읽는다. EEAT 근거에 SOUL이나 검색 검증 자료가 사용됐다면 해당 원문도 읽는다. 파일명과 요약만으로 판정하지 않는다.

## 필수 입력

- 검수할 원고
- 확정한 핵심 키워드
- 연결된 EXP 파일 또는 경험 근거

하나가 없으면 해당 영역을 추정하지 말고 `확인 불가`로 둔다.

## 검수 순서

1. 제목, 핵심 키워드, 핵심 주장과 연결된 EXP를 확인한다.
2. [references/check-rules.md](references/check-rules.md)를 읽고 구조·사실·EEAT를 대조한다.
3. 형태소는 `scripts/analyze_terms.py`로 집계한다. 다른 분석기를 쓰면 도구와 집계 방식을 밝힌다.
4. 핵심 형태소, 결합어와 상위 경쟁 명사의 횟수를 실제 수치로 제시한다.
5. 항목별 상태, 근거, 문제 문장과 수정 방향을 보고한다.
6. 최종 판정과 원고 확정 전에 반드시 고칠 항목만 압축한다.

실행 예:

```powershell
python scripts/analyze_terms.py "원고.md" --keyword "작가 홈페이지 제작" --top 20
```

## 출력 계약

1. 최종 판정
2. 형태소 집계 방식과 결과표
3. EEAT·사실성 검증표
4. 구조·가독성 검증표
5. 반드시 수정할 항목
6. 확인 자료가 없어 판정하지 못한 항목

문제마다 원문 위치 또는 문장을 짧게 식별한다. 수정 요청이 함께 있지 않으면 수정본 전체를 만들지 않는다.

## 바로 실행하는 요청

- `$webfit-blogcheck 이 원고의 형태소와 EEAT를 검수해줘.`
- `$webfit-blogcheck EXP-023과 연결된 블로그 원고가 발행 가능한지 확인해줘.`



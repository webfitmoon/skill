#!/usr/bin/env python3
"""Count priority keyword terms, adjacent compounds, and other surface terms."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


TOKEN_RE = re.compile(r"[가-힣A-Za-z0-9]+")
PARTICLES = (
    "으로부터", "에게서", "에서는", "으로는", "이라고", "이라는", "까지", "부터",
    "에서", "에게", "처럼", "보다", "으로", "라고", "이라", "에는", "에도",
    "은", "는", "이", "가", "을", "를", "의", "에", "와", "과", "도", "만", "로",
)


def normalize_token(token: str) -> str:
    token = token.lower()
    for particle in PARTICLES:
        if token.endswith(particle) and len(token) - len(particle) >= 2:
            return token[: -len(particle)]
    return token


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    text = args.source.read_text(encoding="utf-8")
    lowered = text.lower()
    priority = [part.lower() for part in TOKEN_RE.findall(args.keyword)]
    priority_counts = {term: lowered.count(term) for term in priority}

    compounds = {}
    for size in range(2, len(priority) + 1):
        for start in range(len(priority) - size + 1):
            compound = " ".join(priority[start : start + size])
            compounds[compound] = lowered.count(compound)

    tokens = [normalize_token(token) for token in TOKEN_RE.findall(text)]
    other_counts = Counter(
        token for token in tokens if len(token) >= 2 and token not in priority
    )

    result = {
        "method": "surface substring count for priority terms; particle-normalized token count for other terms",
        "source": str(args.source),
        "keyword": args.keyword,
        "priority_terms": priority_counts,
        "priority_compounds": compounds,
        "top_other_terms": dict(other_counts.most_common(args.top)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()



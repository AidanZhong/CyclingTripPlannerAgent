# -*- coding: utf-8 -*-
"""
Created on 17/01/2026 21:04

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: intent_matching
"""
import math
import re
from collections import Counter

from src.configuration import similarity_threshold


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]+", text.lower())


def build_tfidf(corpus_text: list[str]):
    docs = [tokenize(text) for text in corpus_text]
    counter = Counter()
    for doc in docs:
        for w in set(doc):
            counter[w] += 1
    vocab = {w: i for i, w in enumerate(counter.keys())}
    n = len(docs)
    idf = {w: math.log((n + 1) / (counter[w] + 1)) + 1.0 for w in counter}

    def vectorize(text: str):
        tf = Counter(tokenize(text))
        vec = [0.0] * len(vocab)
        for w, c in tf.items():
            if w in vocab:
                vec[vocab[w]] = c * idf[w]
        return vec

    corpus_vecs = [vectorize(text) for text in corpus_text]
    return vectorize, corpus_vecs


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x ** 2 for x in a))
    nb = math.sqrt(sum(x ** 2 for x in b))
    if na * nb == 0: return 0.0
    return dot / (na * nb)


def classify_message(text: str, vectorize, corpus_vecs, labels, threshold=similarity_threshold) -> set[str]:
    vec = vectorize(text)
    score = [(cosine(vec, cv), lab) for cv, lab in zip(corpus_vecs, labels)]
    score.sort(reverse=True, key=lambda x: x[0])

    intents = set()
    for s, lab in score[:5]:
        if s >= threshold:
            intents.add(lab)
    return intents

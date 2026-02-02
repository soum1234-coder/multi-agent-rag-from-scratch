import math
import re

class RetrieverAgent:
    def __init__(self, documents):
        self.documents = documents

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def vectorize(self, tokens):
        vector = {}
        for token in tokens:
            vector[token] = vector.get(token, 0) + 1
        return vector

    def cosine_similarity(self, v1, v2):
        common = set(v1.keys()) & set(v2.keys())
        numerator = sum(v1[word] * v2[word] for word in common)

        sum1 = sum(v ** 2 for v in v1.values())
        sum2 = sum(v ** 2 for v in v2.values())
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        return numerator / denominator if denominator != 0 else 0

    def retrieve(self, query, top_k=2):
        query_vec = self.vectorize(self.tokenize(query))
        scored_docs = []

        for doc in self.documents:
            doc_vec = self.vectorize(self.tokenize(doc["text"]))
            score = self.cosine_similarity(query_vec, doc_vec)
            scored_docs.append((score, doc["text"]))

        scored_docs.sort(reverse=True, key=lambda x: x[0])
        return [text for score, text in scored_docs[:top_k]]

class EvalAgent:
    def evaluate(self, query, response):
        if query.lower()[:5] in response.lower():
            return True, "High relevance"
        if len(response) < 50:
            return False, "Low quality: too short"
        return True, "Acceptable quality"

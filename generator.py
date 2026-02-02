class GeneratorAgent:
    def generate(self, query, context):
        if not context:
            return "I could not find relevant information."

        answer = f"Based on the retrieved information:\n"
        for ctx in context:
            answer += f"- {ctx}\n"

        answer += f"\nAnswer to your question: '{query}'"
        return answer

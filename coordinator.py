class CoordinatorAgent:
    def __init__(self, retriever, generator, guardrails, evaluator):
        self.retriever = retriever
        self.generator = generator
        self.guardrails = guardrails
        self.evaluator = evaluator

    def handle_query(self, query):
        print("Coordinator: Received user query")

        context = self.retriever.retrieve(query)
        print("Coordinator: Retrieved context")

        response = self.generator.generate(query, context)
        print("Coordinator: Generated response")

        safe, checked_response = self.guardrails.check(response)
        if not safe:
            return checked_response

        quality, feedback = self.evaluator.evaluate(query, checked_response)
        if not quality:
            return f"Response rejected: {feedback}"

        return checked_response

from documents import DOCUMENTS
from retriever import RetrieverAgent
from generator import GeneratorAgent
from guardrails import GuardrailsAgent
from evaluator import EvalAgent
from coordinator import CoordinatorAgent

retriever = RetrieverAgent(DOCUMENTS)
generator = GeneratorAgent()
guardrails = GuardrailsAgent()
evaluator = EvalAgent()

coordinator = CoordinatorAgent(
    retriever=retriever,
    generator=generator,
    guardrails=guardrails,
    evaluator=evaluator
)

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer = coordinator.handle_query(query)
        print("\nFinal Answer:\n", answer)

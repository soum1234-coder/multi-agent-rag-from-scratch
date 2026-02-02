class GuardrailsAgent:
    def check(self, response):
        banned_words = ["kill", "hack", "attack"]

        for word in banned_words:
            if word in response.lower():
                return False, "Response blocked due to unsafe content."

        return True, response

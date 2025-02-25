
import re
import random

class ElizaBot:
    def __init__(self):
        self.responses = {
            r'I am (.*)': [
                "Why do you say that you are %1?",
                "How long have you been %1?",
                "How do you feel about being %1?"
            ],
            r'I feel (.*)': [
                "Tell me more about feeling %1.",
                "Do you often feel %1?",
                "Why do you think you feel %1?"
            ],
            r'(.*)\?': [
                "Why do you ask that?",
                "What do you think?",
                "How would you answer that?"
            ]
        }
        self.default_responses = [
            "Please tell me more.",
            "Go on.",
            "I see.",
            "Very interesting.",
            "Can you elaborate on that?"
        ]

    def respond(self, message):
        for pattern, possible_responses in self.responses.items():
            match = re.match(pattern, message, re.I)
            if match:
                response = random.choice(possible_responses)
                return response.replace('%1', match.group(1))
        return random.choice(self.default_responses)

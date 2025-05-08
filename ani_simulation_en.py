"""
Simple Simulation of Artificial Narrow Intelligence (ANI) - English

This ANI performs sentiment analysis on input text.
It categorizes input as Positive, Negative, or Neutral based on keywords.

Note: This is a simplistic and task-specific AI model.
"""

class ANI:
    def __init__(self):
        self.positive_keywords = {'good', 'happy', 'great', 'excellent', 'love', 'wonderful'}
        self.negative_keywords = {'bad', 'sad', 'terrible', 'horrible', 'hate', 'awful'}

    def analyze_sentiment(self, text):
        text_lower = text.lower()
        pos_count = sum(word in text_lower for word in self.positive_keywords)
        neg_count = sum(word in text_lower for word in self.negative_keywords)

        if pos_count > neg_count:
            return "Positive"
        elif neg_count > pos_count:
            return "Negative"
        else:
            return "Neutral"

if __name__ == "__main__":
    ani = ANI()
    samples = [
        "I love this beautiful sunny day!",
        "This is a horrible mistake.",
        "I feel okay about the results.",
        "The movie was excellent and wonderful.",
        "I hate the bad weather."
    ]

    for text in samples:
        sentiment = ani.analyze_sentiment(text)
        print(f"Text: \"{text}\" -> Sentiment: {sentiment}")

"""
محاكاة بسيطة للذكاء الاصطناعي الضيق (ANI) - العربية

يقوم هذا النموذج بتحليل المشاعر في نص عربي بسيط.
يصنف النص إلى إيجابي، سلبي، أو محايد بناءً على كلمات مفتاحية.

ملاحظة: نموذج مبسط ومحدود لمهمة واحدة فقط.
"""

class ANI:
    def __init__(self):
        self.positive_keywords = {'جيد', 'سعيد', 'عظيم', 'ممتاز', 'أحب', 'رائع'}
        self.negative_keywords = {'سيء', 'حزين', 'فظيع', 'بشع', 'أكره', 'رديء'}

    def analyze_sentiment(self, text):
        text_lower = text.lower()
        pos_count = sum(word in text_lower for word in self.positive_keywords)
        neg_count = sum(word in text_lower for word in self.negative_keywords)

        if pos_count > neg_count:
            return "إيجابي"
        elif neg_count > pos_count:
            return "سلبي"
        else:
            return "محايد"

if __name__ == "__main__":
    ani = ANI()
    samples = [
        "أنا أحب هذا اليوم المشمس الجميل!",
        "هذا خطأ فظيع.",
        "أشعر بالرضا عن النتائج.",
        "كان الفيلم ممتاز ورائع.",
        "أنا أكره الطقس السيء."
    ]

    for text in samples:
        sentiment = ani.analyze_sentiment(text)
        print(f"النص: \"{text}\" -> المشاعر: {sentiment}")

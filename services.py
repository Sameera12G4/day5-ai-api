def analyze_text(text):
    words = text.lower().replace(".", "").split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return {
        "word_count": len(words),
        "character_count": len(text),
        "sentence_count": len(text.split(".")) - 1,
        "unique_words": list(set(words)),
        "most_common_word": max(word_counts, key=word_counts.get)
    }
def calculate(number1, number2, operation):
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        return number1 / number2
    return None
def generate_response(prompt):
    return "AI enables computers to perform tasks that normally require human intelligence."
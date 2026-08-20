from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.

    Returns:
        dict: sentiment, polarity, and subjectivity
    """

    # Remove unnecessary spaces
    text = text.strip()

    # Handle empty input
    if not text:
        return {
            "sentiment": "Neutral",
            "polarity": 0.0,
            "subjectivity": 0.0
        }

    # Create TextBlob object
    blob = TextBlob(text)

    # Get sentiment scores
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Determine sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3)
    }


# Test the sentiment analyzer
if __name__ == "__main__":

    print("=" * 50)
    print("       NewsSense - Sentiment Analyzer")
    print("=" * 50)

    text = input("\nEnter a news sentence: ")

    result = analyze_sentiment(text)

    print("\n--- Analysis Result ---")
    print("Sentiment    :", result["sentiment"])
    print("Polarity     :", result["polarity"])
    print("Subjectivity :", result["subjectivity"])
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_thresholds = {
            'positive': 0.1,
            'negative': -0.1
        }

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of a text message using TextBlob.
        Returns: 'positive', 'negative', or 'neutral'
        """
        try:
            # Get sentiment polarity (-1 to 1)
            sentiment = TextBlob(text).sentiment.polarity
            
            # Categorize sentiment
            if sentiment > self.sentiment_thresholds['positive']:
                return 'positive'
            elif sentiment < self.sentiment_thresholds['negative']:
                return 'negative'
            else:
                return 'neutral'
        except:
            return 'neutral'  # Return neutral for any errors 
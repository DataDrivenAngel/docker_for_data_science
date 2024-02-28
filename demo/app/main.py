from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob


app = FastAPI()

# Define a path operation for the root ("/") endpoint



def predict_sentiment(text: str) -> (str,float):

    """Analyzes the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple: a stuple containing a string containing 'Positive', 'Neutral', or 'Negative' based on the sentiment analysis, along with the polarity score
    """

    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score (-1 to 1)
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return(sentiment, polarity)


# Define a Pydantic model to require a string input on the request.
class SentimentRequest(BaseModel):
    text: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/predict-sentiment")
async def predict(request: SentimentRequest):
    prediction = predict_sentiment(request.text)
    return {"prediction": prediction[0], "polarity": prediction[1]}
    

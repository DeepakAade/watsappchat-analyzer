import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
import emoji
import re
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from src.chat_processor import ChatProcessor
from src.sentiment_analyzer import SentimentAnalyzer

# Set page config
st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("📱 WhatsApp Chat Analyzer")
    st.markdown("Upload your WhatsApp chat export file to analyze conversations!")

    # File upload
    uploaded_file = st.file_uploader("Choose a WhatsApp chat export file", type=['txt'])
    
    if uploaded_file is not None:
        # Read and process the file
        chat_processor = ChatProcessor(uploaded_file)
        df = chat_processor.process_chat()
        
        if df is not None:
            # Display basic statistics
            st.header("📊 Basic Statistics")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Messages", len(df))
            with col2:
                st.metric("Unique Users", df['sender'].nunique())
            with col3:
                st.metric("Date Range", f"{df['date'].min().date()} to {df['date'].max().date()}")

            # Most active users
            st.header("👥 Most Active Users")
            user_counts = df['sender'].value_counts()
            fig = px.bar(
                x=user_counts.index,
                y=user_counts.values,
                title="Message Count by User"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Messages over time
            st.header("📈 Messages Over Time")
            daily_messages = df.groupby(df['date'].dt.date).size().reset_index(name='count')
            fig = px.line(
                daily_messages,
                x='date',
                y='count',
                title="Daily Message Count"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Word Cloud
            st.header("☁️ Word Cloud")
            text = ' '.join(df['message'].astype(str))
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color='white',
                max_words=100
            ).generate(text)
            
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

            # Sentiment Analysis
            st.header("😊 Sentiment Analysis")
            sentiment_analyzer = SentimentAnalyzer()
            df['sentiment'] = df['message'].apply(sentiment_analyzer.analyze_sentiment)
            
            sentiment_counts = df['sentiment'].value_counts()
            fig = px.pie(
                values=sentiment_counts.values,
                names=sentiment_counts.index,
                title="Message Sentiment Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Raw Data Preview
            st.header("📋 Raw Data Preview")
            st.dataframe(df.head(10))

if __name__ == "__main__":
    main() 
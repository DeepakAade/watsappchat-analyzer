import pandas as pd
import re
from datetime import datetime
import emoji

class ChatProcessor:
    def __init__(self, file):
        self.file = file
        self.date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4})'
        self.time_pattern = r'(\d{1,2}:\d{2}(?::\d{2})?)\s*(?:AM|PM|am|pm)?'
        self.message_pattern = r'([^:]+):\s*(.*)'

    def process_chat(self):
        try:
            # Read the file
            content = self.file.read().decode('utf-8')
            lines = content.split('\n')

            # Initialize lists to store data
            dates = []
            times = []
            senders = []
            messages = []

            # Process each line
            for line in lines:
                # Skip empty lines
                if not line.strip():
                    continue

                # Try to match the date and time pattern
                date_match = re.search(self.date_pattern, line)
                time_match = re.search(self.time_pattern, line)
                
                if date_match and time_match:
                    # Extract date and time
                    date_str = date_match.group(1)
                    time_str = time_match.group(1)
                    
                    # Convert to datetime
                    try:
                        if len(date_str.split('/')[-1]) == 2:
                            date_str = date_str[:-2] + '20' + date_str[-2:]
                        datetime_str = f"{date_str} {time_str}"
                        date_time = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')
                    except ValueError:
                        continue

                    # Extract sender and message
                    message_match = re.search(self.message_pattern, line)
                    if message_match:
                        sender = message_match.group(1).strip()
                        message = message_match.group(2).strip()

                        # Skip media messages
                        if '<Media omitted>' in message:
                            continue

                        # Clean message
                        message = self._clean_message(message)

                        # Append to lists
                        dates.append(date_time)
                        times.append(time_str)
                        senders.append(sender)
                        messages.append(message)

            # Create DataFrame
            df = pd.DataFrame({
                'date': dates,
                'time': times,
                'sender': senders,
                'message': messages
            })

            return df

        except Exception as e:
            print(f"Error processing chat: {str(e)}")
            return None

    def _clean_message(self, message):
        # Remove URLs
        message = re.sub(r'http\S+|www\S+|https\S+', '', message, flags=re.MULTILINE)
        
        # Remove special characters but keep emojis
        message = re.sub(r'[^\w\s\U0001F300-\U0001F9FF]', '', message)
        
        # Remove extra whitespace
        message = ' '.join(message.split())
        
        return message 
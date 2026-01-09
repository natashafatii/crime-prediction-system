# load_dataset.py
import pandas as pd
from sqlalchemy import create_engine

# Use raw string (prefix r) for Windows path
df = pd.read_excel(r'C:\Users\Hp\Desktop\crime_prediction_app\crime_prediction_app\crime_prediction_app\cleaned_data.xlsx')

# Connect to SQLite
engine = create_engine('sqlite:///crime_data.db')

# Save to database
df.to_sql('crime_table', con=engine, if_exists='replace', index=False)

print("✅ Dataset loaded into SQLite database!")

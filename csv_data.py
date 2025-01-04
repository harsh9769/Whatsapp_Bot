import pandas as pd
from api.webapp import app, db, Data

# Correct file path with raw string
file_path = r"stations_with_lines.csv"

def import_csv_to_db(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    with app.app_context():
        for index, row in df.iterrows():
            try:
                # Create a new Data entry using Station_Name and Line from the CSV
                csv_entry = Data(ID=row['ID'], Station_Name=row['Station Name'], Line=row['Line'])
                print(f"Adding: {csv_entry}")  # For debugging purposes
                db.session.add(csv_entry)
            except Exception as e:
                print(f"Error adding entry {index}: {e}")
        db.session.commit()

# Run the import
import_csv_to_db(file_path)

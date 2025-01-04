from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load data from CSV file
data_file = "stations_with_lines.csv"  # Ensure the file exists and is formatted correctly
stations_df = pd.read_csv(data_file)

@app.route("/")
def main():
    # Convert the DataFrame to a list of dictionaries and pass it to the template
    stations = stations_df.to_dict(orient='records')
    return render_template("index1.html", stations=stations)

@app.route("/cost", methods=["POST"])
def cost_cal():
    if request.method == "POST":
        selected_source = request.form.get('source')
        selected_destination = request.form.get('destination')

        # Find the source and destination stations
        source_station = stations_df[stations_df['Station_Name'] == selected_source]
        destination_station = stations_df[stations_df['Station_Name'] == selected_destination]

        if not source_station.empty and not destination_station.empty:
            source_id = int(source_station['ID'].values[0])
            destination_id = int(destination_station['ID'].values[0])

            # Calculate the cost (for simplicity, the difference between IDs)
            cost = abs(destination_id - source_id)

            # Pass data to the HTML template
            return render_template("cost.html", 
                                   selected_source=selected_source, 
                                   selected_destination=selected_destination, 
                                   cost=cost)
        else:
            error_msg = "Source or Destination not found."
            return render_template("error.html", error_msg=error_msg)
    else:
        return "Invalid request method.", 405

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import pandas as pd

# Create an instance of Flask object
# __name__ due to the fact, that I want run this script only when the file \
# is run, not when the function is importer to another file
app = Flask(__name__)

# Read the data to dataframe
df = pd.read_csv("dictionary.csv")


# This will create a link to home page
@app.route("/")
def home():
    return render_template("home.html")


# This will create a link to the API page
@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    result_dictionary = {"definition": definition, "word": word}
    return result_dictionary


# Run API on the specific port
if __name__ == "__main__":
    app.run(debug=True, port=5001)

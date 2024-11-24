# vehicles_analysis
Vehicles analysis

A simple and interactive web application to perform an analysis on vehicles. The app shows an histogram and a scatter plot.

Features
Checkbox histogram: Use a checkbox button to show the histogram.
Checkbox scatter plot: Use another checkbox to show the scatter plot.
Visual Representation: The charts that shows up after clicking the checkbox are a dynamic ones. You can make a zoom to visualize them and hover the mouse over them so you can see details of the info. 

How to Use
Launch the app using Streamlit.
Press the checkbox to show the charts.
View the result and observe all of the info
.
Installation
To run this app locally, follow these steps:

Clone this repository:

git clone https://github.com/Loretonavarro/vehicles_analysis
cd vehicles_analysis
Install the required dependencies:

pip install streamlit
pip install plotly_express
pip install nbformat
Run the app:

streamlit run app.py --server.runOnSave true
Open the app in your browser at the URL provided by Streamlit.

Technologies Used
Python: The core programming language.
Streamlit: For creating the interactive web interface.
Plotly express: For generating the scatter plot and histogram visualizations.
Pandas: To read the .csv file
Nbformat: To ease the automated processing.
Contributing
Contributions are welcome! If you have suggestions for features or find any issues, feel free to open a pull request or submit an issue.

License
This project is licensed under the MIT License.
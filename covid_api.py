# API data fetch 
import requests
url = "https://disease.sh/v3/covid-19/all"
data = requests.get(url).json()
data
# DataFrame create
import pandas as pd
df = pd.DataFrame({
    "Cases": [data["cases"]],
    "Recovered": [data["recovered"]],
    "Deaths": [data["deaths"]],
    "Active": [data["active"]]
})
df
# Visualization
import matplotlib.pyplot as plt
df.plot(kind="bar")
plt.title("Global COVID-19 Statistics")
plt.show()
# Country-wise 
country = "India"
url = f"https://disease.sh/v3/covid-19/countries/{country}"
data_country = requests.get(url).json()
df_country = pd.DataFrame({
    "Cases": [data_country["cases"]],
    "Recovered": [data_country["recovered"]],
    "Deaths": [data_country["deaths"]],
    "Active": [data_country["active"]]
})
df_country
df_country.plot(kind="bar")
plt.title("COVID-19 Data - India")
plt.show()

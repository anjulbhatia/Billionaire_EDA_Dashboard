import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_icon=":moneybag:", page_title="Billionaire Dashboard",)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the billionaire dataset
@st.cache_data
def load_data():
    return pd.read_csv("Billionaires.csv")

df = load_data()
df["finalWorth"] = df["finalWorth"]/1000

# Sidebar
st.sidebar.title("Dashboard Options")

# Search bar
search_query = st.sidebar.text_input("Search by Name")

# Dashboard options
selected_country = st.sidebar.multiselect("Filter by Country", df['country'].sort_values().unique())
selected_gender = st.sidebar.multiselect("Filter by Gender", df['gender'].sort_values().unique())
selected_category = st.sidebar.multiselect("Filter by Category", df['category'].sort_values().unique())
selected_industry = st.sidebar.multiselect("Filter by Industry", df['industries'].sort_values().unique())
selected_age_range = st.sidebar.slider("Filter by Age Range", min_value=18, max_value=101, value=(18, 101))

# Filter data based on search query and selected options
filtered_df = df.copy()
if search_query:
    filtered_df = filtered_df[filtered_df['personName'].str.contains(search_query, case=False)]
if selected_country:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_country)]
if selected_gender:
    filtered_df = filtered_df[filtered_df['gender'].isin(selected_gender)]
if selected_category:
    filtered_df = filtered_df[filtered_df['category'].isin(selected_category)]
if selected_industry:
    filtered_df = filtered_df[filtered_df['industries'].isin(selected_industry)]
filtered_df = filtered_df[(filtered_df['age'] >= selected_age_range[0]) & (filtered_df['age'] <= selected_age_range[1])]

# Main content

#st.title("Billionaires Data Analysis Dashboard")
components.html("""
<script src="https://cdn.tailwindcss.com"></script>
<style>
.highlight {
  background: linear-gradient(
      100deg,
      rgba(255, 221, 64, 0) 0.9%,
      rgba(255, 221, 64, 1) 2.4%,
      rgba(255, 221, 64, 0.5) 5.8%,
      rgba(255, 221, 64, 0.1) 93%,
      rgba(255, 221, 64, 0.7) 96%,
      rgba(255, 221, 64, 0) 98%
    ),
    linear-gradient(
      180deg,
      rgba(255, 221, 64, 0) 0%,
      rgba(255, 221, 64, 0.3) 7.9%,
      rgba(255, 221, 64, 0) 15%
    );
  border-radius: 0.125em;
  box-decoration-break: clone;
  padding: 0.125em 0.25em;
}
</style>
<div class="abg-indigo-900 text-center py-4 lg:px-4">
<a id="get_latest" href="https://www.bloomberg.com/billionaires/" target=_blank class="group p-2 bg-indigo-800 hover:bg-indigo-900 items-center text-indigo-100 leading-none lg:rounded-full flex lg:inline-flex hover:cursor-pointer" role="alert">
    <span class="group-hover:bg-indigo-600 flex rounded-full bg-indigo-500 uppercase px-2 py-1 text-xs font-bold mr-3">New</span>
    <span class="font-semibold mr-2 text-left flex-auto">Get real time billionaire data</span>
    <svg class=" rounded text-white group-hover:text-neutral-900 group-hover:bg-white fill-current opacity-75 h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M12.95 10.707l.707-.707L8 4.343 6.586 5.757 10.828 10l-4.242 4.243L8 15.657l4.95-4.95z"/></svg>
</a>
</div>

<div class="text-center mb-2 min-md:space-y-2">
        <h1 class="highlsight max-md:text-xl text-3xl font-bold">Billionaires Data Analysis Dashboard</h1>
        <p class="text-gray-600">Created by 
            <span class="font-medium underline selection:text-purple-900 decoration-blue-500/30">Anjul Bhatia<span>
        </p>
    </div>

    <!-- Links to LinkedIn and GitHub -->
    <div class="flex justify-center space-x-4">
        <!-- LinkedIn Link -->
        <a href="https://www.linkedin.com/in/anjulbhatia/" target=_blank class="m-0 hover:shadow-[10px_10px_0px_#000] hover:-translate-x-[8px] hover:-translate-y-[8px] transition-all duration-[600ms]">
            <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
        </a>
        <!-- GitHub Link -->
        <a href="https://github.com/anjulbhatia" target=_blank class="m-0 hover:shadow-[10px_10px_0px_#ee4] hover:-translate-x-[8px] hover:-translate-y-[8px] transition-all duration-[600ms]">
            <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
        </a>
    </div>
""", height=200)

# Main content
components.html(f"""
<script src="https://cdn.tailwindcss.com"></script>
<h2 class="text-center mb-4 text-2xl font-bold">Billionaire Analysis</h2>
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <p class="text-3xl font-bold text-center text-blue-500">{filtered_df.shape[0]}</p>
        <h3 class="text-lg font-semibold mb-2 text-center">Total Billionaires</h3>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Total Net Worth (in billion $)</h3>
        <p class="text-3xl font-bold text-center text-green-500">{df['finalWorth'].sum()}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Total Countries</h3>
        <p class="text-3xl font-bold text-center text-purple-500">{len(df['country'].unique())}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Median Age</h3>
        <p class="text-3xl font-bold text-center text-red-500">{df['age'].median()}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Male Billionaires</h3>
        <p class="text-3xl font-bold text-center text-yellow-500">{len(df[df['gender'] == 'M'])}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Female Billionaires</h3>
        <p class="text-3xl font-bold text-center text-pink-500">{len(df[df['gender'] == 'F'])}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Total Industries</h3>
        <p class="text-3xl font-bold text-center text-indigo-500">{len(df['industries'].unique())}</p>
    </div>
    <div class="bg-white rounded-lg p-4 shadow-md transition duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg">
        <h3 class="text-lg font-semibold mb-2 text-center">Self-made Ratio</h3>
        <p class="text-3xl font-bold text-center text-orange-500">{df['selfMade'].value_counts(normalize=True).loc[True]:.2f}</p>
    </div>
</div>
""", height=200)

# Create subplots with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Pie chart for Male/Female distribution
male_female_counts = df['gender'].value_counts()
axes[0, 0].pie(male_female_counts, labels=male_female_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
axes[0, 0].set_title('Male/Female Distribution')

# Pie chart for Self-made billionaires
selfmade_counts = df['selfMade'].value_counts()
axes[0, 1].pie(selfmade_counts, labels=selfmade_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
axes[0, 1].set_title('Self-made Billionaires')

# Bar graph for top 10 countries with billionaires
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, ax=axes[1, 0], palette='viridis')
axes[1, 0].set_xlabel('Number of Billionaires')
axes[1, 0].set_ylabel('Country')
axes[1, 0].set_title('Top 10 Countries with Billionaires')

# Bar graph for top industries with billionaires
top_industries = df['industries'].value_counts().head(10)
sns.barplot(x=top_industries.values, y=top_industries.index, ax=axes[1, 1], palette='viridis')
axes[1, 1].set_xlabel('Number of Billionaires')
axes[1, 1].set_ylabel('Industry')
axes[1, 1].set_title('Top 10 Industries with Billionaires')

plt.tight_layout()
plt.show()

# Bar graph for top 10 countries with billionaires
plt.figure(figsize=(12, 6))
sns.countplot(y='country', data=df, order=df['country'].value_counts().head(10).index, palette='viridis')
plt.title('Top 10 Countries with Billionaires')
plt.xlabel('Number of Billionaires')
plt.ylabel('Country')
st.pyplot()

# Bar graph for top industries with billionaires
plt.figure(figsize=(12, 6))
sns.countplot(y='industries', data=df, order=df['industries'].value_counts().head(10).index, palette='viridis')
plt.title('Top Industries with Billionaires')
plt.xlabel('Number of Billionaires')
plt.ylabel('Industry')
st.pyplot()

# Filter data based on selected country from the sidebar
country_filtered_df = df[df['country'].isin(selected_country)]

# Sort the filtered data by rank
country_filtered_df = country_filtered_df.sort_values(by='rank')

# Select the top 10 billionaires from the selected country
top_10_billionaires = country_filtered_df.head(10)[['personName', 'source', 'finalWorth']]


fig, ax = plt.subplots(figsize=(14, 6))

sns.barplot(data=top_10_billionaires, x='finalWorth', y='personName', palette="flare", ax=ax)
ax.set_xlabel('Net Worth')
ax.set_ylabel('Name')
ax.set_title('Net Worth of Top 10 Billionaires by Name')

for index, value in enumerate(top_10_billionaires['finalWorth']):
    ax.text(value, index, f'{value:,}', ha='left', va='center', color='black')
st.write(fig)  # Display the plot

    
# Create an accordion container
with st.expander("# Dataset"):
    with st.container():
        st.markdown("### Dataset Preview")
        st.write(filtered_df.set_index('rank', inplace=False))
        
    with st.container():
        st.markdown("### Top 10 Billionaires")
        st.markdown(f"**Country: {[i for i in selected_country]}**")
        
        # Display the top 10 billionaires with ranks starting from 1 if there are rows in the DataFrame
        if not top_10_billionaires.empty:
            top_10_billionaires.index = range(1, 11)
            st.write(top_10_billionaires)
        else:
            st.write("No data available for the selected country.")
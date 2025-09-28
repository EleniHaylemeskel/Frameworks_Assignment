import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Load Data with caching ---
@st.cache_data
def load_data():
    # Use low_memory=False to avoid dtype warnings
    df = pd.read_csv("data/metadata.csv", low_memory=False)
    
    # Convert publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    
    # Extract publication year
    df['year'] = df['publish_time'].dt.year
    
    # Fill missing journal names for safer plotting
    df['journal'] = df['journal'].fillna("Unknown")
    
    return df

df = load_data()

# --- App Layout ---
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers metadata interactively.")

# Year range slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

st.write(f"Showing {len(filtered)} papers from {year_range[0]} to {year_range[1]}")

# --- Publications by Year ---
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# --- Top Journals ---
st.write("### Top Journals")
top_journals = filtered['journal'].value_counts().head(5)
st.bar_chart(top_journals)

# --- Sample Data ---
st.write("### Sample Papers")
st.dataframe(filtered[['title', 'authors', 'journal', 'publish_time']].head(10))

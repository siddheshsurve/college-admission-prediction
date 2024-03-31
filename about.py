import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def app() :

    df = pd.read_csv("college_data.csv")

    # st.title("Top 5 Branch Distribution")

    # # Branch names and counts
    # branches = ['COMP', 'ENTC', 'MECH', 'IT', 'ELECTRICAL']
    # counts = [18655, 15173, 12788, 9542, 8026]

    # # Create a DataFrame for visualization
    # df = pd.DataFrame({'Branch': branches, 'Count': counts})

    # # Display the data
    # st.write("Here's the distribution of the top 5 branches with the highest counts:")
    # st.write(df)

    # # Create a bar chart
    # plt.figure(figsize=(10, 6))
    # plt.bar(df['Branch'], df['Count'], color='skyblue')
    # plt.xlabel('Branch')
    # plt.ylabel('Count')
    # plt.title('Top 5 Branch Distribution')
    # plt.xticks(rotation=45, ha='right')
    # st.pyplot()

    st.title("Top 5 Branch Distribution")

    # Branch names and counts
    branches = ['COMP', 'ENTC', 'MECH', 'IT', 'ELECTRICAL']
    counts = [18655, 15173, 12788, 9542, 8026]

    # Create a DataFrame for visualization
    df = pd.DataFrame({'Branch': branches, 'Count': counts})


    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['Branch'], df['Count'], color='skyblue')
    ax.set_xlabel('Branch')
    ax.set_ylabel('Count')
    ax.set_title('Top 5 Branch Distribution')
    ax.tick_params(axis='x', rotation=45)

    # Display the bar chart
    st.pyplot(fig)

    st.title("Top 5 Cities Distribution")

    # Data
    cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Amravati']
    counts = [19963, 8693, 7657, 4110, 2286]

    # Calculate total count
    total_count = sum(counts)

    # Calculate percentages
    percentages = [(count / total_count) * 100 for count in counts]

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(percentages, labels=cities, autopct='%1.1f%%', startangle=140)
    ax.set_title('Top 5 Cities with Max College Count')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart
    st.pyplot(fig)


    



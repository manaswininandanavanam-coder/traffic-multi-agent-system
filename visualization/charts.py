import matplotlib.pyplot as plt
import pandas as pd


# Bar chart for vehicle count
def vehicle_bar_chart(df):

    fig, ax = plt.subplots()

    ax.bar(df["Intersection"], df["Vehicles"])

    ax.set_title("Vehicle Density at Intersections")
    ax.set_xlabel("Intersection")
    ax.set_ylabel("Number of Vehicles")

    return fig


# Pie chart for traffic distribution
def traffic_pie_chart(df):

    fig, ax = plt.subplots()

    ax.pie(
        df["Vehicles"],
        labels=df["Intersection"],
        autopct="%1.1f%%"
    )

    ax.set_title("Traffic Distribution")

    return fig


# Line chart for traffic trend
def traffic_line_chart(df):

    fig, ax = plt.subplots()

    ax.plot(df["Intersection"], df["Vehicles"], marker="o")

    ax.set_title("Traffic Flow Trend")
    ax.set_xlabel("Intersection")
    ax.set_ylabel("Vehicles")

    return fig

import matplotlib.pyplot as plt
import numpy as np

# Working with Python lists, just a demonstration
# in reality we use NumPy arrays for this, since its faster and has more functionalities

x = [1, 2, 3, 4]
y = [20, 30, 20, 40]

plt.plot(x, y)

plt.show()

# Using NumPy arrays and also customizing the plot

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5, 12, 13, 17, 21, 23])

plt.plot(
    x, y,
    marker = ".",
    markersize = 20,
    markerfacecolor = "#3a5c7a",
    markeredgecolor = "#0a2e4d",
    linestyle = "solid",
    linewidth = 2,
    color = "#0d1b27"
)

# Multiple Plots, and unpacking dictionaries

customization = dict(marker = ".",
                     markersize = 20,
                     markerfacecolor = "#3a5c7a",
                     markeredgecolor = "#0a2e4d",
                     linestyle = "solid",
                     linewidth = 2,
                     color = "#0d1b27")

plt.plot(x, y, **customization) 

# Gives the same plot

# adding title, xlabel and ylabel

font_customization = dict(
    fontweight = "bold",
    color = "#7e0707",
    family = "Cambria"
)

plt.title(
    "Test Plot",
    **font_customization
)

plt.xlabel(
    "xlabel",
    **font_customization
)

plt.ylabel(
    "ylabel",
    **font_customization
)

# Multiple plots can be plotted
# with the help of multiple instances of plt.plot()

# Adding grids

plt.grid()

# Bar Charts: Comparing Categories of data
# Creating your own beautiful bar chart using customization


characters = ["Walter White", "Skylar White", "Hank Schrader", "Marie Schrader", "Walter Junior", "Jesse Pinkman", "Saul Goodman", "Mike Ehrmantraut", "Tuco Salamanca", "Gus Fring", "Skinny Pete"]
rating = np.array([95, 25, 70, 15, 45, 92, 98, 85, 90, 85, 80])

# Used a horizontal bar chart because characters were stacking on top of each other

plt.barh(characters, rating, color="#14a025")
plt.title("Breaking Bad", **font_customization, fontsize=25)
plt.ylabel("Characters", **font_customization, fontsize=18)
plt.xlabel("Ratings out of 100", **font_customization, fontsize=18)

# Pie Chart: Used to show sort of distribution of something between various categories
# Like distribution of my time playing various games during childhood:

games = ["Minecraft", "PUBG", "FreeFire", "Clash of Clans", "Clash Royale", "Brawl Stars", "Swordigo", "Others"]
times = np.array([200, 85, 15, 120, 140, 135, 70, 100])
colors = ["#308f30", "#5B525222", "#f66714", "#f5f544", "#f14444", "#c1c17f", "#2667b1", "#b55de1"]
plt.pie(times, labels=games,
               autopct="%1.1f",
               colors=colors,
               shadow=True,
               explode=[0.1, 0, 0, 0, 0, 0, 0, 0]
               )

plt.title("Games played by me vs % time")


# Scatter Graphs: Same as line graph without the lines
# Scatter plots are usually used to show dependancy between 2 variables
# Can show correlation between the values
# Like Hours studied vs Marks obtained will most probably have a positive correlation

# use plt.scatter()

# Histograms: used to show distributions

iqs = np.random.normal(loc=100, size=200, scale=20)
plt.hist(iqs, color="lightgreen", edgecolor="black")

plt.title("IQ across a population")
plt.xlabel("IQ")
plt.ylabel("Number of people")


# Can use matplotlib for working with data and representing them
# too using pandas, can refer to docs for particular usage


# Go to ./plots/ to view the plots of this file!

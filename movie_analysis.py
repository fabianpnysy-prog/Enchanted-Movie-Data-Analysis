
#Part 1 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Enchanted"
print("My favorite movie is " + favMovie)


#Part 2 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])


#Part 3 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

favMovieBooleanList = movieData["movie_title"] == favMovie
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
comedyMovieBooleanList = movieData["genres"].str.contains("Comedy")

comedyMovieData = movieData.loc[comedyMovieBooleanList]

numOfMovies = comedyMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Comedy in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Comedy.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 4 Describe data
#min
min = comedyMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " Enchanted is rated [93] points higher than the lowest rated movie.")
print()

#find max
max = comedyMovieData["audience_rating"].max()
print("The max audience rating of the data set is:" + str(max))
print(favMovie + " Enchanted is rated [7] points lower than the highest rated movie.")
print()

#find mean
mean = comedyMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " [is higher than] the mean movie rating.")

#find median
median = comedyMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " [is higher than] the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 5 Create graphs
#Create histogram
plt.hist(comedyMovieData["audience_rating"],range=(0,100), bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audiece Ratings of Comedy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Comedy Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most comedy movies have audience ratings between 40 and 80, while very low and very high ratings are less common"
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data=comedyMovieData, x="audience_rating", y="critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0,100)
plt.ylim(0,100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, audience rating and critic rating present a positive correlation, while still showing some outliers "
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")

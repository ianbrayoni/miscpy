## The Restaurant Recommendation Problem

### Task

The problem we'll be tackling is a restaurant recommendation system.

We are given a list of restaurants that contains:

- The name of the restaurant.
- The percentage of people who recommended the restaurant.
- The price range of the restaurant.
- The type of food served by the restaurant.
- The program will make a recommendation to the user based on this data.

### The Problem:

Write a function that has three parameters:

1. a restaurant file that is open for reading,
2. the price range (one of $, $$, $$$ and $$$$), and
3. a list of cuisines.

_The function returns a list of restaurants (in that price range, serving at least one of those cuisines), and their ratings sorted from highest to lowest._



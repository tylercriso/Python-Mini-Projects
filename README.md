This is a collection of personal mini-projects that I've created to show my knowledge of the Python programming language.

Details of each mini-project and the skills used are below:

BankAccountList
A CLI program to simulate a bank telling system. By default, there are 20 bank accounts with randomized names and balances. The names come from RandomFullNameGenerator.py, which generates a random first and last name from a pool of names.
In the CLI, you can display all accounts, view a single account, and deposit/withdraw money into/from an account.
Skills used: classes / class functions, custom modules, random, for loops, list management, user input

CityWeather
A CLI program to enter a city and get the current weather via the Open Meteo API. Results shows the conditions (weather code), temperature, feels-like, humidity, windspeed, and sunrise/sunset times for the day.
The city is first entered into Open Mateo's geocoding API, which converts the user-inputted city into a latitude-longitude geolocation. Then, the latitude and longitude are fed as request parameters into the main weather API request.
Skills used: APIs, JSON, user input, datetime formatting, geolocation conversion

CountdownTimer
An extremely simple, 9-line program to demonstrate understanding of the time library and simulating time delay via time.sleep.
Skills used: time delay (via time library), user input

MultiplicationTableGenerator
Enter in a number, and the program will generate a times table up to a given range (default is 10).
Skills used: user input, for loops

NumberGuessingGame
The program stores a random number from 1 to 100, and the user must guess the number within 5 attempts.
After each attempt, the program tells the user if their guess was too high or too low.
Skills used: user input interpretation, while loops, random

PasswordGenerator
The program will generate a random password based off the users preferences.
The program asks the user what the password length should be and if it should include numbers, special characters, and capital letters.
Skills used: string manipulation, .join, random choice, user input, for loops

PokeAPI
A simple API practice CLI that lets the user enter in the name of a Pokemon, and the program will pull data from PokeAPI.
Skills used: APIs, JSON, user input

RandomFullNameGenerator
Used for the BankAccountList.py program to generate a random full name in the output of a string.
The generator pulls from two separate lists, one with first names and one with last names. Then, it uses a function to randomly choose a name from each list and combine as a single string.
Skills used: lists, random, functions

RockPaperScissors
A program to simulate a rock paper scissors game between the user and the computer.
Skills used: match statements, while loops, user input interpretation, random

TestFileAnalyzer
The user inputs the filename (or the location + filename if it is not within the same folder as the program), and the program analyzes the file for various statistics, such as total amount of characters in the file, words, sentences, and more.
Skills used: file handling, user input

ToDoList
A simple to-do list program that lets the user add, view, and complete tasks to the list.
Skills used: user input, match statements, for loops, user-defined data management

This is a non-exhaustive list that I will be continuing to add stuff to as my experience improves. Watch this space!


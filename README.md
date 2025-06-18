# Codsoft
# Task-1: CHATBOT WITH RULE-BASED RESPONSES

Here's a more detailed summary of my simple chatbot:

IMPORTS :

The datetime module is imported for date and time functions.

CHATBOT RESPONSE FUNCTION :

Converts user input to lowercase for consistent handling.
Uses conditional statements to respond based on specific keywords in the user's input:
Greets with "Hello" or "Hi" and asks for the user's name.
Provides the current time using datetime.now().strftime().
Provides the current date using datetime.today().strftime().
Extracts and uses the name if the input contains "my name is."
Introduces itself if asked, "What is your name?"
Ends the conversation with "Goodbye" or "Bye."
Asks the user to rephrase if the input doesn't match any predefined conditions.

MAIN LOOP :

Continuously runs until the user types "bye."
Prompts the user for input and prints the chatbot's response based on the chatbot_response function.
# Task-2: TIC-TAC-TOE AI

The Python code implements a Tic-Tac-Toe game where a player competes against an AI opponent.

IMPORTS :

The random module is used for generating random moves.

GAME INSTRUCTIONS:

The instructions variable explains the game rules and board format.

BOARD INITIALIZATION :

The sign_dict list represents the board with nine empty spaces.

FUNCTIONS :

1) print_board(): Displays the current board state.

2) take_input(): Prompts the player for a move and validates it.

3) is_moves_left(): Checks if any empty spaces are left on the board.

4) evaluate(): Checks if a player (X or O) has won the game by evaluating possible win 5)conditions (rows, columns, and diagonals).

6) minimax(): Implements the Minimax algorithm for the AI to make optimal moves.

7) find_best_move(): Uses the Minimax algorithm to find the best move for the AI.

MAIN FUNCTION :

Orchestrates the Game Flow:

Welcomes the player and displays instructions.
Prompts the player for their name and assigns signs (O for the player, X for the AI).
Alternates turns between the player and AI, using the Minimax algorithm for AI moves and take_input() for player moves.
Prints the board after each move and checks for win conditions.
Declares the winner or a tie based on the game outcome.

Finally,The game runs until either the player or AI wins, or the board is full, resulting in a tie.

# Task-4: RECOMMENDATION SYSTEM

The Python code uses content-based filtering to recommend movies based on their descriptions.

IMPORTS :

1) pandas for data manipulation.

2) TfidfVectorizer from sklearn for text vectorization.

3) linear_kernel from sklearn for calculating cosine similarity.

4) random for generating random numbers.

DATASET :

The code reads a sample movie dataset from a CSV file using pd.read_csv.

TF-IDF VECTORIZATION :

The TfidfVectorizer is initialized with English stop words to convert the movie descriptions into a matrix of TF-IDF features (tfidf_matrix).

COSINE SIMILARITY :

The cosine similarity of the TF-IDF matrix is calculated using linear_kernel to measure the similarity between movies.

RECOMMENDATION FUNCTION :

get_content_based_recommendations(title, num_recommendations):

1) Finds the index of the given movie title.

2) Calculates similarity scores for all movies with respect to the given movie.

3) Sorts the similarity scores in descending order.

4) Selects the top num_recommendations most similar movies (excluding the given movie itself).

5) Returns the titles of the recommended movies.

RANDOM SELECTION :

A random number of recommendations (num_recommendations) is chosen between 1 and 35.

A random movie title (movie_title) is selected from the dataset.

GET RECOMMENDATIONS :

The get_content_based_recommendations function is called with the randomly selected movie title and number of recommendations.

Finally,The recommended movie titles are printed.

This research examines the capabilities of Large Language Models (LLMs) in strategic decision-making through the game of Tic-Tac-Toe. We evaluated top LLMs, such as Jurassic2 (ai21.j2-ultra-v1), Claude2.1 (anthropic.claude-v2:1), Gemini-pro, GPT-3.5-Turbo, GPT-4, Llama2-70 (meta.llama2-70b-chat-v1), and Mistral-Large (mistral-large-latest), focusing on their understanding of rules and strategic planning. The outcomes of these tests are available in the test-output folder of this repository. The repository contains three types of output files: JSON, CSV, and TXT. The CSV files, specifically all_list.csv and all_illustration.csv, consolidate the contents from the 'list' and 'illustration' folders, which represent the two different prompt types used in the benchmarking process.

The JSON file offers comprehensive details encompassing the date/time, participants, outcome, length of the game, and every move made, covering both successful and unsuccessful efforts. An unsuccessful attempt is identified as one that targets a cell already taken in the 3x3 matrix, or when the response text fails to clearly indicate the subsequent action. Furthermore, the file captures the game's current state as communicated to the Large Language Model (LLM) and the LLM's replies for each action. In contrast, a more concise summary of the game is presented in a CSV file, omitting the intricate details of each move. The TXT file visually displays the sequence of game moves as illustrated.

A sample of JSON, CSV, and TXT files are given below:

Sample JSON file content:

{
    "datetime": "240308-175045",
    "player1": "gpt-4",
    "player2": "gemini-pro",
    "totalMoves": 5,
    "player1MovesAlreadyTaken": 0,
    "player2MovesAlreadyTaken": 0,
    "player1MovesOutOfBounds": 0,
    "player2MovesOutOfBounds": 0,
    "player1MovesInvalidFormat": 0,
    "player2MovesInvalidFormat": 0,
    "result": "gpt-4 X wins!",
    "gameDuration": "00:05",
    "promptType": "list",
    "moves": [
        {
            "no": 1,
            "player": 1,
            "row": 2,
            "col": 2,
            "valid": "Y",
            "promptType": "list",
            "currentStatus": "The moves by the first player (marked by X): None \nThe moves by the second player (marked by O): None \n",
            "response": "{'row': 2, 'column': 2}"
        },
        {
            "no": 2,
            "player": 2,
            "row": 1,
            "col": 1,
            "valid": "Y",
            "promptType": "list",
            "currentStatus": "The moves by the first player (marked by X): 2,2 \nThe moves by the second player (marked by O): None \n",
            "response": "{'row': 1, 'column': 1}"
        },
        {
            "no": 3,
            "player": 1,
            "row": 1,
            "col": 2,
            "valid": "Y",
            "promptType": "list",
            "currentStatus": "The moves by the first player (marked by X): 2,2 \nThe moves by the second player (marked by O): 1,1 \n",
            "response": "{'row': 1, 'column': 2}"
        },
        {
            "no": 4,
            "player": 2,
            "row": 3,
            "col": 1,
            "valid": "Y",
            "promptType": "list",
            "currentStatus": "The moves by the first player (marked by X): 1,2; 2,2 \nThe moves by the second player (marked by O): 1,1 \n",
            "response": "{'row': 3, 'column': 1}"
        },
        {
            "no": 5,
            "player": 1,
            "row": 3,
            "col": 2,
            "valid": "Y",
            "promptType": "list",
            "currentStatus": "The moves by the first player (marked by X): 1,2; 2,2 \nThe moves by the second player (marked by O): 1,1; 3,1 \n",
            "response": "{'row': 3, 'column': 2}"
        }
    ]
}


Sample CSV file content:

Ga-me-Time,PromptType,Player1,Player2,Result,TotalTime,TotalMoves,Player1InvalidAlreadyTaken,Player2InvalidAlreadyTaken,Player1InvalidFormat, Player2InvalidFormat, Play-er1OutOfBounds, Player2OutOfBounds 
240308-163604,list,gemini-pro,meta.llama2-70b-chat-v1,gemini-pro X wins!,00:12,10,0,1,0,0,0,0


Sample TXT file content:

Game #559
Prompt Type: list
Player 1: anthropic.claude-v2:1
Player 2: gpt-4
Date Time: 240307-202522
Game Duration: 00:16
Total Moves: 9
Player 1 Already Taken Moves: 0
Player 2 Already Taken Moves: 0
Player 1 Invalid Format Moves: 0
Player 2 Invalid Format Moves: 0
Player 1 Out of Bounds Moves: 0
Player 2 Out of Bounds Moves: 0
Result: Draw
Game Progress: 
X|.|.
.|.|.
.|.|.


X|O|.
.|.|.
.|.|.


X|O|.
.|X|.
.|.|.


X|O|.
.|X|.
.|.|O


X|O|X
.|X|.
.|.|O


X|O|X
.|X|.
O|.|O


X|O|X
.|X|.
O|X|O


X|O|X
.|X|O
O|X|O


X|O|X
X|X|O
O|X|O






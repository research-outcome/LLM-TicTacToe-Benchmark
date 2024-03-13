This study investigates the strategic decision-making abilities of Large Language Models (LLMs) via the game of Tic-Tac-Toe.

We tested leading LLMs including Jurassic-2 Ultra by AI21, Claude2.1 by Anthropic, Gemini-Pro by Google, GPT-3.5-turbo and GPT-4 by OpenAI, LLaMA2-70B by Meta, and Mistral-Large by Mistral, to assess their rule comprehension and strategic thinking.

You can find the output of the runs in this repository. There are three types of output files; JSON, CSV, and TXT. A sample for these files are given below:

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






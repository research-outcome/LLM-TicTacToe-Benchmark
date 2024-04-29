This repository has the output data of the following study. If you use the output data, please cite the publication:

**Topsakal O, Harper JB. Benchmarking Large Language Model (LLM) Performance for Game Playing via Tic-Tac-Toe. Electronics. 2024; 13(8):1532. https://doi.org/10.3390/electronics13081532**

By utilizing an Android mobile app coupled with web services, we facilitated Tic-Tac-Toe game playing among leading LLMs, including Jurassic-2 Ultra by AI21, Claude 2.1 by Anthropic, Gemini-Pro by Google, GPT-3.5-Turbo and GPT-4 by OpenAI, Llama2-70B by Meta, and Mistral Large by Mistral. Using a consistent prompt structure in 10 sessions for each LLM pair, we systematically collected data on wins, draws, and invalid moves across 980 games, employing two distinct prompt types (list and illustration) to vary the presentation of the game’s status. Our findings reveal significant performance variations among the LLMs. Notably, GPT-4, GPT-3.5-Turbo, and Llama2 secured the most wins with the list prompt, while GPT-4, Gemini-Pro, and Mistral Large excelled using the illustration prompt. GPT-4 emerged as the top performer, achieving victory with the minimum number of moves and the fewest errors for both prompt types. This research introduces a novel methodology for assessing LLM capabilities using a game that can illuminate their strategic thinking abilities.


![TicTacToe-GeminiPro-GPT4](https://github.com/research-outcome/LLM-TicTacToe-Benchmark/assets/136174718/be4c9543-802f-4ea4-9f3c-e639173d4d7a)


The outcomes of these tests are available in the test-output folder of this repository. The repository contains three types of output files: JSON, CSV, and TXT. The file names are formed as Player1_Player2_Result_PromptType_GameTime.ext, for example, gemini-pro_gpt-3.5-turbo_gpt-3.5-turbo O wins!_list_240308-162700.csv. Player names are Jurassic2 (ai21.j2-ultra-v1), Claude2.1 (anthropic.claude-v2:1), Gemini-pro, GPT-3.5-Turbo, GPT-4, Llama2-70 (meta.llama2-70b-chat-v1), and Mistral-Large (mistral-large-latest).

- The JSON file offers comprehensive details encompassing the date/time, participants, outcome, length of the game, and every move made, covering both successful and unsuccessful efforts. An unsuccessful attempt is identified as one that targets a cell already taken in the 3x3 matrix, or when the response text fails to clearly indicate the subsequent action. Furthermore, the file captures the game's current state as communicated to the Large Language Model (LLM) and the LLM's replies for each action.
- The CSV file presents a summary of the game, omitting the details of each move. The all_list.csv and all_illustration.csv consolidate the contents of csv files from the 'list' and 'illustration' folders, which represent the two different prompt types used in the benchmarking process.
- The TXT file visually displays the sequence of game moves.


A sample of JSON, CSV, and TXT files are given below:

Sample JSON file content:
```
{
   "datetime":"240308-175045",
   
   "player1":"gpt-4",
   
   "player2":"gemini-pro",
   
   "totalMoves":5,
   
   "player1MovesAlreadyTaken":0,
   
   "player2MovesAlreadyTaken":0,
   
   "player1MovesOutOfBounds":0,
   
   "player2MovesOutOfBounds":0,
   
   "player1MovesInvalidFormat":0,
   
   "player2MovesInvalidFormat":0,
   
   "result":"gpt-4 X wins!",
   
   "gameDuration":"00:05",
   
   "promptType":"list",
   
   "moves":[
   
      {
         "no":1,
         "player":1,
         "row":2,
         "col":2,
         "valid":"Y",
         "promptType":"list",
         "currentStatus":"The moves by the first player (marked by X): None \nThe moves by the second player (marked by O): None \n",
         "response":"{'row': 2, 'column': 2}"
      },
      
      {
         "no":2,
         "player":2,
         "row":1,
         "col":1,
         "valid":"Y",
         "promptType":"list",
         "currentStatus":"The moves by the first player (marked by X): 2,2 \nThe moves by the second player (marked by O): None \n",
         "response":"{'row': 1, 'column': 1}"
      },
      
      {
         "no":3,
         "player":1,
         "row":1,
         "col":2,
         "valid":"Y",
         "promptType":"list",
         "currentStatus":"The moves by the first player (marked by X): 2,2 \nThe moves by the second player (marked by O): 1,1 \n",
         "response":"{'row': 1, 'column': 2}"
      },
      
      {
         "no":4,
         "player":2,
         "row":3,
         "col":1,
         "valid":"Y",
         "promptType":"list",
         "currentStatus":"The moves by the first player (marked by X): 1,2; 2,2 \nThe moves by the second player (marked by O): 1,1 \n",
         "response":"{'row': 3, 'column': 1}"
      },
      
      {
         "no":5,
         "player":1,
         "row":3,
         "col":2,
         "valid":"Y",
         "promptType":"list",
         "currentStatus":"The moves by the first player (marked by X): 1,2; 2,2 \nThe moves by the second player (marked by O): 1,1; 3,1 \n",
         "response":"{'row': 3, 'column': 2}"
      }
   ]
}
```


Sample CSV file content:
```

GameTime,PromptType,Player1,Player2,Result,TotalTime,TotalMoves,Player1InvalidAlreadyTaken,Player2InvalidAlreadyTaken,Player1InvalidFormat, Player2InvalidFormat, Play-er1OutOfBounds, Player2OutOfBounds 

240308-163604,list,gemini-pro,meta.llama2-70b-chat-v1,gemini-pro X wins!,00:12,10,0,1,0,0,0,0
```


Sample TXT file content:

```
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

```



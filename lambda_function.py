# This code was utilized in the study called "Benchmarking Large Language Model (LLM) Performance for Game Playing via Tic-Tac-Toe"
# If you utilize the code, please cite the publication:
# Topsakal O, Harper JB. Benchmarking Large Language Model (LLM) Performance for Game Playing via Tic-Tac-Toe. Electronics. 2024; 13(8):1532. https://doi.org/10.3390/electronics13081532
# Note that the prompts utilized in the study was slightly different than what was used below.

# Oguzhan Topsakal, Ph.D., 2024


import json
import boto3

#print("boto3 Version: ", boto3.__version__)

#amazon
#{
#  "prompt": "\n\nHuman: Tic-tac-toe is a game for two players, played on a 3 by 3 grid. The first player uses Xs, and the second player uses Os to mark one of the nine squares in the grid. A player wins by placing 3 of their marks in a horizontal, vertical, or diagonal row. To prevent losing, a player may place a mark to block their opponent from creating a row of 3. The previous moves of the tic-tac-toe game are given in a format that moves are separated by ';'.  Each move first gives the row number and then the column separated by a comma. The previous moves are as follows: The moves by the first player (marked by X): 1,2; 1,3; 1,1. The moves by the second player (marked by O): 2,2; 3,3. You are a master at the Tic-tac-toe game, and you are unbeatable. You are the second player.  What would be your next move? Do not explain your move. Just give it in the format 'response: row number, column number' for an available position, such as 'response: 1,3' \n\nAssistant:",
#  "modelId": "amazon.titan-embed-text-v1",
#  "secret": "some-secret",
#  "type": "amazon"
#}

#anthropic
#{
#  "prompt": "\n\nHuman: Tic-tac-toe is a game for two players, played on a 3 by 3 grid. The first player uses Xs, and the second player uses Os to mark one of the nine squares in the grid. A player wins by placing 3 of their marks in a horizontal, vertical, or diagonal row. To prevent losing, a player may place a mark to block their opponent from creating a row of 3. The previous moves of the tic-tac-toe game are given in a format that moves are separated by ';'.  Each move first gives the row number and then the column separated by a comma. The previous moves are as follows: The moves by the first player (marked by X): 1,2; 1,3; 1,1. The moves by the second player (marked by O): 2,2; 3,3. You are a master at the Tic-tac-toe game, and you are unbeatable. You are the second player.  What would be your next move? Do not explain your move. Just give it in the format 'response: row number, column number' for an available position, such as 'response: 1,3' \n\nAssistant:",
#  "modelId": "anthropic.claude-v2:1",
#  "secret": "some-secret",
#  "type": "anthropic"
#}

#ai21
#{
#  "prompt": "Tic-tac-toe is a game for two players, played on a 3 by 3 grid. The first player uses Xs, and the second player uses Os to mark one of the nine squares in the grid. A player wins by placing 3 of their marks in a horizontal, vertical, or diagonal row. To prevent losing, a player may place a mark to block their opponent from creating a row of 3. The previous moves of the tic-tac-toe game are given in a format that moves are separated by ';'.  Each move first gives the row number and then the column separated by a comma. The previous moves are as follows: The moves by the first player (marked by X): 1,2; 1,3; 1,1. The moves by the second player (marked by O): 2,2; 3,3. You are a master at the Tic-tac-toe game, and you are unbeatable. You are the second player.  What would be your next move? Do not explain your move. Just give it in the format 'response: row number, column number' for an available position, such as 'response: 1,3' ",
#  "modelId": "ai21.j2-ultra-v1",
#  "secret": "some-secret",
#  "type": "ai21"
#}

#meta
#{
#  "prompt": "Tic-tac-toe is a game for two players, played on a 3 by 3 grid. The first player uses Xs, and the second player uses Os to mark one of the nine squares in the grid. A player wins by placing 3 of their marks in a horizontal, vertical, or diagonal row. To prevent losing, a player may place a mark to block their opponent from creating a row of 3. The previous moves of the tic-tac-toe game are given in a format that moves are separated by ';'.  Each move first gives the row number and then the column separated by a comma. The previous moves are as follows: The moves by the first player (marked by X): 1,2; 1,3; 1,1. The moves by the second player (marked by O): 2,2; 3,3. You are a master at the Tic-tac-toe game, and you are unbeatable. You are the second player.  What would be your next move? Do not explain your move. Just give it in the format 'response: row number, column number' for an available position, such as 'response: 1,3' ",
#  "modelId": "meta.llama2-70b-chat-v1",
#  "secret": "some-secret",
#  "type": "meta"
#}


#MODEL IDs
    #modelId = 'meta.llama2-13b-chat-v1'
    #modelId = 'meta.llama2-70b-chat-v1'
    #modelId = 'amazon.titan-embed-text-v1'
    #modelId = 'amazon.titan-text-express-v1'
    #modelId = 'amazon.titan-text-lite-v1'
    #modelId = 'anthropic.claude-v2' #Claude 2
    #modelId = 'ai21.j2-ultra-v1'
    #modelId = 'anthropic.claude-v2:1' #Claude 2.1
    #modelId = 'anthropic.claude-3-sonnet-20240229-v1:0' #Claude 3 Sonnet



accept = 'application/json'
contentType = 'application/json'

brt = boto3.client('bedrock-runtime')

def lambda_handler(event, context):

    print("event: ", event)
    #prompt = "Tic-tac-toe is a game for two players, played on a 3 by 3 grid. The first player uses Xs, and the second player uses Os to mark one of the nine squares in the grid. A player wins by placing 3 of their marks in a horizontal, vertical, or diagonal row. To prevent losing, a player may place a mark to block their opponent from creating a row of 3. The previous moves of the tic-tac-toe game are given in a format that moves are separated by ';'.  Each move first gives the row number and then the column separated by a comma. The previous moves are as follows: The moves by the first player (marked by X): 1,2; 1,3; 1,1. The moves by the second player (marked by O): 2,2; 3,3. You are a master at the Tic-tac-toe game, and you are unbeatable. You are the second player.  What would be your next move? Do not explain your move. Just give it in the format 'response: row number, column number' for an available position, such as 'response: 1,3' "
    secret = event['secret']
    if (secret != 'some secret TTT'):
        return {'statusCode':200,'body': 'unauthorized access'}
        
    prompt = event['prompt']
    modelId = event['modelId']
    type = event['type']
    
    print("prompt: ", prompt )
    print("modelId: ", modelId )
    print("type: ", type )
    
    body = " "
    
    if (type == 'anthropic'):
        prompt = "Human: " + prompt + " \n\nAssistant:"
        body = json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 300
            })
    
    if (type == 'amazon'):
        prompt = prompt + " [INST] suggest your next move in a concise JSON format, such as {'row': 1, 'column': 3}, without any additional commentary. [/INST]"
        body = json.dumps({
            "inputText": prompt
            })

    if (type == 'meta'):
        prompt = prompt + " [INST] suggest your next move in a concise JSON format, such as {'row': 1, 'column': 3}, without any additional commentary. [/INST]"
        body = json.dumps({
            "prompt": prompt
            })

    if (type == 'ai21'):
        body = json.dumps({
            "prompt": prompt
            })

    print("body: ", body)
    
    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    print("response: ", response)
    response_body = json.loads(response.get('body').read())
    print("response_body: ", response_body)
    response_text = ""

    if (type == 'ai21'):
        response_text = response_body.get('completions')[0].get('data').get('text')
        print("response_text: ", response_text)
       
    if (type == 'meta'):
        response_text = response_body.get('generation')
        print("response_text: ", response_text)
        
    if (type == 'amazon'):
        #results = response_body.get('results')
        #print("results: ", results)
        #for result in response_body['results']:
        #    print(f"Token count: {result['tokenCount']}")
        #    print(f"Output text: {result['outputText']}")
        #    print(f"Completion reason: {result['completionReason']}")
        #results = response_body['results']
        #firstResult = results[0]
        #response_text = result['outputText']
        #print(firstResult)
        #response_text = json.loads(response.get('body').read()).get('results')[0].get('outputText')
        response_text = response_body.get('results')[0].get('outputText')
        
        print("response_text: ", response_text)

    if (type == 'anthropic'):
        response_text = response_body.get('completion')
        print("response_text: ", response_text)

    return {
        'statusCode':200,
        'body': json.dumps(response_text)
    }
    

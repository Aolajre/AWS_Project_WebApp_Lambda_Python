  # import the JSON utility package
import json
# import the Python math library
import math

# define the handler function that the Lambda service will use at entry point
def lambda_handler(event, context):
    
# extract the two numbers from Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))
    
# return a properly formatted JSON object
    return{
      'statusCode' : 200,
      'body' : json.dumps('Your answer is ' + str(mathResult)) 
    }  
    
    

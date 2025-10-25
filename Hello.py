import json
def lambda_handler(event, context):
    # For console test event (JSON)
    # For HTTP Function URL trigger (GET/POST)
    
    message = "Hello from my first AWS Lambda function!"
    
    # If called through Function URL, include query param
    name = None
    if event.get("queryStringParameters"):
        name = event["queryStringParameters"].get("name")

    if name:
        message = f"Hello, {name}! Welcome to AWS Lambda 🚀"

    # Always return HTTP-style response for Function URL
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": message})
    }

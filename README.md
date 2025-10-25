# Elevate_Labs_Day4_Lamba

# AWS Lambda Hello World (Python) ( For Testing)

This is a simple **serverless function** deployed on **AWS Lambda** via the console.

##  Objective
To understand serverless computing and create a basic cloud function that executes automatically without managing any servers.

## Function Code
See Hello world function code in Hello.py

## Tools Used

1. AWS Lambda (console)
2. AWS CloudWatch Logs
3. Python 3.11 Runtime

## Console steps — do these now
  1. Open Lambda in AWS Console
         In AWS Console, Services → Lambda.
  2. Create function

     Click Create function → Author from scratch.
     Function name: hello
     Runtime: Python 3.13 
     Architecture: leave default (x86_64) unless you want arm.
      Permissions → Execution role:
     Choose Create a new role from AWS policy templates.
     Role name: Hello
     Policy templates: select Create basic Lambda permissions (this attaches AWSLambdaBasicExecutionRole which allows CloudWatch logs).
     Click Create function.
  The console will create the function and open the function configuration page.

  <img width="1756" height="810" alt="image" src="https://github.com/user-attachments/assets/299464cd-8c29-4ff4-a78f-1fd6f094a1f7" />

  3. Create a Function URL (simple HTTP endpoint)

  In the function page left panel → Configuration → scroll to Function URL 

    Click Create function URL.
    Auth type: choose None 
    Leave CORS disabled unless you need browser cross-domain calls.
  Click Create.

  <img width="1275" height="357" alt="image" src="https://github.com/user-attachments/assets/1b31bda8-6940-4d45-af1c-6cc69051f502" />

  4. Copy code

<img width="919" height="506" alt="image" src="https://github.com/user-attachments/assets/e6e22797-a047-458e-a533-99dd1e6a3c74" />

  5. Test it.

     Event: Hello
     Format: {}

<img width="669" height="232" alt="image" src="https://github.com/user-attachments/assets/5ffc820f-b3f0-4dc5-b9fa-261e06f6d289" />

  6. Test in Browser with function URL

     URL: https://7wuiu5fqtdfhqt4lgli56wyq5i0llpxp.lambda-url.eu-north-1.on.aws/

<img width="515" height="99" alt="image" src="https://github.com/user-attachments/assets/5947b2f3-e900-4efb-9833-f466209dbb69" />

**Behavior:**
- Returns a JSON message `"Hello from my first AWS Lambda function!"`
- Supports query parameter `name` for personalized greeting.

# -----------------





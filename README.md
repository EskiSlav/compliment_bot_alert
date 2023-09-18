# Compliment Bot Alert
This is code for the lambda function which generates a compliment with OpenAI service, translates it via AWS Translate, and sends compliments by the trigger.

## Technologies
- [SAM](https://aws.amazon.com/serverless/sam/). To build and Test lambda function;
- Python. Main language.

## Usage
When this repository is placed near the [aws_infra](https://github.com/EskiSlav/aws_infra) repository it can be deployed via Terraform into the AWS cloud.

## Development
All of the code is stored under the `bot` folder. <be>
To add new features please go to the 

### Testing
The command for building and testing
```bash
sam build && sam local invoke "BotFunction" --event events/event.json
```

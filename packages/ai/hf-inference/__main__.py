import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Args:
    def __init__(self, args):
        self.args = args
        self.prompt = args.get("prompt")
        self.model = args.get("model", "openai-gpt-oss-120b")
        self.max_tokens = args.get("max_tokens", 100)
        self.role = args.get("role", "user")

    def validate(self) -> bool:
        if not self.prompt:
            return False
    
        return True


class Request():
    def __init__(self, args: Args) -> None:
        self.url = "https://inference.do-ai.run/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('do-token')}"
        }
        print(self.headers)
        self.data = {
            "model": args.model,
            "messages": [
                {
                    "role": args.role,
                    "content": f"{args.prompt}"
                }
            ],
            "max_tokens": args.max_tokens
        }
    

def main(args):
    args = Args(args)
    validated_args = args.validate()

    if not validated_args:
        return {"body": {"error": "Missing 'prompt' in request body"}, "statusCode": 400}

    request = Request(args)

    response = requests.post(request.url, headers=request.headers, json=request.data)
    return response.json()

if __name__ == "__main__":
    returned_value = main({
        "prompt": "Hello, how are you?"
    })
    print(returned_value)
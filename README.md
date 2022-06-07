# FastAPI Json Web Token

Repository to learn how to use and validate and use a **Json Web Token** with FastAPI.

## Requirements:

- python3.8+
```zsh
pip3 install "fastapi[ALL]"
pip3 install pyjwt
pip3 install python-dotenv
```

## How can I get a Token?

You can use Swagger UI or Postman, both works.

1. Create token:
- http://localhost:8000/api/login

The body of this path operation is:
- 'username': 'maucoder'
- 'password': any password

We're not using a Data base, for this reason the unique valid username is *"mauricio"*.

Then you will see a string, that's the token.

2. Validate token:
- http://localhost:8000/verify/token

The unique requirement in the path operation is a Header:
- token bareer

The response must be:
```
"success"
```

3. Use the token to get github users by country and page:
- http://localhost:8000/users/github:
The requirement in this path operation is:
- Body:
    - country: str
    - page: int
- Header:
    - token bareer

The response must be a JSON object with Github users models like:
- avatar: url
- id: UUID
- profile: url

etc...

### Conclusions:

Hey! You completed this simple Json web token guide with fastapi, I expect this guide works for you.

If you want to see more guides or simple tutorials, send me a DM in my Twitter: [maucoder]('https://twitter.com/maucoder')
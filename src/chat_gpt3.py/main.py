import openai
from dotenv import load_dotenv
from get_env import print_env

load_dotenv()

try:

    env = print_env(['api_key'])
    print(env)
    openai.api_key = env['api_key']

    #openai.api_key = "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"


    # list engines
    #engines = openai.Engine.list()
    # print the first engine's id
    #print(engines.data[0].id)
    # create a completion
    #completion = openai.Completion.create(engine="ada", prompt="Hello world")
    # print the completion
    #print(completion.choices[0].text)

    model_engine =("text-davinci-003")

    while True:
        prompt = input("Como posso ajuda-lo?: ")

        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
        )

        response = completion.choices[0].text
        print(response)

except Exception as e:
    print(f"Um erro inesperado aconteceu:{e}")
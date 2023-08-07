"""
This is a simple script that utilizes the OpenAI API to generate responses based on user messages.
"""

import openai

def read_api_key_from_file(file_path):
    """
    Read the API key from a file.

    Parameters:
        file_path (str): The path to the file containing the API key.

    Returns:
        str: The API key read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def get_res(msg: str) -> str:
    """
    Generate a response using the OpenAI API based on the input message.

    Parameters:
        msg (str): The input message.

    Returns:
        str: The generated response.
    """
    api_key = read_api_key_from_file("open_ai.txt")
    openai.api_key = api_key
    if msg.startswith("!!??!!"):
        # Extract the message after "!!??!!" to use as input for OpenAI
        user_msg = msg[len("!!??!!"):].strip()

        # Call the OpenAI API to generate a response using chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model engine
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.7,  # Controls the randomness of the response
            max_tokens=500,    # Controls the maximum length of the generated response
            stop=["\n"]       # Stops the response at the first line break
        )
        return response.choices[0].message["content"].strip()
    if msg.startswith("!!image!!"):
        # Extract the message after "!!??!!" to use as input for OpenAI
        user_msg = msg[len("!!image!!"):].strip()

        # Call the OpenAI API to generate a response using chat completions
        response = openai.Image.create(
            prompt = user_msg,
            n = 1,
            size = "256x256"
        )
        return response['data'][0]['url']

    return 'What?'

import openai
from openai import OpenAI
import time
from checker import checker


client = OpenAI(
api_key="YOUR-OPENAI-KEY"
)

def get_model_response(prompt, retries=5, delay=1):
    for attempt in range(retries):
        try:
            response = client.responses.create(
                model="gpt-5.2",
                input=prompt,
                temperature=0.0,  # Low creativity for a more direct response
                top_p=0.5,        # Lower sampling
            )

            return {
                    "text": response.output_text,
                    "attempts": attempt + 1,
                    "model": "gpt-5.2"
                    }


        except Exception as e:
            print(
                f"API error on attempt {attempt + 1}/{retries}: {e}"
            )

            if attempt == retries - 1:
                break

            time.sleep(delay)
            delay *= 2  # exponential backoff

    print("Exceeded maximum retry attempts.")
    return None

def prompter(chapter, instructions):

        prompt = f'Make the chapter more readable and dyslexia friendly. \n{instructions}\n Here is the text: \n{chapter}'

        # Log the prompt (optional)
        print(f"Sending prompt")

        #time.sleep(1)
        # Get the response from the model
        response = get_model_response(prompt)

        #time.sleep(1)
        # Add the response and prompt to the response_data list
        #response_data["responses"].append({
        #    "prompt": prompt,
        #    "response": response
        #})
        print(type(response), ' response type')
        print(response["text"], ' response ')
        return response["text"]

    
# Save the response to a text file (for task 2)
#with open(model + task + "miss_data.json", "w") as json_file:
    #json.dump(response_data, json_file, indent=4)

# Test
response = get_model_response("Hello world")
if response:
    print(response)
    
    
    

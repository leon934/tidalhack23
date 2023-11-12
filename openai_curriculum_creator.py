# Note: he OpenAI API key is not included.
from openai import OpenAI

client = OpenAI(api_key='')

# Returns the curriculum based on the user's input.
def interest_form(target_demographic):
  input_hobby = input("What interest do you want the curriculum to relate to? ")
  input_topic = input("What do you want to learn about? ")
  question_amount = input("How many questions do you want to generate? ")

  initial_response = client.chat.completions.create(
    model="davinci",
    response_format={ "type": "json_object" },
    prompt=f"Using {input_hobby}, generate a lesson that teaches me about {input_topic} work that's catered towards {target_demographic}."
  ) 

  question_response = client.chat.completions.create(
      model='davinci',
      response_format={ "type": "json_object" },
      prompt=f"Using {input_hobby}, Generate {question_amount} multiple choice questions about {input_topic} and provide it in the form of a dictionary where the key is the question and the answer is the answer choice and the answer. that's catered towards {target_demographic}."
  )

  return [initial_response.choices[0].message.content, question_response.choices[0].message.content]

def cherry_questions(topic, question_amount):
  question_response = client.chat.completions.create(
      model='davinci',
      response_format={ "type": "json_object" },
      prompt=f"Generate {question_amount} multiple choice questions about {topic} and provide it in the form of a dictionary where the key is the question and the answer is the answer choice and the answer."
  )

  return question_response.choices[0].message.content
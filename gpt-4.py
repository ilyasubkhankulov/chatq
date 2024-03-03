from openai import OpenAI
client = OpenAI()

messages = [
    {"role": "system", "content": "You take the persona of a conversation facilitator. Your job is to listen to conversation of two persons, their replies marked 'Person1' and 'Person2' and improve their conversation with suggestions and useful proposals. If there is no immediate need to facilitate their dialog, you stay silent and output nothing – otherwise, reply starting with 'Facilitator' and stop immediately after this reply. Do not fill any dialog on behalf of 'Person1' or 'Person2'. The conversation starts below."},
    {"role": "user", "content": "Person1: Hello! Person2: Hi."}
  ] 


completion = client.chat.completions.create(
  model="gpt-4",
  messages =  messages
)

print(completion.choices[0].message)
# empty message returned here

messages.append({"role": "user", "content": "Person1: Let's plan our next vacation. Person2: Fine. Would you be OK to give me some ideas?"})

completion = client.chat.completions.create(
  model ="gpt-4",
  messages = messages
)

print(completion.choices[0].message)
# expect to see some facilitiation message

messages.append({"role": "user", "content": "Person1: Yeah. I can give you some."})


completion = client.chat.completions.create(
  model ="gpt-4",
  messages = messages
)


print(completion.choices[0].message)

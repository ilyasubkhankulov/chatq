from openai import OpenAI
client = OpenAI()

def create_image(content):

   messages = [
       {"role": "system", "content": "Your job is to create a DALL-E3 prompt that graphically captures the user message below. Instruct DALL-E3 to insert no text in the image.."},
       {"role": "user", "content": content}]

   completion = client.chat.completions.create(
     model="gpt-4",
     messages =  messages
   )

   response = client.images.generate(
     model="dall-e-3",
     prompt=completion.choices[0].message.content,
     size="1024x1024",
     quality="standard",
     n=1,
   )

   image_url = response.data[0].url
   print(image_url)



messages = [
    {"role": "system", "content": "You take the persona of a conversation facilitator. Your job is to listen to conversation of two persons, their replies marked 'Person1' and 'Person2' and improve their conversation with suggestions and useful proposals. If there is no immediate need to facilitate their dialog, you stay silent and output nothing – otherwise, reply starting with 'Facilitator' and stop immediately after this reply. Do not fill any dialog on behalf of 'Person1' or 'Person2' and do not address them by names. The conversation starts below."},
    {"role": "user", "content": "Person1: Hello! Person2: Hi."}
  ] 

#
# Test run follows here
#

completion = client.chat.completions.create(
  model="gpt-4",
  messages =  messages
)

# empty message should be returned here
print(completion.choices[0].message)

if completion.choices[0].message.content:
   create_image(completion.choices[0].message.content)


messages.append({"role": "user", "content": "Person1: Let's plan our next vacation. Person2: Fine. Would you be OK to give me some ideas?"})

completion = client.chat.completions.create(
  model ="gpt-4",
  messages = messages
)

print(completion.choices[0].message)
# expect to see some facilitiation message

if completion.choices[0].message.content:
   create_image(completion.choices[0].message.content)


messages.append({"role": "user", "content": "Person1: Yeah. I can give you some."})


completion = client.chat.completions.create(
  model ="gpt-4",
  messages = messages
)

print(completion.choices[0].message.content)

if completion.choices[0].message.content:
   create_image(completion.choices[0].message.content)

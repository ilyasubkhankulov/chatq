
async def create_image(content):








#
# Test run follows here
#
async def main():
  

  # empty message should be returned here
  print(completion.choices[0].message)

  if completion.choices[0].message.content:
    create_image(completion.choices[0].message.content)


  messages.append({"role": "user", "content": "Person1: Hi Person2: Hey"})

  completion = await client.chat.completions.create(
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

if __name__ == '__main__':
    asyncio.run(main())


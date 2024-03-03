import asyncio
import redis
from openai import AsyncOpenAI
redis_client = redis.Redis(host='localhost', port=6379, db=0, encoding='utf8', decode_responses=True)

openai_client = AsyncOpenAI(api_key='')

async def create_image(message):
    messages = [
        {"role": "system", "content": "Your job is to create a DALL-E3 prompt that graphically captures the user message below. Instruct DALL-E3 to insert no text in the image.."},
        {"role": "user", "content": message}]
    image_prompt = await openai_client.chat.completions.create(
        model="gpt-4",
        messages = messages
    )
    
    print(image_prompt)
    response = await openai_client.images.generate(
        model="dall-e-3",
        prompt=image_prompt.choices[0].message.content,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    url = response.data[0].url
    print(url)
    redis_client.set('chatq:image_url', url)


async def send_first(last_message):
    print('send first message')
    old_prompt = {"role": "system", "content": "You take the persona of a conversation facilitator. Your job is to \
listen to conversation of two persons, their replies marked 'Person1' and 'Person2'. \
Improve their conversation with suggestions and useful proposals. If there is no immediate \
need to facilitate their dialog, you stay silent and output nothing – otherwise, reply starting \
with 'Facilitator' and stop immediately after this reply. Do not fill any dialog on behalf of 'Person1'\
or 'Person2' and do not address participants by names. The conversation starts below."}
    messages = [
        old_prompt,
        {"role": "user", "content": last_message[0]},
        {"role": "user", "content": last_message[1]}
    ] 
    print(messages)
    completion = await openai_client.chat.completions.create(
        model="gpt-4",
        messages = messages
    )
    await create_image(completion.choices[0].message.content)

async def send_others(last_message):
    print('Send other requests')
    
    messages = [
        {"role": "user", "content": message} for message in last_message
    ] 
    print(messages)
    completion = await openai_client.chat.completions.create(
        model="gpt-4",
        messages = messages
    )
    print(completion)
    await create_image(completion.choices[0].message.content)
    

async def get_chat():
    chat_history = []
    while True:
        new_chat_history = redis_client.lrange('chatq:chat', 0, -1)
        len_new_chat_history = len(new_chat_history)
        len_history = len(chat_history)
        if len_new_chat_history > len_history:
            if len_new_chat_history == 2:
                await send_first(new_chat_history[-2:])
            elif len_new_chat_history > 1:
                await send_others(new_chat_history[-2:])
            chat_history = new_chat_history

        await asyncio.sleep(1)

# Example usage
async def main():
    await get_chat()

if __name__ == '__main__':
    asyncio.run(main())
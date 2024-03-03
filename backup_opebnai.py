import time

from openai import OpenAI

client = OpenAI(api_key=token)

prompt = "3D geometrical objects, such as cylinder, box, etc. Make sure to include the formula for the volume underneath each one."
model = "dall-e-3"

def main() -> None:
    start = time.perf_counter()
    response = client.images.generate(prompt=prompt, model=model)
    print(f'Done processing in {time.perf_counter()-start} seconds')
    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()

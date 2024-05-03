from openai import OpenAI


def main():
    client = OpenAI()

    # Chat completion example
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            },
            {
                "role": "user",
                "content": "Compose a poem that explains the concept of recursion in programming.",
            },
        ],
    )

    print(completion.choices[0].message)

    # Embeddings example
    response = client.embeddings.create(
        model="text-embedding-ada-002", input="The food was delicious and the waiter..."
    )

    print(response)

    # Image example
    response = client.images.generate(
        prompt="A cute baby sea otter", n=2, size="1024x1024"
    )

    print(response)


if __name__ == "__main__":
    main()

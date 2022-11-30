import wikipedia

prompt = input(">>> ")
while prompt != "":
    try:
        page = wikipedia.page(prompt, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary:\n{wikipedia.summary(prompt)}")
        print(f"Url: {page.url}")

    except wikipedia.exceptions.DisambiguationError as suggestions:
        print(suggestions)
    except wikipedia.exceptions.PageError:
        print(f"{prompt} does not match any pages. Try another prompt")
    prompt = input(">>> ")

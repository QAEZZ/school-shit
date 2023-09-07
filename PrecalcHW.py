import json


def questions() -> dict:
    doContinue: bool = True
    questions = []
    header = input("Header: ")
    while doContinue:
        question = input("Question: ")
        questions.append(question)

        moreQuestions: str = input("More questions? [Y/n] ").lower()

        if moreQuestions == "y":
            doContinue = True
        else:
            doContinue = False


    return {"header": header, "questions": [questions]}


def main() -> None:
    isContinuing = True
    data = []

    while isContinuing:
        section_data = questions()
        data.append(section_data)

        moreSections = input("\nAnother Section? [Y/n] ").lower()
        if moreSections == "y":
            isContinuing = True
        else:
            isContinuing = False

        
    json_data = json.dumps({"data": data})

    print(f"\n\n{data}")
    print(f"\n\n{json_data}")


if __name__ == "__main__":
    main()

"""
{
  "data": [
    {
      "header": "Do the do for 1-2",
      "questions": [
        [
          "[1] Do that",
          "[2] Do this"
        ]
      ]
    },
    {
      "header": "Do the thingy for 3-5",
      "questions": [
        [
          "[3] Do thingy",
          "[4] Do the do with the thingy",
          "[5] Do the final thingy"
        ]
      ]
    }
  ]
}
"""

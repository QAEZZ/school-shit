import json
import os
import pyautogui
import time

WRITE_INTERVAL=.02

def questions() -> dict:
    doContinue: bool = True
    questions = []
    header = input("Header: ")
    while doContinue:
        question = input("Question: ")
        questions.append(question.trim())

        moreQuestions: str = input("More questions? [Y/n] ").lower()

        if moreQuestions == "y":
            doContinue = True
        else:
            doContinue = False

    return {"header": header, "questions": questions}


def main() -> None:
    os.system("cls")
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
    
    os.system("cls")
    input("press enter to type to document, typing will start 5 seconds after.\n\nmake sure to have enable markdown detection tools>preferenceseseses")
    time.sleep(5)

    json_data = json.loads(json.dumps({"data": data}))

    sections = json_data["data"]
    for section in sections:
        h = f"**{section['header']}**"
        print(h)
        pyautogui.typewrite(f"{h}\n", WRITE_INTERVAL)
        for q in section["questions"]:
            formatted_q = f"**{q}\n\n".replace(". ", ".** ")
            print(formatted_q)
            pyautogui.typewrite(formatted_q, WRITE_INTERVAL)
        print("\n\n")
        pyautogui.typewrite("\n\n", WRITE_INTERVAL)


if __name__ == "__main__":
    main()

"""
{
  "data": [
    {
      "header": "Do the do for 1-2",
      "questions": [
        "[1] Do that",
        "[2] Do this"
      ]
    },
    {
      "header": "Do the thingy for 3-5",
      "questions": [
        "[3] Do thingy",
        "[4] Do the do with the thingy",
        "[5] Do the final thingy"
      ]
    }
  ]
}
"""

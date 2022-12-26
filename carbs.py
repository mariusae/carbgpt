#!/usr/bin/env python3

import openai
import os
import sys

prompt = """
You are an agent helping to estimate the amount of carbohydrates in a meal. You should provide an estimate of the carbohydrate contents in a meal, but do not provide detailed reasoning about the answer.

Here are some examples:

EXAMPLE 1:
====
FOOD: a piece of bread with cheese and jam.
YOUR ESTIMATE: about 25 grams
====

EXAMPLE 2:
====
FOOD: a small burrito from chipotle
YOUR ESTIMATE: about 45 grams
====

"""

def main():
  assert len(sys.argv) == 2

  question = prompt + "FOOD: " + sys.argv[1]
  response = openai.Completion.create(
    model="text-davinci-003", prompt=question, temperature=0.5, best_of=10, n=3, max_tokens=50)
  answer = response.choices[0].text
  print(answer.split("YOUR ESTIMATE: ")[1])


if __name__ == '__main__':
  openai.api_key = os.environ.get("OPENAI_API_KEY")
  main()

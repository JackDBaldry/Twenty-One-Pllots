## Twenty-One-Pllots

Twenty One Pllots is a text based adventure game in the style of Zork inspired by Twenty One Pilots lore. The user plays as the character Clancy from the lore as he faces his nemesis Nico. The game starts with Clancy in a car which blows up, stranding him in the middle of nowhere. Nico is threatening to try and capture Clancy. The main goal is to evade Nico, defeat him and decide the fate of the city of Dema. If you manage to defeat Nico your moral score will determine the fate of Dema.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JackDBaldry/Twenty-One-Pllots/blob/main/code/TwentyOnePllots.ipynb)

This project demonstrates key programming concepts such as loops, conditionals, functions, and user input/output.

## Features

Morality score (Screenshots plot description)

Puzzle structure (Screenshots cant defeat dragon)

Menu (Screenshots dema districts)

Multiple endings based on player choices (Screenshots hero, simple, broke and villain ending)

Branching story logic (Screenshots add item to inventory, have item and not have time)

Looping validation (Screenshots looping validation)

Player Inventory (Screenshots have inventory item)

Written as a Jupyter/Colab notebook.

## Code

[code/TwentyOnePllots.ipynb](code/TwentyOnePllots.ipynb) – Interactive notebook

[code/TwentyOnePllots.py](code/TwentyOnePllots.py) – Plain Python script

[code/TwentyOnePllots_TestingSuite.py](code/TwentyOnePllots_TestingSuite.py) – Plain Python script of automated tests for each story ending

## How to Open

**On GitHub:**

Click `[code/TwentyOnePllots.ipynb](code/TwentyOnePllots.ipynb)' to view directly.

**In Google Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JackDBaldry/Twenty-One-Pllots/blob/main/code/TwentyOnePllots.ipynb)

**Locally:** 

Download the file and open with Jupyter Notebook.

**Tests**

## To run all automated ending tests: python -m unittest code/TextGamePrototype_TestEndings.py

## Documentation

[docs/TwentyOnePllotsInitialConceptWrittenScript.txt](docs/TwentyOnePllotsInitialConceptWrittenScript.txt) – Initial game concept prototype script

[docs/TwentyOnePllotsPseudocode.txt](docs/TwentyOnePllotsPseudocode.txt) - Edexcel iGCSE Computer Science standard Pseudocode for the game

**Flowcharts**

[docs/MainTwentyOnePllotsFlowchart.png](docs/MainTwentyOnePllotsFlowchart.png) – Initial Game logic flowchart

**TO DO** - New fearures flowcharts showing later design modifications

**Screenshots of Gameplay**

[docs/TwentyOnePllotsScreenshot1.png](docs/TwentyOnePllotsScreenshot1.png) – Gameplay screenshot (raw image)

Add links to all screenshot file names

## License

This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.

## Challenges

First major code application (Time w3schools, personal research, used to colab IDE and debugging tools)
Since we were making this during time I was still learning to code, it made it difficult. What helped me was using w3schools and other personal research on coding so that way the code was efficient and actually worked.

Mapping the branching structure to reach all endings (Doing flowcharts and pseduocode)
Another challenge was figuring out how to reach all the different endings in the game since there are 13 different endings. The intial flowcharts and pseudocode helped with this as it gave a solid foundation for us to build off of and helped to make sure it all functioned as it should.

Figuring out dema puzzle logic (Doing flowcharts and pseudocode and lots testing)
We applied similar logic when it came to doing the dema section of the game as this has lots of little sections and was difficult to make. Since there were no intial flowcharts or pseudocode for these sections of the game, we made new ones for this section of the game which made it much easier to figure out how to get all of the logic working. We also made sure we tested all of the possible outcomes each time we made any changes to the code to make sure it still worked as it should.

Testing (Getting blackbox testing with external users to test gameplay)
We needed a good way to test whether the game was user friendly and made sense to someone who had no involvement in the devolopment of the game, so we did blackbox testing to ensure it all worked smoothly and in an understandable way.

Team coding (Problems: Source control, labour division. Solution: Task allocation and communication
Since it was a team project, it came with issues such as source control and labour division. To overcome these issues we would use task allocation and good communication to make sure that we either weren't working on an important task or that we were both working on the same thing when we didn't need to be.

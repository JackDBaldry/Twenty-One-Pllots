## Twenty-One-Pllots

Twenty One Pllots is a text based adventure game in the style of Zork inspired by Twenty One Pilots lore. The user plays as the character Clancy from the lore as he faces his nemesis Nico. The game starts with Clancy in a car which blows up, stranding him in the middle of nowhere. Nico is threatening to try and capture Clancy. The main goal is to evade Nico, defeat him and decide the fate of the city of Dema. If you manage to defeat Nico your moral score will determine the fate of Dema.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JackDBaldry/Twenty-One-Pllots/blob/main/code/TwentyOnePllots.ipynb)

This project demonstrates key programming concepts such as loops, conditionals, functions, and user input/output.

## Features

We added an Easter egg where if you type "Clancy" then it gives you a different message than for example typing in your own name. Clancy is the main character in Twenty one pilots lore which is why it is an easter egg. 

Generic username:
<img width="1976" height="427" alt="Genericusernamept1" src="https://github.com/user-attachments/assets/2e9688bb-6817-4de4-b5e4-acf4a4bbaaf5" />
<img width="1956" height="497" alt="Genericusernamept2" src="https://github.com/user-attachments/assets/897bf2fe-dd59-443d-88d8-990d3bd56f21" />

Easter egg username:
<img width="1931" height="346" alt="Eastereggusername" src="https://github.com/user-attachments/assets/65831599-9714-416c-b148-453f69eab7bb" />


We added a morality score which you gain either good (YBC) or bad (BG) morality score. This in turn can change the outcome or result for different aspects of the game.


<img width="1922" height="704" alt="Plotdescriptionpt2" src="https://github.com/user-attachments/assets/61b64b1c-3369-45d2-8184-33515d608881" />
<img width="1948" height="647" alt="Plotdescriptionpt3" src="https://github.com/user-attachments/assets/1f58baeb-37c1-437c-9426-5882285e59ae" />
<img width="1969" height="666" alt="Plotdescriptionpt1" src="https://github.com/user-attachments/assets/397e724f-87cc-4eee-be13-4529469ef929" />


We added puzzle structure which means you have to unlock certain things before being able to do an action. For example, the screenshot shows you can't defeat the dragon without a weapon. 


<img width="1995" height="473" alt="Cantdefeatdragon" src="https://github.com/user-attachments/assets/b5ea65f2-875a-49bf-8e4b-77c3a3e8aeff" />


We added a menu which makes the areas of Dema clear to the user. 


<img width="1926" height="717" alt="Demadistricts" src="https://github.com/user-attachments/assets/4b9b7ecc-31af-4563-9af5-6e7402e5d47e" />


We added multiple different endings which are all based on the players choices. Here are some examples:

This ending shows that the user didn't have enough YBC to go with the Banditos so they are stuck in Dema and lose:
<img width="1950" height="722" alt="BrokeEnding" src="https://github.com/user-attachments/assets/65283134-109f-47a6-807e-579e3000a96e" />

This ending shows that the user were as good as they can be and freed as many districts as possible making it a good ending:
<img width="2027" height="548" alt="Heroending" src="https://github.com/user-attachments/assets/67b1ba7e-8b23-468f-a2cf-1b119a70645d" />

This ending shows a simple death or in other words way to lose:
<img width="1920" height="717" alt="Simpledeathpt1" src="https://github.com/user-attachments/assets/d02a6070-e73d-498f-ab3a-7e2347edaefc" />
<img width="1945" height="714" alt="Simpledeathpt2" src="https://github.com/user-attachments/assets/d6482576-a650-476a-b626-3fc7a530efe2" />

This ending shows that the user were as bad as they can be making it the bad ending:
<img width="1927" height="746" alt="Badendingpt1" src="https://github.com/user-attachments/assets/81accc6b-f0b1-4d2a-bd08-96bfac48b080" />
<img width="1876" height="713" alt="Badendingpt2" src="https://github.com/user-attachments/assets/367ab629-e366-4629-9ea6-cd78bced3df0" />


Branching story logic.

This shows how items get added to the user inventory based off of their decisions:
<img width="1919" height="701" alt="Additemtoinventorypt1" src="https://github.com/user-attachments/assets/e4f28eaf-7c36-4d75-980c-537a0010c717" />
<img width="1947" height="677" alt="Additemtoinventorypt2" src="https://github.com/user-attachments/assets/f675b056-71eb-4c9f-b982-de6fb76b759f" />
<img width="1930" height="706" alt="Additemtoinventorypt3" src="https://github.com/user-attachments/assets/8d7be192-223a-4a72-a8d8-4e9d947d29e9" />

This shows what happens when the user has the item required:
<img width="1991" height="476" alt="Haveinventoryitem" src="https://github.com/user-attachments/assets/4ea28df7-e7f5-45e7-80e5-7b04d373b6e8" />

This shows what happens when the user doesn't have the item required:
<img width="1966" height="558" alt="Donthaveinventoryitem" src="https://github.com/user-attachments/assets/37a51f50-dd60-4056-92fc-c6484053885e" />


We added looping validation to make the sure the game can't break if the user mis-inputs for example a letter instead of a number.


<img width="1923" height="709" alt="Loopingvalidation" src="https://github.com/user-attachments/assets/40850fdc-4441-484d-b632-e70a5d6c78dd" />


We added a player inventory which can have things added to it.


<img width="1991" height="476" alt="Haveinventoryitem" src="https://github.com/user-attachments/assets/dea8911d-e951-4b0e-a201-7c3542a8c170" />


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

To run all automated ending tests: python -m unittest code/TwentyOnePllots_TestingSuite.py

## Documentation

[docs/TwentyOnePllotsInitialConceptWrittenScript.txt](docs/TwentyOnePllotsInitialConceptWrittenScript.txt) – Initial game concept prototype script

[docs/TwentyOnePllotsPseudocode.txt](docs/TwentyOnePllotsPseudocode.txt) - Edexcel iGCSE Computer Science standard Pseudocode for the game

**Flowcharts**

[docs/MainTwentyOnePllotsFlowchart.png](docs/MainTwentyOnePllotsFlowchart.png) – Initial Game logic flowchart

[docs/TwentyOnePllots_Dema_Flowchart.png](docs/TwentyOnePllots_Dema_Flowchart.png) - Dema logic flowchart

[docs/TwentyOnePllots_CREDITS_Flowchart.png](docs/TwentyOnePllots_CREDITS_Flowchart.png) - Credits logic flowchart

**TO DO** - New fearures flowcharts showing later design modifications

**Screenshots of Gameplay**

[docs/TwentyOnePllotsScreenshot1.png](docs/TwentyOnePllotsScreenshot1.png) – Gameplay screenshot (raw image)

Add links to all screenshot file names


## License

This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.

## Challenges

First major code application 

Since we were making this during the time I was still learning to code, it made it difficult. What helped me was using w3schools and other personal research on coding as well as getting used to the Colab IDE. That way the code was efficient and actually worked.

Mapping the branching structure to reach all endings 

Another challenge was figuring out how to reach all the different endings in the game since there are 13 different endings. The initial flowcharts and pseudocode helped with this as it gave a solid foundation for us to build off of and helped to make sure it all functioned as it should.

Figuring out Dema puzzle logic

We applied similar logic when it came to doing the Dema section of the game as this has lots of little sections and was difficult to make. Since there were no initial flowcharts or pseudocode for these sections of the game, we made new ones for this section of the game which made it much easier to figure out how to get all of the logic working. We also made sure we tested all of the possible outcomes each time we made any changes to the code to make sure it still worked as it should.

Testing

We needed a good way to test whether the game was user friendly and made sense to someone who had no involvement in the development of the game, so we did blackbox testing to ensure it all worked smoothly and in an understandable way.

Team coding 

Since it was a team project, it came with issues such as source control and labour division. To overcome these issues we would use task allocation and good communication to make sure that we weren't working on an important task simultaneously and that everyone had a similar workload.

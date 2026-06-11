
'''
JACK TO DO

1. Fix all unqualified functions and variables
Anywhere you wrote main, take_item, inventory, BG, gameOn, room6, etc. —
change to game.main, game.take_item, game.inventory, game.BG, game.gameOn, game.room6, etc.
This is because the game is being imported now so they are no longer global.

Examples:

output = run_and_capture(game.main)

game.take_item("apple", game.inventory)
assert "apple" in game.inventory

game.inventory.append(game.soup)
game.BG = 5

assert game.gameOn is False
assert game.YBC == 1

game.bowl = "bowl"
game.inventory = []
game.gameOn = True

Use find and replace to do this quickly. After doing find/replace search for
these leftovers and fix them to be sure: end_Credits, main, gameOn, inventory,
BG, YBC, room6, exploreDema used without game.

The only things that should be unqualified are reset_state,
run_and_capture and local variables like inputs.

2. Fix the end_Credits stub pattern
As it stubs end_Credits in the test file, not the game module you need:

real_end_Credits = game.end_Credits
game.end_Credits = lambda *args, **kwargs: False
...
game.end_Credits = real_end_Credits

so in ending tests you need:

reset_state()

real_end_Credits = game.end_Credits
game.end_Credits = lambda *args, **kwargs: False

real_input = __builtins__.input
__builtins__.input = fake_input

try:
  output = run_and_capture(game.main) # or game.scene_a, etc.
finally:
  __builtins__.input = real_input
  game.end_Credits = real_end_Credits

assert game.gameOn is False

3. Remember not to use "globals" - they must not exist in the test file.

'''

'''

CORRECT EXAMPLE for Test E:

print("Running Ending Test E — Death by Campers")

reset_state()

# Stub end_Credits INSIDE the game module
real_end_Credits = game.end_Credits
game.end_Credits = lambda *args, **kwargs: False

# Ordered scripted inputs:
scripted_inputs = iter([
    "CamperTest",
    "",
    "2",
    "B1",
    "C2",
    "D1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        return ""

real_input = __builtins__.input
__builtins__.input = fake_input

try:
    # Run the main game function (from the imported module)
    output = run_and_capture(game.main)
finally:
    __builtins__.input = real_input
    game.end_Credits = real_end_Credits

# --- Assertions ---
assert "You get eaten" in output, "Ending 3 (campers) text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test E passed\n")

'''

'''

CORRECT EXAMPLE FOR Test 1 take_item

print("Running test: take_item()")

reset_state()

inputs = iter(["y"])

def fake_input(prompt=""):
    print(prompt, end="")
    return next(inputs)

real_input = __builtins__.input
__builtins__.input = fake_input

try:
    game.take_item("apple", game.inventory)
finally:
    __builtins__.input = real_input

assert "apple" in game.inventory, "Item was not added to inventory."

print("✓ take_item() passed\n")

'''

'''

CORRECT EXAMPLE FOR exploreDema

print("Running test: exploreDema()")

reset_state()

inputs = iter(["x", "0"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(inputs)
    except StopIteration:
        return "0"

real_input = __builtins__.input
__builtins__.input = fake_input

try:
    output = run_and_capture(game.exploreDema)
finally:
    __builtins__.input = real_input

assert "Please enter a number" in output, "Did not handle invalid non-numeric input as expected."

print("✓ exploreDema() input-handling test passed\n")

'''

'''

CORRECT EXAMPLE FOR test 4 room6

print("Running test: room6()")

reset_state()

inputs = iter(["y", "WRONGCODE"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(inputs)
    except StopIteration:
        return "n"

real_input = __builtins__.input
__builtins__.input = fake_input

try:
    output = run_and_capture(game.room6)
finally:
    __builtins__.input = real_input

assert "ACCESS DENIED" in output, "Expected failure message not shown."

print("✓ room6() try/except/else test passed\n")

'''


# ================================================================
# HOW TO RUN THESE TESTS
# ================================================================
# ▶ Option 1 – Jupyter / Colab
#    1. Clone the repo inside your notebook:
#    JACK CHECK     !git clone https://github.com/JackDBaldry/Twenty-One-Pllots.git
#    2. Change into the code folder:
#         %cd Twenty-One-Pllots/code
#    3. Run this file:
#         !python TwentyOnePllots_TestingSuite.py
#
# ▶ Option 2 – Standard .py file from a terminal/IDE
#    1. Save this file as TwentyOnePllots_TestingSuite.py
#       in the same folder as TwentyOnePllots.py:
#
#         Twenty-One-Pllots/
#            code/
#               TwentyOnePllots.py
#               TwentyOnePllots_TestingSuite.py
#
#    2. From a terminal:
#         cd Twenty-One-Pllots/code
#         python TwentyOnePllots_TestingSuite.py
#
#    This runs all unittests.
#
#    (Inside the code below, unittest.main(argv=[''], exit=False)
#     lets tests run in notebooks without stopping the kernel.
#     If running as a normal script you can simply use unittest.main().)
# ================================================================


#Use !wget to fetch the raw file from GitHub
#This downloads the file into the notebook’s current working directory so Python can import it.
#Remove the two below comment markers to use in a notebook like colab
#!git clone https://github.com/JackDBaldry/Twenty-One-Pllots.git - comment out if you are running it from a terminal/IDE
# %cd Twenty-One-Pllots/code

#Import Twenty One Pllots Game
from io import StringIO
import io
from contextlib import redirect_stdout
import TwentyOnePllots as game


# ============================================================
# UTILITIES USED BY ALL TEST CELLS
# ============================================================

"""
Resets the game’s global variables so each test start clean.
This ensures one test cannot influence another test.
"""
def reset_state():
    game.BG = 0
    game.YBC = 0
    game.moralityTracker = 0
    game.gameOn = True
    game.inventory = []
    game.capture_TB = False


def run_and_capture(func, *args, **kwargs):
    """
    Runs a function while capturing printed output.
    This allows tests to inspect what was printed without
    showing it inside the notebook.
    """
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()

print("Utilities loaded.")

# ============================================================
# ENDING TEST E — Death by Campers (ending3)
# Demonstrates: Mocking a full path through multiple scenes
# ============================================================

print("Running Ending Test E — Death by Campers")

reset_state()

# Stub end_Credits so ending3 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Player name
# 2) Press Enter after name
# 3) scene_a() choice: "2" (jump out into a field)
# 4) scene_a2() choice: "B1" (high road up towards a forest)
# 5) scene_a2_b1() choice: "C2" (Stay outside and continue)
# 6) scene_a2_b1() choice: "D1" (Ask to join them)
# 7) Press Enter at credits
scripted_inputs = iter([
    "CamperTest",
    "",
    "2",
    "B1",
    "C2",
    "D1",
    "" # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending3
output = run_and_capture(main)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "You get eaten" in output, "Ending 3 (campers) text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test E passed\n")

# ============================================================
# TEST 1 — take_item()
# Demonstrates:
# - Mocking input() safely
# - Assertions
# - Teaching how item pickup logic works
# ============================================================

print("Running test: take_item()")

reset_state()

# Fake input sequence: the student function will call input("y/n")
inputs = iter(["y"])  # simulate user choosing "yes"

def fake_input(prompt=""):
    print(prompt, end="")   # show prompt to the teacher
    return next(inputs)

# Override input temporarily
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the function under test
take_item("apple", inventory)

# Restore input immediately after test
__builtins__.input = real_input

# The actual test condition
assert "apple" in inventory, "Item was not added to inventory."

print("✓ take_item() passed\n")

# ============================================================
# TEST 2 — remove_item()
# Teaching:
# - How removal from inventory is validated
# - Why tests must set up preconditions
# ============================================================

print("Running test: remove_item()")

reset_state()
inventory.append("key")   # Precondition: item must exist first

remove_item("key", inventory)

assert "key" not in inventory, "Item was not removed."

print("✓ remove_item() passed\n")

# ============================================================
# TEST 3 — exploreDema() menu input handling
# Teaching:
# - How the game copes with invalid input (non-numeric)
# - How a valid numeric choice then exits the menu
# - How to avoid infinite loops in tests by using a safe fallback
# ============================================================

print("Running test: exploreDema()")

reset_state()   # make sure BG, YBC, inventory, gameOn etc. are clean

# We simulate TWO user inputs:
#  1) "x"  → invalid (not a number) → should trigger "Please enter a number."
#  2) "0"  → valid exit choice → exploreDema() should return
inputs = iter(["x", "0"])

def fake_input(prompt=""):
    """
    Fake version of input() for this test only.

    - First call returns "x"   (invalid, not a digit)
    - Second call returns "0"  (valid exit choice)
    - Any further calls (just in case) also return "0"
      so the menu will always exit instead of looping forever.
    """
    print(prompt, end="")   # still show the prompt in notebook output for the teacher
    try:
        return next(inputs)
    except StopIteration:
        # SAFE FALLBACK: "0" is always a valid "exit" choice for exploreDema()
        return "0"

# Patch built-in input() with our fake one
real_input = __builtins__.input
__builtins__.input = fake_input

# Run exploreDema() and capture its output so it doesn't spam the notebook
output = run_and_capture(exploreDema)

# Restore the real input() function
__builtins__.input = real_input

# Optional: you can assert on the text if you want to be stricter:
#  - it should have complained at least once with "Please enter a number."
assert "Please enter a number" in output, "Did not handle invalid non-numeric input as expected."

print("✓ exploreDema() input-handling test passed\n")

# ============================================================
# TEST 4 — room6()
# Teaching:
# - try / except / else demonstration
# - Checking the “ACCESS DENIED” branch
# - Why we need an infinite-safe fallback for test inputs
# ============================================================

print("Running test: room6()")

reset_state()

# Scripted inputs:
# 1) "y" → attempt password entry
# 2) "WRONGCODE" → fail
inputs = iter(["y", "WRONGCODE"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(inputs)
    except StopIteration:
        return "n"  # fallback; prevents accidental infinite loops

real_input = __builtins__.input
__builtins__.input = fake_input

output = run_and_capture(room6)

__builtins__.input = real_input

assert "ACCESS DENIED" in output, "Expected failure message not shown."

print("✓ room6() try/except/else test passed\n")

# ============================================================
# TEST 5 — Multiple exceptions
# Teaching:
# - try / except (ValueError, TypeError)
# - else branch executes when no exception occurs
# ============================================================

print("Running test: multiple exceptions")

def demo_multi(x):
    try:
        if x == 1:
            raise ValueError("value broken")
        elif x == 2:
            raise TypeError("wrong type")
    except (ValueError, TypeError):
        return "caught"
    else:
        return "no error"

assert demo_multi(1) == "caught"
assert demo_multi(2) == "caught"
assert demo_multi(999) == "no error"

print("✓ multiple exception-block test passed\n")

# ============================================================
# TEST 6 — try / finally
# Teaching:
# - that finally ALWAYS runs even if an exception occurs
# ============================================================

print("Running test: try/finally")

log = []

def demo_finally():
    try:
        log.append("try block")
        raise RuntimeError("boom")
    finally:
        log.append("finally block")

try:
    demo_finally()
except RuntimeError:
    pass  # expected

assert log == ["try block", "finally block"]

print("✓ try/finally test passed\n")

# ============================================================
# TEST 7 — Exception with argument
# Teaching:
# - how to inspect the message stored inside an exception
# ============================================================

print("Running test: exception with argument")

try:
    raise ValueError("Custom error message")
except ValueError as e:
    assert str(e) == "Custom error message"

print("✓ exception argument test passed\n")

# HERE ARE FEW EXAMPLES OF TESTING YOUR ENDINGS

# ============================================================
# ENDING TEST A — Good Ending (Player shares normal soup)
# Robust version with full input mocking to prevent hanging
# ============================================================

print("Running Ending Test A — Good soup ending")

reset_state()

# --- Set minimal state ---
inventory.append(soup)
BG = 0
YBC = 0

# Ordered scripted inputs:
# 1) G2 → fight
# 2) s  → choose soup
scripted_inputs = iter(["G2", "s"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        # Use scripted inputs first
        return next(scripted_inputs)
    except StopIteration:
        # SAFETY DEFAULTS:
        # - "n" declines cloak
        # - "" satisfies end_Credits() prompt
        # - "s" works if chooseWeapon() asks again
        if "cloak" in prompt.lower():
            return "n"
        if "press enter" in prompt.lower():
            return ""
        return "s"   # safe fallback weapon

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the battle
output = run_and_capture(scene_finalbattle)

# Restore input
__builtins__.input = real_input

# --- Assertions ---
assert "shared your" in output.lower(), "Good ending text missing."
assert YBC == 1, "YBC should increase by +1 in good ending."

print("✓ Ending Test A passed\n")

# ============================================================
# ENDING TEST B — Bad Ending (BG >= 5)
# Demonstrates:
# - Direct testing of moral point thresholds
# - No need to enter the battle sequence
# - Mocking input() to bypass the end_Credits pause
# ============================================================

print("Running Ending Test B — Bad moral ending")

reset_state()

BG = 5  # threshold for bad ending
YBC = 0

# ---- Mock input() so end_Credits() does NOT pause ----
def fake_input(prompt=""):
    print(prompt, end="")  # show prompt, but auto-return instantly
    return ""              # simulate pressing Enter

real_input = __builtins__.input
__builtins__.input = fake_input

# ---- Run test ----
output = run_and_capture(scene_fightresult)

# Restore real input()
__builtins__.input = real_input

# ---- Assertions ----
assert "You are worse than" in output or "rule Dema" in output, \
       "Bad ending did not trigger at BG >= 5."

print("✓ Ending Test B passed\n")

# ============================================================
# ENDING TEST C — Betrayal ending (Hand Torchbearer to Nico)
# PLEASE ADD CORRECT ENDING NUMBER
# Demonstrates:
# - Setting a flag (capture_TB)
# - Mocking menu choice "G3"
# - Checking inventory and BG updates
# ============================================================

print("Running Ending Test C — Betrayal ending")

reset_state()

capture_TB = True   # key requirement
BG = 0
YBC = 0

# Final battle will ask:
# G1 = run
# G2 = fight
# G3 = hand over Torchbearer
inputs = iter(["G3"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(inputs)
    except StopIteration:
        return "G3"

real_input = __builtins__.input
__builtins__.input = fake_input

output = run_and_capture(scene_finalbattle)

__builtins__.input = real_input

# --- Assertions ---
assert "Betraying the Banditos" in output, "Betrayal text missing."
assert battleItem in inventory, "Did not receive Nico's cloak."
assert BG == 5, "BG should increase by +5 for betrayal."

print("✓ Ending Test C passed\n")

# ============================================================
# SCENE A TEST 1 — Option 1 triggers ending1 (car death)
# Demonstrates:
# - Mocking name input + "Press Enter" pause + numeric menu choice
# - Stubbing end_Credits() so we can assert gameOn cleanly
# ============================================================

print("Running Scene A Test 1 — Option 1 triggers ending1")

reset_state()

# Ensure expected globals exist for scene_a
bowl = "bowl"
inventory = []
gameOn = True

# Stub end_Credits so ending1 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Inputs:
# 1) name
# 2) press enter pause
# 3) menu choice
inputs = iter(["Clancy", "", "1"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(inputs)
    except StopIteration:
        return ""

real_input = __builtins__.input
__builtins__.input = fake_input

output = run_and_capture(scene_a)

__builtins__.input = real_input
end_Credits = real_end_Credits  # restore

# --- Assertions ---
assert "we've been expecting you" in output, "Clancy greeting missing."
assert "Your car bursts into flames" in output, "Death text missing (ending1 not reached)."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Scene A Test 1 passed\n")

# ============================================================
# ENDING TEST 2 — Hut Arrow Trap (ending2)
# Demonstrates: Mocking a full path to a specific ending
# ============================================================

print("Running Ending Test 2 — Hut Arrow Trap")

reset_state()

# Stub end_Credits so ending2 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Player name
# 2) Press Enter after name
# 3) scene_a() choice: "2" (jump out into a field)
# 4) scene_a2() choice: "B1" (high road up towards a forest)
# 5) scene_a2_b1() choice: "C1" (Go inside)
# 6) Press Enter at credits
scripted_inputs = iter([
    "ArrowTest",
    "",
    "2",
    "B1",
    "C1",
    "" # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending2
output = run_and_capture(main)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "Arrow trap inside the hut. You die." in output, "Ending 2 (arrow trap) text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 2 passed\n")

# ============================================================
# ENDING TEST 3 — Campers Join (ending3)
# Demonstrates: Mocking a full path to the campers ending
# ============================================================

print("Running Ending Test 3 — Campers Join")

reset_state()

# Stub end_Credits so ending3 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Player name
# 2) Press Enter after name
# 3) scene_a() choice: "2"
# 4) scene_a2() choice: "B1"
# 5) scene_a2_b1() choice: "C2" (Stay outside)
# 6) Camper choice: "D1" (Ask to join)
# 7) Press Enter at credits
scripted_inputs = iter([
    "CamperTest",
    "",
    "2",
    "B1",
    "C2",
    "D1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending3
output = run_and_capture(main)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "campers" in output.lower(), "Ending 3 (campers join) text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 3 passed\n")

# ============================================================
# ENDING TEST 4 — Ignore Campers (ending4)
# Demonstrates: Mocking a full path to the ignore campers ending
# ============================================================

print("Running Ending Test 4 — Ignore Campers")

reset_state()

# Stub end_Credits so ending4 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Player name
# 2) Press Enter after name
# 3) scene_a() choice: "2"
# 4) scene_a2() choice: "B1"
# 5) scene_a2_b1() choice: "C2" (Stay outside)
# 6) Camper choice: "D2" (Ignore them and continue)
# 7) Press Enter at credits
scripted_inputs = iter([
    "IgnoreTest",
    "",
    "2",
    "B1",
    "C2",
    "D2",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending4
output = run_and_capture(main)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "continue" in output.lower(), "Ending 4 (ignore campers) text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 4 passed\n")

# ============================================================
# ENDING TEST 5 — Banditos Decline (ending5)
# Demonstrates: Calling ending5() from scene_banditos()
# ============================================================

print("Running Ending Test 5 — Banditos Decline")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Stub end_Credits so ending5 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_banditos() choice: "D5" (Decline)
# 2) Press Enter at credits
scripted_inputs = iter([
    "D5",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_banditos)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "stay trapped in dema forever" in output.lower(), "Ending 5 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 5 passed\n")

# ============================================================
# ENDING TEST 6 — Banditos Rejected (ending6)
# Demonstrates: Calling ending6() from scene_banditos()
# ============================================================

print("Running Ending Test 6 — Banditos Rejected")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force YBC to 0 so option D6 fails
YBC = 0

# Stub end_Credits so ending6 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_banditos() choice: "D6" (Put on jumpsuit, but no YBC)
# 2) Press Enter at credits
scripted_inputs = iter([
    "D6",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        # Safe fallback
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_banditos)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "you cannot pay" in output.lower(), "Ending 6 text missing."
assert "you remain in dema" in output.lower(), "Ending 6 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 6 passed\n")

# ============================================================
# ENDING TEST 7 — Recaptured at Camp (ending7)
# Demonstrates: Calling ending7() from scene_camp()
# ============================================================

print("Running Ending Test 7 — Recaptured at Camp")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Stub end_Credits so ending7 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_camp() choice: "E1" (Leave immediately)
# 2) Press Enter at credits
scripted_inputs = iter([
    "E1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_camp)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "re-captures you" in output.lower(), "Ending 7 text missing."
assert "stuck in dema forever" in output.lower(), "Ending 7 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 7 passed\n")

# ============================================================
# ENDING TEST 8 — Caught and Returned (ending8)
# Demonstrates: Calling ending8() from scene_finalbattle()
# ============================================================

print("Running Ending Test 8 — Caught and Returned")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Ensure Torchbearer capture state doesn't matter
capture_TB = False

# Stub end_Credits so ending8 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_finalbattle() choice: "G1" (Run away)
# 2) Press Enter at credits
scripted_inputs = iter([
    "G1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_finalbattle)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "you are caught and returned to dema" in output.lower(), "Ending 8 text missing."
assert "you failed your mission" in output.lower(), "Ending 8 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 8 passed\n")

# ============================================================
# ENDING TEST 9 — Fight and Die (ending9)
# Demonstrates: Calling ending9() from scene_fightresult()
# ============================================================

print("Running Ending Test 9 — Fight and Die")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force BG to 4 to trigger ending9()
BG = 4

# Stub end_Credits so ending9 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Press Enter at credits
scripted_inputs = iter([
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_fightresult)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "you attempt to fight but die" in output.lower(), "Ending 9 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 9 passed\n")

# ============================================================
# ENDING TEST 10 — Spared by Villain (ending10)
# Demonstrates: Calling ending10() from scene_fightresult()
# ============================================================

print("Running Ending Test 10 — Spared by Villain")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force conditions to trigger ending10()
BG = 3
villain = "Nico"  # Ensure villain name exists for f-string

# Stub end_Credits so ending10 sets gameOn to a known value
real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Press Enter at credits
scripted_inputs = iter([
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
output = run_and_capture(scene_fightresult)

# Restore input and end_Credits
__builtins__.input = real_input
end_Credits = real_end_Credits

# --- Assertions ---
assert "takes pity on you" in output.lower(), "Ending 10 text missing."
assert "lets you crawl away" in output.lower(), "Ending 10 text missing."
assert gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 10 passed\n")

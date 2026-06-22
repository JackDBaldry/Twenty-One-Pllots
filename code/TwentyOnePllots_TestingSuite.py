# ================================================================
# HOW TO RUN THESE TESTS
# ================================================================
# ▶ Option 1 – Jupyter / Colab
#    1. Clone the repo inside your notebook:
#    !git clone https://github.com/JackDBaldry/Twenty-One-Pllots.git
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
!git clone https://github.com/JackDBaldry/Twenty-One-Pllots.git #comment this out if you are running it from a terminal/IDE
%cd Twenty-One-Pllots/code #comment this out if you are running it from a terminal/IDE

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
game.real_end_Credits = game.end_Credits
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
game.scripted_inputs = iter([
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
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending3
game.output = run_and_capture(game.main)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "You get eaten" in game.output, "Ending 3 (campers) text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

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

# The function will call input("y/n")
game.inputs = iter(["y"])  # simulate user choosing "yes"

def fake_input(prompt=""):
    print(prompt, end="")   # show prompt to the user
    return next(game.inputs)

# Override input temporarily
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the function under test
game.take_item("apple", game.inventory)
# Restore input immediately after test
__builtins__.input = game.real_input

# The actual test condition
assert "apple" in game.inventory, "Item was not added to inventory."

print("✓ take_item() passed\n")

# ============================================================
# TEST 2 — remove_item()
# - How removal from inventory is validated
# - Why tests must set up preconditions
# ============================================================

print("Running test: remove_item()")

reset_state()
game.inventory.append("key")   # Precondition: item must exist first
game.remove_item("key", game.inventory)

assert "key" not in game.inventory, "Item was not removed."

print("✓ remove_item() passed\n")

# ============================================================
# TEST 3 — exploreDema() menu input handling
# - How the game copes with invalid input (non-numeric)
# - How a valid numeric choice then exits the menu
# - How to avoid infinite loops in tests by using a safe fallback
# ============================================================

print("Running test: exploreDema()")

reset_state()  # make sure BG, YBC, inventory, gameOn etc. are clean

# We simulate TWO user inputs:
#  1) "x"  → invalid (not a number) → should trigger "Please enter a number."
#  2) "0"  → valid exit choice → exploreDema() should return
game.inputs = iter(["x", "0"])

def fake_input(prompt=""):
    """
    Fake version of input() for this test only.

    - First call returns "x"   (invalid, not a digit)
    - Second call returns "0"  (valid exit choice)
    - Any further calls (just in case) also return "0"
      so the menu will always exit instead of looping forever.
    """
    print(prompt, end="")   # show the prompt in the notebook output
    try:
        return next(game.inputs)
    except StopIteration:
        # SAFE FALLBACK: "0" is always a valid "exit" choice for exploreDema()
        return "0"

# Patch built-in input() with our fake one
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run exploreDema() and capture its output so it doesn't spam the notebook
game.output = run_and_capture(game.exploreDema)

# Restore the real input() function
__builtins__.input = game.real_input

# Optional: you can assert on the text if you want to be stricter:
#  - it should have complained at least once with "Please enter a number."
assert "Please enter a number" in game.output, "Did not handle invalid non-numeric input as expected."

print("✓ exploreDema() input-handling test passed\n")

# ============================================================
# TEST 4 — room6()
# - try / except / else demonstration
# - Checking the “ACCESS DENIED” branch
# - Why we need an infinite-safe fallback for test inputs
# ============================================================

print("Running test: room6()")

reset_state()

# Scripted inputs:
# 1) "y" → attempt password entry
# 2) "WRONGCODE" → fail
game.inputs = iter(["y", "WRONGCODE"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.inputs)
    except StopIteration:
        return "n"  # fallback; prevents accidental infinite loops

game.real_input = __builtins__.input
__builtins__.input = fake_input

game.output = run_and_capture(game.room6)

__builtins__.input = game.real_input

assert "ACCESS DENIED" in game.output, "Expected failure message not shown."

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

game.log = []

def demo_finally():
    try:
        game.log.append("try block")
        raise RuntimeError("boom")
    finally:
        game.log.append("finally block")

try:
    demo_finally()
except RuntimeError:
    pass  # expected

assert game.log == ["try block", "finally block"]

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
game.inventory.append(game.soup)
game.BG = 0
game.YBC = 0

# Ordered scripted inputs:
# 1) G2 → fight
# 2) s  → choose soup
game.scripted_inputs = iter(["G2", "s"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        # Use scripted inputs first
        return next(game.scripted_inputs)
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
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the battle
game.output = run_and_capture(game.scene_finalbattle)

# Restore input
__builtins__.input = game.real_input

# --- Assertions ---
assert "shared your" in game.output.lower(), "Good ending text missing."
assert game.YBC == 1, "YBC should increase by +1 in good ending."

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

game.BG = 5  # threshold for bad ending
game.YBC = 0

# ---- Mock input() so end_Credits() does NOT pause ----
def fake_input(prompt=""):
    print(prompt, end="")  # show prompt, but auto-return instantly
    return ""              # simulate pressing Enter

game.real_input = __builtins__.input
__builtins__.input = fake_input

# ---- Run test ----
game.output = run_and_capture(game.scene_fightresult)

# Restore real input()
__builtins__.input = game.real_input

# ---- Assertions ----
assert "You are worse than" in game.output or "rule Dema" in game.output, \
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

game.capture_TB = True   # key requirement
game.BG = 0
game.YBC = 0

# Final battle will ask:
# G1 = run
# G2 = fight
# G3 = hand over Torchbearer
game.inputs = iter(["G3"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.inputs)
    except StopIteration:
        return "G3"

game.real_input = __builtins__.input
__builtins__.input = fake_input

game.output = run_and_capture(game.scene_finalbattle)

__builtins__.input = game.real_input

# --- Assertions ---
assert "Betraying the Banditos" in game.output, "Betrayal text missing."
assert game.battleItem in game.inventory, "Did not receive Nico's cloak."
assert game.BG == 5, "BG should increase by +5 for betrayal."

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
game.bowl = "bowl"
game.inventory = []
game.gameOn = True

# Stub end_Credits so ending1 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Inputs:
# 1) name
# 2) press enter pause
# 3) menu choice
game.inputs = iter(["Clancy", "", "1"])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.inputs)
    except StopIteration:
        return ""

game.real_input = __builtins__.input
__builtins__.input = fake_input

game.output = run_and_capture(game.scene_a)

__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits  # restore

# --- Assertions ---
assert "we've been expecting you" in game.output, "Clancy greeting missing."
assert "Your car bursts into flames" in game.output, "Death text missing (ending1 not reached)."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Scene A Test 1 passed\n")

# ============================================================
# ENDING TEST 2 — Hut Arrow Trap (ending2)
# Demonstrates: Mocking a full path to a specific ending
# ============================================================

print("Running Ending Test 2 — Hut Arrow Trap")

reset_state()

# Stub end_Credits so ending2 sets gameOn to a known value
game.real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Player name
# 2) Press Enter after name
# 3) scene_a() choice: "2" (jump out into a field)
# 4) scene_a2() choice: "B1" (high road up towards a forest)
# 5) scene_a2_b1() choice: "C1" (Go inside)
# 6) Press Enter at credits
game.scripted_inputs = iter([
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
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending2
game.output = run_and_capture(game.main)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "Arrow trap inside the hut. You die." in game.output, "Ending 2 (arrow trap) text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 2 passed\n")

# ============================================================
# ENDING TEST 3 — Campers Join (ending3)
# Demonstrates: Mocking a full path to the campers ending
# ============================================================

print("Running Ending Test 3 — Campers Join")

reset_state()

# Stub end_Credits so ending3 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
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
game.scripted_inputs = iter([
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
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending3
game.output = run_and_capture(game.main)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "campers" in game.output.lower(), "Ending 3 (campers join) text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 3 passed\n")

# ============================================================
# ENDING TEST 4 — Ignore Campers (ending4)
# Demonstrates: Mocking a full path to the ignore campers ending
# ============================================================

print("Running Ending Test 4 — Ignore Campers")

reset_state()

# Stub end_Credits so ending4 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
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
game.scripted_inputs = iter([
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
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback in case more input is requested than scripted
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run the main game function, which will eventually hit ending4
game.output = run_and_capture(game.main)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "continue" in game.output.lower(), "Ending 4 (ignore campers) text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 4 passed\n")

# ============================================================
# ENDING TEST 5 — Banditos Decline (ending5)
# Demonstrates: Calling ending5() from scene_banditos()
# ============================================================

print("Running Ending Test 5 — Banditos Decline")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Stub end_Credits so ending5 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_banditos() choice: "D5" (Decline)
# 2) Press Enter at credits
game.scripted_inputs = iter([
    "D5",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_banditos)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "stay trapped in dema forever" in game.output.lower(), "Ending 5 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 5 passed\n")

# ============================================================
# ENDING TEST 6 — Banditos Rejected (ending6)
# Demonstrates: Calling ending6() from scene_banditos()
# ============================================================

print("Running Ending Test 6 — Banditos Rejected")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force YBC to 0 so option D6 fails
game.YBC = 0

# Stub end_Credits so ending6 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_banditos() choice: "D6" (Put on jumpsuit, but no YBC)
# 2) Press Enter at credits
game.scripted_inputs = iter([
    "D6",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        # Safe fallback
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_banditos)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "you cannot pay" in game.output.lower(), "Ending 6 text missing."
assert "you remain in dema" in game.output.lower(), "Ending 6 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 6 passed\n")

# ============================================================
# ENDING TEST 7 — Recaptured at Camp (ending7)
# Demonstrates: Calling ending7() from scene_camp()
# ============================================================

print("Running Ending Test 7 — Recaptured at Camp")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Stub end_Credits so ending7 sets gameOn to a known value
game.real_end_Credits = end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_camp() choice: "E1" (Leave immediately)
# 2) Press Enter at credits
game.scripted_inputs = iter([
    "E1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_camp)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "re-captures you" in game.output.lower(), "Ending 7 text missing."
assert "stuck in dema forever" in game.output.lower(), "Ending 7 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 7 passed\n")

# ============================================================
# ENDING TEST 8 — Caught and Returned (ending8)
# Demonstrates: Calling ending8() from scene_finalbattle()
# ============================================================

print("Running Ending Test 8 — Caught and Returned")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Ensure Torchbearer capture state doesn't matter
game.capture_TB = False

# Stub end_Credits so ending8 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) scene_finalbattle() choice: "G1" (Run away)
# 2) Press Enter at credits
game.scripted_inputs = iter([
    "G1",
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_finalbattle)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "you are caught and returned to dema" in game.output.lower(), "Ending 8 text missing."
assert "you failed your mission" in game.output.lower(), "Ending 8 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 8 passed\n")

# ============================================================
# ENDING TEST 9 — Fight and Die (ending9)
# Demonstrates: Calling ending9() from scene_fightresult()
# ============================================================

print("Running Ending Test 9 — Fight and Die")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force BG to 4 to trigger ending9()
game.BG = 4

# Stub end_Credits so ending9 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Press Enter at credits
game.scripted_inputs = iter([
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_fightresult)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "you attempt to fight but die" in game.output.lower(), "Ending 9 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 9 passed\n")

# ============================================================
# ENDING TEST 10 — Spared by Villain (ending10)
# Demonstrates: Calling ending10() from scene_fightresult()
# ============================================================

print("Running Ending Test 10 — Spared by Villain")

reset_state()  # Ensure clean globals (inventory, YBC, gameOn, etc.)

# Force conditions to trigger ending10()
game.BG = 3
game.villain = "Nico"  # Ensure villain name exists for f-string

# Stub end_Credits so ending10 sets gameOn to a known value
game.real_end_Credits = game.end_Credits
def end_Credits():
    return False

# Ordered scripted inputs:
# 1) Press Enter at credits
game.scripted_inputs = iter([
    ""  # For the final 'Press Enter to exit.'
])

def fake_input(prompt=""):
    print(prompt, end="")
    try:
        return next(game.scripted_inputs)
    except StopIteration:
        return ""

# Patch input()
game.real_input = __builtins__.input
__builtins__.input = fake_input

# Run ONLY the scene being tested
game.output = run_and_capture(game.scene_fightresult)

# Restore input and end_Credits
__builtins__.input = game.real_input
game.end_Credits = game.real_end_Credits

# --- Assertions ---
assert "takes pity on you" in game.output.lower(), "Ending 10 text missing."
assert "lets you crawl away" in game.output.lower(), "Ending 10 text missing."
assert game.gameOn is False, "gameOn should be False after end_Credits stub."

print("✓ Ending Test 10 passed\n")

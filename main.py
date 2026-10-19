from pynput import keyboard
import re

typed_chars = []

def do_calculation(input_string):
    # Example calculation: count the number of characters typed
    char_count = len(input_string)
    print(f"Number of characters typed: {char_count}")

def on_press(key):
    #pattern = r"^-?\d+\.\d+$"
    #if re.match(pattern, key.char):
    #    typed_chars.append(key.char)

    try:
        typed_chars.append(key.char)
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.enter:
        print("\n--- Enter pressed, stopping ---")
        print(f"You typed: {''.join(typed_chars)}")
        return False  # Stop listener

def main():
    print("Ouptput:")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    #controller = keyboard.Controller()
    #        #controller.type("ls")
    #controller.press(keyboard.Key.backspace)
    #controller.release(keyboard.Key.enter)
            
    

if __name__ == "__main__":
    main()
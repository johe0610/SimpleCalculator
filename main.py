#import pynput
#
#def main():
#    print("Hello, World!")
#
#    # input
#    num1 = int(input())
#    num2 = int(input())
#
#    # printing the sum in integer
#    print(num1 + num2)
#
#if __name__ == "__main__":
#    main()

from pynput import keyboard

typed_chars = []

def on_press(key):
    try:
        #print(f"Key pressed: {key.char!r}")
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

if __name__ == "__main__":
    main()
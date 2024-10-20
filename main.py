import gdieffects

import threading
import time
import subprocess

contents = """
Lunaris by UniqueName12345

This virus is safe if you let it play out, however if you try to intervene... Things won't end up so well for you.
"""

with open("MEMZ.txt", "w") as file:
    file.write(contents)
notepad_process = subprocess.Popen(["notepad.exe", "MEMZ.txt"])
notepad_process.wait()

time.sleep(2)

def start_carousel():
    effects = [gdieffects.bouncing_balls, gdieffects.bitblt222]
    i = 0
    effect_thread = None
    while True:
        if effect_thread and effect_thread.is_alive():
            print("Waiting for current effect to finish")
            effect_thread.join(timeout=15)
            if effect_thread.is_alive():
                print("Effect taking too long, killing...")
                effect_thread._stop()
        else:
            print("Starting new effect")
            effect_thread = threading.Thread(target=effects[i % len(effects)])
            effect_thread.start()
            i += 1



threading.Thread(target=start_carousel).start()


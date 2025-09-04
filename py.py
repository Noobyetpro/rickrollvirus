import webview
import keyboard
from screeninfo import get_monitors

# Block keys globally
keyboard.block_key('alt')
keyboard.block_key('f4')
keyboard.block_key('windows')
keyboard.add_hotkey('ctrl+esc', lambda: None, suppress=True)
keyboard.add_hotkey('ctrl+esc+shift', lambda: None, suppress=True)
video_url = "https://shattereddisk.github.io/rickroll/rickroll.mp4"

# Create a window on each monitor
windows = []
for m in get_monitors():
    win = webview.create_window(
        "Fullscreen Video",
        video_url,
        x=m.x,
        y=m.y,
        width=m.width,
        height=m.height,
        fullscreen=True,
        confirm_close=False
    )
    windows.append(win)

webview.start()

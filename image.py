import pyautogui
from pynput import mouse
from pynput.mouse import Controller, Button

mouse_controller = Controller()

# -------------------------------
# Wait for a mouse click
# -------------------------------
def get_mouse_click_position():
    print("Click anywhere on the screen...")

    position = {"x": None, "y": None}

    def on_click(x, y, button, pressed):
        if pressed:
            position["x"] = x
            position["y"] = y
            print(f"Clicked at ({x}, {y})")
            return False  # Stop listener

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return position["x"], position["y"]

def click_at(x, y, button=Button.left):
    mouse_controller.position = (x, y)
    mouse_controller.click(button, 1)


# -------------------------------
# Take screenshot
# -------------------------------
def take_screenshot():
    return pyautogui.screenshot()


# -------------------------------
# Iterate pixels from click point
# -------------------------------
nice = []
n = 0
def iterate_from_point(image, start_x, start_y):
    global n
    width, height = image.size
    boundary = []
    filename = "pixels1.txt"
    pixels = image.load()
    prev_colour = 0;
    curr_colour = 0;
    with open(filename, "w") as f:
        for x in range(start_x , start_x + 1):
            for y in range(start_y, height):
                curr_colour = pixels[x, y];
                f.write(f"{pixels[x, y]}\n");
                # print(curr_colour)
                if(curr_colour == (0, 0, 0) and curr_colour != prev_colour):
                    boundary.append([x, y])
                prev_colour = curr_colour

    print(boundary)
    n = len(boundary) - 1
    block_s = (boundary[1][1] - boundary[0][1])
    print(block_s)
    d = {}
    count = 1;

    # print(block_s)

    for i in range(1, n + 1):
        y = boundary[i][1] - block_s / 2;
        for j in range(n):
            x = start_x + block_s * (95 * j) / 100;
            # print(f"{x}, {y}", end="\t");
            print(pixels[x, y], end = " ")
            click_at(x, y)
            if(not (pixels[x, y] in d)):
                d[pixels[x, y]] = count;
                count += 1
            nice.append(d[pixels[x, y]]);
        print()
    print()     

    
    for i in range(n):
        for j in range(n):
            print(nice[i * n + j], end=' ')
        print()
    print()
        



# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    x, y = get_mouse_click_position()
    img = take_screenshot()
    iterate_from_point(img, x, y)

def Main(OS):
    import tkinter as T
    import os
    from PIL import ImageTk, Image
    import json as J
    import random
    from functools import partial

    from WindowsClass import MovableFrame as MF

    ProgDir = "Apps"
    ProgFolder = "Chess"
    appDir = f"{ProgDir}\\{ProgFolder}"
    iconDir = f"{appDir}\\Pieces"
    square_size = 60  # Define the size of each square

    piece = random.choice(os.listdir(f"{iconDir}"))

    # Initialize the frame
    Frame = MF(OS, Image.open(f"{iconDir}\\{piece}"), [5000, 5000])
    table = Frame.frame
    board = T.Canvas(table,width=480,height=480)
    board.pack(pady=30)

    # Load the board from the JSON file
    with open(f"{appDir}\\defaultBoard.json", "r") as default_board_file:
        default_board = J.load(default_board_file)

    # Get the board data and split into rows
    board_data = default_board["Board"]
    rows = board_data.split(";")

    # Dictionary to store piece images
    piece_images = {}

    # Load all images into the dictionary
    for filename in os.listdir(iconDir):
        if filename.endswith('.png'):
            piece_name = os.path.splitext(filename)[0]  # Get the piece name without the extension
            image_path = os.path.join(iconDir, filename)
            image = Image.open(image_path)
            piece_images[piece_name] = ImageTk.PhotoImage(image)

    # Internal representation of the board
    board_state = [row.split(",") for row in rows]
    
    selected_piece = None
    selected_pos = None

    def toggle_button(button):
        current_color = button.cget("bg")
        new_color = "yellow" if current_color != "yellow" else button.original_color
        button.config(bg=new_color)

    def on_button_click(i, j):
        nonlocal selected_piece, selected_pos

        if selected_piece:
            # Move the piece
            move_piece(i, j)
            selected_piece = None
            selected_pos = None
        else:
            # Select the piece
            selected_piece = buttons[i][j]
            selected_pos = (i, j)
            selected_piece.config(bg="lightblue")  # Highlight selected piece

    def move_piece(i, j):

        old_i, old_j = selected_pos
        piece_name = board_state[old_i][old_j]
        board_state[i][j] = piece_name
        board_state[old_i][old_j] = "x"

        # Update the button images
        update_board()

    def update_board():
        # Clear existing buttons
        try:
            for button_row in buttons:
                for button in button_row:
                    del button
        except:
            pass

        # Create buttons and place pieces
        for i, row in enumerate(board_state):
            for j, piece in enumerate(row):
                color = "gray" if (i + j) % 2 == 0 else "olive"
                x1, y1 = j * square_size, i * square_size

                button = T.Button(board, bg=color, width=square_size, height=square_size)
                button.original_color = color
                button.config(command=partial(on_button_click, i, j))
                button.place(x=x1, y=y1, width=square_size, height=square_size)

                if piece != "x":
                    color_prefix = 'w' if piece.isupper() else 'b'
                    piece_image = piece_images.get(color_prefix + piece.upper())
                    if piece_image:
                        button.config(image=piece_image, compound="center")
                        button.image = piece_image

                buttons[i][j] = button

    buttons = [[None]*8 for _ in range(8)]
    update_board()
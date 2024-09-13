# PING PONG GAME

This is a simple Pong game built using Python's Pygame library. It is a two-player game where each player controls a racket to hit a ball. The game continues until one player misses the ball, and the opponent wins. The game includes background music and sound effects for a more engaging experience.

## Features

- Two-player game with Player 1 using `W` and `S` keys, and Player 2 using the `UP` and `DOWN` arrow keys.
- Background music and sound effects for ball hits.
- A game-over screen that shows the winner.
- Option to replay the game or exit.

## Installation

To run this game, you need to install the `pygame` library. You can do so by running:

```bash
pip install pygame
```

## How to Play

1. Run the `game.py` script in your Python environment.
2. The game will display a welcome screen.
3. Press the `W` key to start playing.
4. Player 1 (left racket) controls:
   - `W` to move up.
   - `S` to move down.
5. Player 2 (right racket) controls:
   - `UP` arrow to move up.
   - `DOWN` arrow to move down.
6. The ball will bounce off the rackets and walls. The game ends when one player misses the ball, and the opponent wins.
7. On the game-over screen:
   - Press `W` to play again.
   - Press `ESC` to exit the game.

## Controls

- **Player 1 (left racket)**:
  - `W` - Move up
  - `S` - Move down

- **Player 2 (right racket)**:
  - `UP Arrow` - Move up
  - `DOWN Arrow` - Move down

## Files Required

Ensure you have the following assets in the `assets` directory:

1. `bg.mp3` - Background music for the game.
2. `bullet.mp3` - Sound effect for when the ball hits the racket.
3. `rakcet.png` - Image file for the racket.
4. `ball.png` - Image file for the ball.
5. `smallfont.ttf` - Font file for small text (e.g., game instructions).
6. `bigfont.ttf` - Font file for large text (e.g., game title and winner announcement).
7. `icon.png` - Icon image for the game window.

## License

This project is open-source and available for personal use.
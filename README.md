# Pygame Space Shooter Game

A 2D space shooter game built with Pygame where players battle against enemies while collecting power-ups and managing helper units.

## Project Structure

```
├── assets/
│   ├── images/
│   │   └── background.png
│   └── sounds/
└── src/
    ├── __init__.py
    ├── bullet.py
    ├── cube.py
    ├── enemy_bullet.py
    ├── enemy.py
    ├── entity.py
    ├── game.py
    ├── gift.py
    ├── helper.py
    ├── player.py
    └── utils.py
```

## Features

- Player-controlled character with directional movement and shooting
- Enemy AI that tracks and shoots at the player
- Power-up system with collectible gifts
- Helper units that protect the player by intercepting enemy bullets
- Dynamic difficulty scaling with increasing enemy spawn rates
- Health system for both player and enemies
- Collision detection system
- Background graphics support

## Controls

- **Arrow Keys**: Move the player
- **W**: Shoot upward
- **S**: Shoot downward
- **A**: Shoot left
- **D**: Shoot right

## Game Mechanics

### Player
- Controlled using arrow keys for movement
- Can shoot in four directions
- Has a health system
- Cannot move beyond screen boundaries

### Enemies
- Automatically track the player
- Shoot projectiles at the player
- Spawn rate increases over time
- Have individual health systems

### Helper Units
- Spawn when collecting gifts
- Automatically intercept enemy bullets
- Can absorb up to 10 bullets before being destroyed
- Move independently to protect the player

### Gift System
- Gifts spawn periodically
- Collecting gifts spawns helper units
- Adds strategic gameplay elements

## Dependencies

- Python 3.x
- Pygame
- OpenGL (for cube.py visualization)

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install pygame PyOpenGL
```
3. Run the game:
```bash
python src/game.py
```

## Technical Details

The game is built using an entity-component system with the following key classes:

- `Entity`: Base class for game objects
- `Player`: Handles player movement and shooting
- `Enemy`: Manages enemy AI and behavior
- `Helper`: Controls helper unit behavior
- `Gift`: Manages power-up spawning and collection
- `Game`: Main game loop and state management

## Development

The project uses modular design principles for easy expansion:

- All game entities inherit from the base `Entity` class
- Separate bullet classes for player and enemy projectiles
- Centralized game state management in the `Game` class
- Event-driven gift collection system
- Configurable parameters for game balance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

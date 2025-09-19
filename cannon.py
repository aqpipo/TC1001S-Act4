"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Lanza la bala si está fuera de pantalla."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Más velocidad al proyectil (ajustable)
        speed.x = (x + 150) / 10
        speed.y = (y + 150) / 10

def inside(xy):
    """True si xy está dentro de la ventana."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Dibuja bala y targets."""
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Mueve bala y targets (juego infinito)."""
    # Spawnea targets cada cierto tiempo
    if randrange(40) == 0:
        targets.append(vector(200, randrange(-150, 150)))

    # Avance de targets (puedes subir a -2 o -3 para más velocidad)
    for target in targets:
        target.x -= 1

        # Re-posiciona target al salir de pantalla (wrap a la derecha)
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)

    # Física de la bala
    if inside(ball):
        speed.y -= 1      # gravedad
        ball.move(speed)
    else:
        # Si salió, déjala lista para el siguiente tap
        ball.x, ball.y = -200, -200
        speed.x = speed.y = 0

    # Colisiones: elimina target si la bala lo golpea
    dupe = targets.copy()
    targets.clear()
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 50)

# Inicialización
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

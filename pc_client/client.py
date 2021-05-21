import pygame
from network_interface import Network
from moving_object import MovingObject
from player import Player
from ball import Ball
from game import Game
import json
import traceback

pygame.font.init()

WIDTH, HEIGHT = 858, 525
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")


def redrawWindow(connected, mover_list):
    if not connected:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for player 2...", 1, (255, 0, 0))
        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    else:
        WIN.fill((0, 0, 0))
        for mover in mover_list:
            mover.draw(WIN)
        pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = n.get_player()
    id = player.get_id()
    opponent = None
    ball = None
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        recieved_game = False
        while not recieved_game:
            try:
                json_game = n.send_then_receive(player)
                connected_json = json_game["connected"]
                if connected_json == "true":
                    connected = True
                else:
                    connected = False
                print("connected ", connected)
                game = Game(json_game["gameID"], json_game["players"], json_game["ball"], json_game["points"])
                if game != None:
                    recieved_game = True
            except Exception as e:
                print(e)
                traceback.print_exc()
                run = False
                print("didn't get game")

        player_json = game.getPlayer(id)
        opponent_json = game.getPlayer((id+1)%2)
        ball_json = game.getBall()

        if isinstance(opponent, Player):
            player.setX(opponent_json["x"])
            player.setY(opponent_json["y"])
        else:
            opponent = Player(opponent_json["x"], opponent_json["y"], opponent_json["width"], opponent_json["height"], (id+1)%2)

        if isinstance(ball, Ball):
            player.setX(ball_json["x"])
            player.setY(ball_json["y"])
        else:
            ball = Ball(ball_json["x"], ball_json["y"], ball_json["width"], ball_json["height"])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.moveY(-3)
        if keys[pygame.K_DOWN]:
            player.moveY(3)
        print(player_json, opponent_json, ball_json)
        movers = [player, opponent, ball]
        redrawWindow(connected, movers)


def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        WIN.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("CLick to play", 1, (255, 0, 0))
        WIN.blit(text, (100, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    main()


while True:
    menu_screen()

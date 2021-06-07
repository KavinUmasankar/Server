# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:57:21 2021

@author: kavin
"""
import pygame
import socket

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientId = 0

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.96"
        self.port = 5353
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

def redrawWindow(win, thing):
    window.fill((255, 255, 255))
    thing.draw(win)
    pygame.display.update()
 
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 0.05
        
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)
            
def main():
    
    running = True
    player = Player(50, 50, 25, 25, (0, 255, 0))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        player.move()
        redrawWindow(window, player)
        

            
main()
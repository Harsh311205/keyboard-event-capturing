import pygame
import csv
import time

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Virtual Joystick Simulation")

filename = "virtual_joystick_events.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Event Type", "Details"]) 

print("Press arrow keys as joystick simulation, SPACE as button, ESC to exit...")

running = True
while running:
    for event in pygame.event.get():
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        details = ""
        event_type = ""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                event_type = "Axis Motion"
                details = "UP (Axis Y -1)"
            elif event.key == pygame.K_DOWN:
                event_type = "Axis Motion"
                details = "DOWN (Axis Y +1)"
            elif event.key == pygame.K_LEFT:
                event_type = "Axis Motion"
                details = "LEFT (Axis X -1)"
            elif event.key == pygame.K_RIGHT:
                event_type = "Axis Motion"
                details = "RIGHT (Axis X +1)"
            elif event.key == pygame.K_SPACE:
                event_type = "Button Press"
                details = "Simulated Button A"
            elif event.key == pygame.K_ESCAPE:
                running = False

        if event_type:
            print(f"[{timestamp}] {event_type}: {details}")
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, event_type, details])

pygame.quit()
print(f"Events saved in {filename}")
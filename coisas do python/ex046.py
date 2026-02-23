from time import sleep
import emoji

for t in range(10, -1, -1):
    print(t)
    sleep(1)
print(emoji.emojize(":fireworks: :partying_face: :party_popper: :confetti_ball:"))

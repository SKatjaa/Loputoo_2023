import pygame
import sys
import random

pygame.init()

ekraani_laius = 800
ekraani_kõrgus = 600
võrgu_suurus = 40

VALGE = (255, 255, 255)
MUST = (0, 0, 0)
ROHELINE = (90, 219, 85)
PUNANE = (213, 56, 56)
SININE = (102, 204, 255)

ekraan = pygame.display.set_mode((ekraani_laius, ekraani_kõrgus))
pygame.display.set_caption("Boeingi lennutee visualiseerimine")

lennuki_pilt = pygame.image.load("airplane-icon.png")
lennuki_pilt = pygame.transform.scale(lennuki_pilt, (50, 50)) 
lennuki_kolmnurk = lennuki_pilt.get_rect()

mäe_pilt = pygame.image.load("mountain.png")
mäe_pilt = pygame.transform.scale(mäe_pilt, (70, 30))

lennujaam_pilt = pygame.image.load("airport.png")
lennujaam_pilt = pygame.transform.scale(lennujaam_pilt, (35, 50))

tee_punktid = []

takistuste_arv = 6
takistused = [pygame.Rect(random.randint(0, ekraani_laius - 50), random.randint(0, ekraani_kõrgus - 50), 50, 50) for _ in range(takistuste_arv)]
lennujaamade_arv = 4
lennujaamad = [(random.randint(50, ekraani_laius - 50), random.randint(50, ekraani_kõrgus - 50)) for _ in range(lennujaamade_arv)]

def joonista_võrk():
    for x in range(0, ekraani_laius, võrgu_suurus):
        pygame.draw.line(ekraan, MUST, (x, 0), (x, ekraani_kõrgus))
    for y in range(0, ekraani_kõrgus, võrgu_suurus):
        pygame.draw.line(ekraan, MUST, (0, y), (ekraani_laius, y))

def joonista_tee(punktid):
    for i in range(len(punktid) - 1):
        pygame.draw.line(ekraan, ROHELINE, punktid[i], punktid[i+1], 3)

def joonista_lennuk(seisukoht):
    lennuki_kolmnurk.center = seisukoht
    ekraan.blit(lennuki_pilt, lennuki_kolmnurk)

def joonista_punkt(seisukoht, värv):
    pygame.draw.circle(ekraan, värv, seisukoht, 10)

def joonista_takistused(takistused):
    for obstacle in takistused:
        ekraan.blit(mäe_pilt, (obstacle.x, obstacle.y))

def joonista_lennujaamad(lennujaamad):
    for airport in lennujaamad:
        ekraan.blit(lennujaam_pilt, (airport[0] - 25, airport[1] - 25))

clock = pygame.time.Clock()
edenemine = 0
praegune_segment = 0
while True:
    ekraan.fill(VALGE)
    joonista_võrk()
    joonista_takistused(takistused)
    joonista_lennujaamad(lennujaamad)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tee_punktid.append(pygame.mouse.get_pos())

    for punkt in tee_punktid:
        joonista_punkt(punkt, PUNANE)

    if len(tee_punktid) >= 2:
        joonista_tee(tee_punktid)
        edenemine += 0.01
        if edenemine > 1:
            edenemine = 0
            praegune_segment += 1
            if praegune_segment >= len(tee_punktid) - 1:
                praegune_segment = 0

        algus_punkt = tee_punktid[praegune_segment]
        lõpp_punkt = tee_punktid[praegune_segment + 1]
        lennuk_koht = (int(algus_punkt[0] + edenemine * (lõpp_punkt[0] - algus_punkt[0])),
                        int(algus_punkt[1] + edenemine * (lõpp_punkt[1] - algus_punkt[1])))
        joonista_lennuk(lennuk_koht)

    pygame.display.flip()
    clock.tick(30)
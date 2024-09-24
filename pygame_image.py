import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgr_img= pg.transform.flip(bg_img, True, False)
    tmr = 0
    kk_img = pg.image.load("fig/3.png")#練習２
    kkr_img = pg.transform.flip(kk_img, True, False)#練習２
    kkr_rct = kkr_img.get_rect()
    kkr_rct.center = 300,200

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kkr_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kkr_rct.move_ip((0,1))
        if key_lst[pg.K_LEFT]:
            kkr_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kkr_rct.move_ip((2,0))
        kkr_rct.move_ip((-1,0))
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bgr_img,[x+1600,0])
        screen.blit(bg_img, [x+3200,0])
        screen.blit(bgr_img,[x+4800,0])#練習5
        #screen.blit(kkr_img,[300,200])#練習４
        screen.blit(kkr_img,kkr_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
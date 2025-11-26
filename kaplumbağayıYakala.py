import turtle
from random import randint

# değişkenler
skor_sayisi = 0
kalan_zaman = 20

# --- Ekran Ayarları ---

ekran = turtle.Screen()
ekran.bgcolor("light blue")
ekran.title("Kaplumbağayı Yakala")
ekran.setup(width=800,height=800)
ekran.getcanvas().winfo_toplevel().resizable(width=False,height=False)
ekran.register_shape("kaplumbaga.gif") # kaplumbağa nesnesini shape için atadık
ekran.listen()

def otomatik_kacis():
    k.clear()
    k.speed(1000)
    k.goto(randint(a=-200, b=200), randint(a=-200, b=200))

def skor_guncelle(x,y):
    try:
        global kalan_zaman
        if kalan_zaman == 0:
            return
        global skor_sayisi
        skor_sayisi += 1
        skor.clear()
        skor.write(arg=f"Score : {skor_sayisi}",move=False, font=("Arial",20,"normal"))
    except:
        ekran.clear()
        a=turtle.Turtle()
        a.hideturtle()
        a.penup()
        a.home()
        a.write(arg="Tanımlanamayan Hata",font=("Arial",50,"normal"))

def sayac():
    try:
        global kalan_zaman
        if kalan_zaman <= 0:
            game_over.clear()
            game_over.home()
            return game_over.write("Oyun Bitti",font=("Arial",50,"normal"))
        else:
            kalan_zaman -= 1
            ekran.ontimer(sayac,1000)
            otomatik_kacis()
            s.clear()
            s.write(arg=f"Time : {kalan_zaman}", move=False, font=("Arial", 20, "normal"))

    except:
        pass

# --- Nesneler ---

# kaplumbağa nesnesi
k = turtle.Turtle()
k.shape("kaplumbaga.gif")
k.penup()
k.goto(randint(a=-200,b=200),randint(a=-200,b=200))
k.speed(0)

# skor
skor = turtle.Turtle()
skor.penup()
skor.hideturtle()
skor.color("dark blue")
skor.goto(x=0,y=350)
skor.write(arg=f"Score : {skor_sayisi}",move=False, font=("Arial",20,"normal"))

# Sayaç
s = turtle.Turtle()
s.penup()
s.hideturtle()
s.goto(x=0,y=310)
s.write(arg=f"Time : {kalan_zaman}", move=False, font=("Arial",20,"normal"))

# game over
game_over = turtle.Turtle()
game_over.home()
game_over.penup()
game_over.hideturtle()
game_over.speed(0)


#oyun akışı

k.onclick(skor_guncelle)
sayac()


# oyun ekranı kapanmasın
turtle.mainloop()

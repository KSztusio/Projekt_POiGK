from vpython import *
L1 = 6
L2 = 6
L3 = 5.31
light_orange=vec(1,0.85,0.7)    
class segment:
    axis = vec(1,0,0)
    def __init__(self, seg):
        self.seg = seg
        self.axis = self.seg.axis
        self.pos = self.seg.pos
    def stablilise(self):
        self.angle = 0
        self.up_vector_teo = vec(self.up[0], self.up[2], self.up[1])
        if diff_angle(self.seg.up, self.up_vector_teo) != 0:
            self.angle = -diff_angle(self.seg.up, self.up_vector_teo)
            if diff_angle(cross(self.seg.up, self.up_vector_teo),self.axis) < 0.01:
                self.angle = -self.angle
            self.seg.rotate(axis = self.seg.axis, angle = self.angle) 
    def calc_up(self, ro1, ro2, ro3):
        self.up = [0,0,1]
        self.up = rotationy(ro3, self.up[0], self.up[1], self.up[2])
        self.up = rotationy(ro2, self.up[0], self.up[1], self.up[2])
        self.up = rotationz(ro1, self.up[0], self.up[1], self.up[2])
    def rot(self, ro1, ro2, ro3, s = 0):
        self.axisx = [1,0,0]
        self.axisx = rotationy(ro3, self.axisx[0], self.axisx[1], self.axisx[2])
        self.axisx = rotationy(ro2, self.axisx[0], self.axisx[1], self.axisx[2])
        self.axisx = rotationz(ro1, self.axisx[0], self.axisx[1], self.axisx[2])
        self.axis = vec(self.axisx[0], self.axisx[2], self.axisx[1])
        self.seg.axis=self.axis
        if s:
            self.calc_up(ro1, ro2, ro3)
            self.stablilise()
    def update_pos(self, pos, ax, L):
        self.pos=pos + norm(ax)*L
        self.seg.pos = self.pos
scene = canvas( width=960, height=580, center=vector(0,5,0), background=color.white)
#instrukcja
instruction_box = wtext(text="Instrukcje:\n"
                             "W,A,S,D: rysowanie\n"
                             "Q/E: przysuwanie od/oddalanie od tablicy\n"
                             "Strzałki + K,L: przesuwanie kamery\n"
                             "BACKSPACE: czyszczenie tablicy\n")

#kamera
distant_light(direction=vec(-1, 0, 0), color=color.white*(0.5))
scene.camera.pos = vector(-10, 5, -10)
def kamerka(event):  # info about event is stored in evt 
    global kamera
    aa=0
    bb=0
    cc=0
    strzalka = event.key
    if strzalka == 'up':
        bb+=0.1
    elif strzalka =='down':
        bb-=0.1
    elif strzalka =='left':
        aa-=0.1
    elif strzalka =='right':
        aa+=0.1
    elif strzalka == 'k':
        cc-=0.1
    elif strzalka == 'l':
        cc+=0.1
    kamera=vec(aa,bb,cc)
    scene.camera.pos+=kamera
scene.bind('keydown', kamerka)
scene.camera.axis = vector(12, 0, 10)
#tablica i podloga
brown = vector(0.59, 0.29, 0.0)
tabb = box(pos=vector(0, 0, 0), size=vector(0.1, 12, 20), color=color.white, shininess=0.9)
ramka_lewa = box(pos=vector(0, 0, 10), size=vector(0.1, 12, 0.1), color=color.black)
ramka_prawa = box(pos=vector(0, 0, -10), size=vector(0.1, 12, 0.1), color=color.black)
ramka_gora = box(pos=vector(0, 6, 0), size=vector(0.1, 0.1, 20), color=color.black)
ramka_dol = box(pos=vector(0, -6, 0), size=vector(0.1, 0.1, 20), color=color.black)
podloga = box(pos=vector(0, -0.1, 0), size=vector(20, 0.2, 20), color=brown)
tablica=compound([ramka_dol, ramka_gora, ramka_lewa, ramka_prawa, tabb])
tablica.pos=vec(8.05,6.2,0)
#segment 1
podstawka=cylinder(pos=vector(0,0,0), axis=vec(0,0.2,0), radius=0.6, color=color.gray(0.7))
rura=cylinder(pos=vector(0,0,0), axis=vec(0,6,0), radius=0.5, color=color.gray(0.7))
os1 = cylinder(pos=vec(0,6,0.5), axis=vec(0,0,-1), radius=0.5, color=color.gray(0.7))
segment1=compound([podstawka, rura, os1], origin=vec(0,0,0))
segment1.pos=vec(0,0,0)

#segment 2
g = shapes.circle(radius = 0.3, angle1=pi*1.5, angle2=pi/2)
mpath = [vector(0,0,0.4),vector(0,0,0.8)]
e = extrusion(shape=g, path=mpath, color=color.gray(0.7))
e.pos=vec(6,0,0)

h = shapes.circle(radius = 1, angle1=0.5*pi, angle2=pi*1.5)
f = extrusion(shape=h, path=mpath, color=color.gray(0.7))
f.rotate(axis=vec(0,0,1), angle=pi, origin=vec(0,0,0))

box1=box(pos=vec(6-5.5/2,0,0.6), size=vec(5.5,0.6,0.4), color=color.gray(0.7))

box2=box(pos=vec(0.25,0,0.6), size=vec(0.5,2,0.4), color=color.gray(0.7))
    
trojkat1=[[-0.5,0.3],[-0.5,1],[-6,0.3],[-0.5,0.3]]
troj1 = extrusion(shape=trojkat1, path=mpath, color=color.gray(0.7))

trojkat2=[[-0.5,-0.3],[-0.5,-1],[-6,-0.3],[-0.5,-0.3]]
troj2 = extrusion(shape=trojkat2, path=mpath, color=color.gray(0.7))

segment2=compound([troj1,troj2,box1,box2,e,f],origin=vec(0,0,0))
segment2.pos=segment1.pos+vec(0,L1,0)

#segment 3
mpath=[vector(0,0,-0.2),vector(0,0,0.2)]
g2 = shapes.circle(radius = 0.3*0.7, angle1=pi*1.5, angle2=pi/2)
e2 = extrusion(shape=g2, path=mpath, color=color.gray(0.7))
e2.pos=vec(6*0.7,0,0)

box3=box(pos=vec((6-5.5/2)*0.7,0,0), size=vec((5.5)*0.7,0.6*0.7,0.4), color=color.gray(0.7))
box4=box(pos=vec(0.25*0.7,0,0), size=vec(0.5*0.7,2*0.7,0.4), color=color.gray(0.7))

trojkat3=[[-0.5*0.7,0.3*0.7],[-0.5*0.7,1*0.7],[-6*0.7,0.3*0.7],[-0.5*0.7,0.3*0.7]]
troj3 = extrusion(shape=trojkat3, path=mpath, color=color.gray(0.7))

trojkat4=[[-0.5*0.7,-0.3*0.7],[-0.5*0.7,-1*0.7],[-6*0.7,-0.3*0.7],[-0.5*0.7,-0.3*0.7]]
troj4 = extrusion(shape=trojkat4, path=mpath, color=color.gray(0.7))

h2 = shapes.circle(radius = 0.7, angle1=0.5*pi, angle2=pi*1.5)
f2 = extrusion(shape=h2, path=mpath, color=color.gray(0.7))
f2.rotate(axis=vec(0,0,1), angle=pi, origin=vec(0,0,0))

koniec=cone(pos=vec(0.7,0,0), axis=vec(0.2,0,0), radius=0.07, color=vec(255,255,255))
pis=cylinder(pos=vec(0,0,0), axis=vec(0.7,0,0), radius=0.07, color=vec(255,255,255) )
pisak=compound([koniec, pis])
pisak.pos=vec(6.3*0.7,0,0)
os = cylinder(pos=vec(0,0,0.2), axis=vec(0,0,0.3), radius=0.2, color=color.gray(0.7))
segment3=compound([troj3,troj4,box3,box4,e2,f2,os], origin=vec(0,0,0))
segment3.pos = segment2.pos+vec(L2,0,0)
seg1 = segment(segment1)
seg2 = segment(segment2)
seg3 = segment(segment3)
seg_pisak = segment(pisak)
def rotationz(alpha, x, y, z):
    H = [[cos(alpha),-sin(alpha), 0],
        [sin(alpha), cos(alpha), 0],
        [0,0,1]]
    xn = H[0][0]*x+H[0][1]*y+H[0][2]*z
    yn = H[1][0]*x+H[1][1]*y+H[1][2]*z
    zn = H[2][0]*x+H[2][1]*y+H[2][2]*z
    return [xn, yn, zn]

def rotationy(alpha, x, y, z):
    H = [[cos(alpha), 0,sin(alpha)],
        [0,1,0],
        [-sin(alpha), 0, cos(alpha)]]
    xn = H[0][0]*x+H[0][1]*y+H[0][2]*z
    yn = H[1][0]*x+H[1][1]*y+H[1][2]*z
    zn = H[2][0]*x+H[2][1]*y+H[2][2]*z
    return [xn, yn, zn]
def reverse_kinematic(x,y,z):
    P2 = z - L1
    Ro1 = atan2(y, x)   
    P1 = x * cos(Ro1) + y * sin(Ro1)
    P3 = pow((2 * P1 * L2), 2) + pow((2 * P2 * L2), 2) - pow(pow(P1, 2) + pow(P2, 2) + pow(L2, 2) - pow(L3, 2), 2)
    Ro2 = atan2(2 * P2 * L2 * (pow(P1, 2) + pow(P2, 2) + pow(L2, 2) - pow(L3, 2)) + 2 * P1 * L2 * sqrt(P3), 2 * P1 * L2 * (pow(P1, 2) + pow(P2, 2) + pow(L2, 2) - pow(L3, 2)) - 2 * P2 * L2 * sqrt(P3))
    Ro3 = -Ro2 + atan2(P2 - L2 * sin(Ro2), P1 - L2 * cos(Ro2))
    return [Ro1, Ro2, Ro3]
x = 6
y = 0
z = 5
kolor = color.red
def changecolor(evt): 
    global kolor  
    if evt.index < 1:
        pass
    elif evt.index == 1:
        kolor=color.yellow
    elif evt.index == 2:
        kolor=color.green
    elif evt.index == 3:
        kolor=color.blue
    elif evt.index == 4:
        kolor=color.red
    elif evt.index == 5:
        kolor=color.black
l=[]
point1 = []
file = open('t.txt', 'w')
file.close()
choicelist = ['Color', 'yellow', 'green', 'blue', 'red', 'black']
menu(choices=choicelist, bind=changecolor )
def key_pressed(evt):  # info about event is stored in evt
    global x, y, z, l, point1
    if file.closed:
        keyname = evt.key
        if keyname == 'w':
            if pos[2] < 11:
                pos[2]+=0.01
        elif keyname =='s':
            if pos[2] > 1:
                pos[2]-=0.01
        elif keyname =='a':
            if pos[1] > -6:
                pos[1]-=0.01
        elif keyname =='d':
            if pos[1] < 6:
                pos[1]+=0.01
        elif keyname == 'e':
            pos[0] = 8
        elif keyname == 'q':
            pos[0] = 7
        elif keyname == 'backspace':
            for ball in l:
                ball.visible=False
                del ball
            l = []
            point1 = []
def rys_dom():
    global file
    file = open('domek.txt', 'r')
    domek.background = color.orange
    buzka.background = light_orange
    anakin.background = light_orange
    drzewo.background = light_orange
def rys_buz():
    global file
    file = open('smile.txt', 'r')
    domek.background = light_orange
    buzka.background = color.orange
    anakin.background = light_orange
    drzewo.background = light_orange
def rys_anakin():
    global file
    file = open('anakin.txt', 'r')
    domek.background = light_orange
    buzka.background = light_orange
    anakin.background = color.orange
    drzewo.background = light_orange
def rys_drzewo():
    global file
    file = open('tree.txt', 'r')
    domek.background = light_orange
    buzka.background = light_orange
    anakin.background = light_orange
    drzewo.background = color.orange
domek = button( bind=rys_dom, text='rysuj domek', color=color.black, background=light_orange, selected = 0)
buzka = button( bind=rys_buz, text='rysuj buźkę', color=color.black, background=light_orange, selected = 0)
anakin = button( bind=rys_anakin, text='rysuj anakina', color=color.black, background=light_orange, selected = 0)
drzewo = button( bind=rys_drzewo, text='rysuj drzewo', color=color.black, background=light_orange, selected = 0)
def gotopoint(x, y, z, nx, ny, nz):
    vector_point=vec(nx - x, ny - y, nz - z)
    vector_point = norm(vector_point)
    x +=vector_point.x*0.01
    y +=vector_point.y*0.01
    z +=vector_point.z*0.01
    return [x, y, z]
scene.bind('keydown', key_pressed)
g = 0
newpos = [x,y,z]
pos = [x,y,z]
while True:
    rate(60)
    if not file.closed:
        if g == 0:
            g = 1
            point = file.readline()
            if point == '':
                file.close()
                domek.background = light_orange
                buzka.background = light_orange
                anakin.background = light_orange
                drzewo.background = light_orange
            else:
                point = point.replace('\n', '')
                pos = point.split(' ')
                pos[0] = float(pos[0])
                pos[1] = float(pos[1])
                pos[2] = float(pos[2])
                pos[0] = 8-pos[0]
        if abs(newpos[0]-pos[0]) < 0.01 and abs(newpos[1]-pos[1]) < 0.01 and abs(newpos[2]-pos[2]) < 0.01:
            g = 0
    newpos = gotopoint(newpos[0], newpos[1], newpos[2], pos[0], pos[1], pos[2])
    Ro = reverse_kinematic(newpos[0],newpos[1],newpos[2])
    seg1.rot(Ro[0], 0, 0)
    seg2.rot(Ro[0], -Ro[1], 0, 1)
    seg3.update_pos(seg2.pos, seg2.axis, L2)
    seg3.rot(Ro[0], -Ro[1], -Ro[2], 1)
    seg_pisak.rot(Ro[0], -Ro[1], -Ro[2])
    seg_pisak.update_pos(seg3.pos, seg3.axis, L3-0.9)
    seg_pisak.seg.color = kolor
    v = pisak.pos+norm(pisak.axis)*0.9
    if v.x > 7.99:
        t = 1
        for f in point1:
            if mag(f[0]-v) <0.01 and f[1] == kolor:
                t=0
        if t:
            l.append(sphere(pos=v, radius=0.03, color = kolor))
            point1.append([v, kolor])
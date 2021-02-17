from tkinter import Tk, Canvas


def draw_tiles(row, col, grout, wdth, lngth):
    app = Tk()
    app.title("!!! THE FIRST TILE OUTPUT DRAW EVER !!!")
    r_x, c_x = row, col
    start_x, start_y = 50, 50
    end_x, end_y = 100, 100
    grout = end_x - start_x + grout
    canv = Canvas(app, width=wdth, height=lngth, bg="gray")
    for r in range(r_x):
        for c in range(c_x):
            canv.create_rectangle(start_x, start_y, end_x, end_y, fill="#285078", outline="black")
            start_x += grout
            end_x += grout
        start_y += grout
        end_y += grout
        start_x -= (grout * col)
        end_x -= (grout * col)
    canv.pack()
    app.mainloop()


tile_w = 150
tile_h = 200
inp_wdth = 2150
inp_lngth = 1800
grout = 3
row = int(inp_wdth / tile_w)
col = int(inp_lngth / tile_w)
wdth = inp_wdth / 3 + 100
lngth = inp_lngth / 2 + 100

draw_tiles(row, col, grout, wdth, lngth)

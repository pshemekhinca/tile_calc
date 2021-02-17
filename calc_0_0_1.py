class TileCalculator:
    """Sets initial tile and grout parameters"""
    def __init__(self, tile_width, tile_length, grout):
        self.tile_length = tile_length
        self.tile_width = tile_width
        self.grout = grout

    def single_tile_area(self):
        tile_area = self.tile_length * self.tile_width / 100
        return round(tile_area, 2)


class RectangleSurface:
    """Rectangular surface partition by tile size + grout"""
    def __init__(self, room_width, room_length):
        self.room_width = room_width
        self.room_length = room_length
        self.grout = 3
        self.tile_width = 180
        #TODO: make inheritance after TileCalculator --> grout and tile_width should come from parent class

    def single_surface_area(self):
        surface_area = self.room_length * self.room_width / 1000_000
        return round(surface_area, 2)

    def centered_tiles(self) -> str:
        sides_cuts = str((room_length % self.tile_width) / 2)
        whole_tiles = str(tile_size).split() * int(room_length / tile_size)
        grout_out = f' |{self.grout}| '
        return f'{grout_out.join([sides_cuts, *whole_tiles, sides_cuts])}'

    def side_aligned_tiles(self):
        pass


if __name__ == '__main__':

    # tile_size = int(input("Set the tile width: "))
    # room_length = int(input("Give room length: "))
    # grout = input("Give grout width: ")

    room_length = 2500
    tile_size = 180
    grout = '3'

    #TODO: out of below make method <side_aligned_tiles> of RectangleSurface class

    # section = 180
    # length_to_divide: int = 2150
    # interject = "  3  "
    #
    # cut_side = str((room_length % tile_size) / 2)
    # tiles_ncut = int(room_length / tile_size)
    # whole = str(tile_size).split() * int(room_length / tile_size)
    # grout_sum = (interject * (tiles_ncut + 1))
    # print(f"Suma fug {len(grout_sum) * interject}")
    # result = interject.join([cut_side, *whole, cut_side])
    # print(result)
    # if float(cut_side) > (float(tile_size) / 2):
    #     print(f"Ilość płytek w rzędzie {whole + 2}")
    # else:
    #     print(f"Ilość płytek w rzędzie {whole + 1}")

    sample_tile = TileCalculator(180, 220, 3)
    print(sample_tile.single_tile_area())

    sample_rect_room = RectangleSurface(2500, 2100)
    print(sample_rect_room.single_surface_area())
    print(sample_rect_room.centered_tiles())


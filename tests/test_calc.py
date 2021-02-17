import pytest
from calc_0_0_1 import TileCalculator, RectangleSurface

@pytest.mark.parametrize('width, length, expected', [
    (180, 220, 396),
    (300, 300, 900),
    (245, 305, 747.25)
])
def test_single_tile_area(width, length, expected):
    """ Results in sq centimeters"""
    sample_tile = TileCalculator(width, length, 3)
    assert sample_tile.single_tile_area() == expected


@pytest.mark.parametrize('width, length, expected', [
    (2500, 2100, 5.25),
    (2450, 1350, 3.31),
    (3200, 2150, 6.88)
])
def test_single_surface_area_in_rectangle_room(width, length, expected):
    """ Results in sq meters"""
    sample_rect_room = RectangleSurface(width, length)
    assert sample_rect_room.single_surface_area() == expected


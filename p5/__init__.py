#
# Part of p5: A Python package based on Processing
# Copyright (C) 2017-2019 Abhik Pal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from .core.attribs import background, clear, fill, no_fill, no_tint, tint, no_stroke, \
    stroke, stroke_weight, stroke_cap, stroke_join
from .core.color import color_mode, Color
from .core.font import create_font, load_font, text, text_font, text_size, text_width, \
    text_leading, text_align, text_ascent, text_descent
from .core.image import PImage, load_pixels, image, load_image, image_mode
from .core.light import lights, light_specular, light_falloff, point_light, \
    directional_light, ambient_light
from .core.material import normal_material, diffuse, specular, basic_material, \
    blinn_phong_material, ambient, emissive, shininess
from .core.primitives import point, Arc, rect, rect_mode, bezier, curve, create_shape, \
    draw_shape, ellipse_mode, quad, square, circle, ellipse, triangle, line, arc
from .core.shape import PShape
from .core.transforms import push_matrix, reset_transforms, rotate, translate, rotate_z, \
    camera, print_matrix, reset_matrix, apply_matrix, perspective, shear_y, rotate_y, \
    rotate_x, shear_x, scale, frustum, ortho
from .core.vertex import begin_shape, curve_vertex, bezier_vertex, quadratic_vertex, \
    vertex, end_contour, begin_contour, end_shape
from .pmath.curves import bezier_point, bezier_tangent, bezier_detail, curve_point, \
    curve_tangent, curve_detail, curve_tightness, quadratic_point
from .pmath.rand import noise, noise_detail, noise_seed, random_uniform, \
    random_gaussian, random_seed
from .pmath.utils import TWO_PI, PI, HALF_PI, QUARTER_PI, TAU, HALF_TAU, constrain, \
    lerp, remap, normalize, distance, dist, magnitude, mag, sq
from .pmath.vector import Vector, Point
from .sketch.userspace import no_loop, loop, redraw, size, title, no_cursor, cursor, \
    exit, draw, setup, run, save_frame, save


__all__ = [
    'background', 'clear', 'fill', 'no_fill',
    'stroke', 'no_stroke', 'tint', 'no_tint',
    'stroke_weight', 'stroke_cap', 'stroke_join',
    'color_mode', 'Color'
                  'create_font', 'load_font', 'text', 'text_font',
    'text_align', 'text_leading', 'text_size', 'text_width',
    'text_ascent', 'text_descent',
    'PImage', 'image', 'load_image', 'image_mode',
    'load_pixels',
    'lights', 'ambient_light', 'directional_light', 'point_light', 'light_falloff',
    'light_specular',
    'normal_material', 'basic_material', 'blinn_phong_material', 'ambient', 'emissive',
    'diffuse', 'shininess', 'specular',
    'Arc', 'point', 'line', 'arc', 'triangle', 'quad',
    'rect', 'square', 'circle', 'ellipse', 'ellipse_mode',
    'rect_mode', 'bezier', 'curve', 'create_shape', 'draw_shape',
    'PShape',
    'begin_shape', 'end_shape', 'begin_contour', 'end_contour',
    'curve_vertex', 'bezier_vertex', 'quadratic_vertex', 'vertex',

    'push_matrix', 'reset_transforms',
    'translate', 'rotate', 'rotate_x', 'rotate_y',
    'rotate_z', 'scale', 'shear_x', 'shear_y',
    'camera', 'frustum', 'ortho', 'perspective',
    'print_matrix', 'reset_matrix', 'apply_matrix',
    # pmath
    'Vector', 'Point'
    # TRIG CONSTANTS
              'TWO_PI', 'PI', 'HALF_PI', 'QUARTER_PI', 'TAU', 'HALF_TAU',
    # MATH FUNCTIONS DEFINED HERE
    'constrain', 'lerp', 'remap', 'normalize', 'distance', 'dist',
    'magnitude', 'mag', 'sq',

    # PERLIN NOISE FUNCTIONS
    'noise', 'noise_detail', 'noise_seed',
    # RANDOM NUMBER GENERATION
    'random_uniform', 'random_gaussian', 'random_seed',

    # BEZIER METHODS
    'bezier_point', 'bezier_tangent', 'bezier_detail',
    # CURVE METHODS
    'curve_point', 'curve_tangent', 'curve_detail', 'curve_tightness',
    # QUADRATIC METHODS
    'quadratic_point',

    # sketch
    'no_loop', 'loop', 'redraw', 'size', 'title', 'no_cursor',
    'cursor', 'exit', 'draw', 'setup', 'run', 'save_frame', 'save']

from .__version__ import __title__
from .__version__ import __description__
from .__version__ import __url__
from .__version__ import __version__
from .__version__ import __author__
from .__version__ import __license__
from .__version__ import __copyright__

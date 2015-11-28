'''OpenGL extension ATI.pixel_format_float

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_pixel_format_float'
_DEPRECATED = False
GL_TYPE_RGBA_FLOAT_ATI = constant.Constant( 'GL_TYPE_RGBA_FLOAT_ATI', 0x8820 )
GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = constant.Constant( 'GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI', 0x8835 )
glget.addGLGetConstant( GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI, (4,) )


def glInitPixelFormatFloatATI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
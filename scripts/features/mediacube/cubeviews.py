# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/ArkwoodAR)

from OpenGL.GL import *
from PIL import Image
from constants import *

def cube_degrees_0(textures):

    texture_ids = _get_texture_ids(textures)

    glFrontFace(GL_CCW)
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_FRONT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 1.1, 0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_RIGHT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, -0.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_BACK])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, -0.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, -0.0, -0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_LEFT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, -0.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 1.1, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_TOP])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glEnd()

def cube_degrees_90(textures):

    texture_ids = _get_texture_ids(textures)

    glFrontFace(GL_CCW)
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_RIGHT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 1.1, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, 1.1, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_BACK])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, -0.0, -0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, -0.0, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_LEFT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.0, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, -0.0, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, -0.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_FRONT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([-0.0, 0.0, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 0.0, 0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 1.1, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_TOP])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.0, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, -0.0, -1.1])
    glEnd()

def cube_degrees_180(textures):

    texture_ids = _get_texture_ids(textures)
    
    glFrontFace(GL_CCW)
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_BACK])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.0, 1.1, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_LEFT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 0.0, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_FRONT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 0.0, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.0, 0.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_RIGHT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.0, 0.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([-0.0, 1.1, -0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_TOP])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glEnd()

def cube_degrees_270(textures):

    texture_ids = _get_texture_ids(textures)

    glFrontFace(GL_CCW)
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_LEFT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.0, 1.1, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_FRONT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.1, 1.1, 0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([1.1, 0.0, 0.0])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_RIGHT])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 0.0, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.0, 0.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_BACK])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.0, 0.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([-0.0, 1.1, -0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_ids[TEXTURE_TOP])
    glBegin(GL_POLYGON)
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.1, 1.1, -1.1])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([1.1, 0.0, -1.1])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.0, 0.0, -1.1])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.0, 1.1, -1.1])
    glEnd()

def _get_texture_ids(textures):
    texture_ids = {}

    for name, image in textures.items():
        
        # convert image to OpenGL texture format
        tx_image = Image.fromarray(image)     
        ix = tx_image.size[0]
        iy = tx_image.size[1]
        tx_image = tx_image.tobytes('raw', 'BGRX', 0, -1)
    
        # create texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, tx_image)
        texture_ids[name] = texture_id

    return texture_ids
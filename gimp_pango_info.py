#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015 Jabiertxof<jabier.arraiza@marker.es>
# License: GPL v3+
# Version 0.1.2
# GIMP plugin to get current layer pango info

from gimpfu import *
import os, pango
from pango_to_svg import *

def get_pango_info(img, resolution_96=True):
    version = gimp.version[0:2]
    is_2dot8_up = version[0] >= 2 and version[1] >= 8
    get_resolution = pdb.gimp_image_get_resolution(img)
    resolution = (get_resolution[0] + get_resolution[1])/2.0
    output_resolution = 90.0
    if resolution_96:
        output_resolution = 96.0
    layer = pdb.gimp_image_get_active_layer(img)
    if is_2dot8_up and pdb.gimp_item_is_text_layer(layer):
        color = pdb.gimp_text_layer_get_color(layer)
        font_info = pango.FontDescription(pdb.gimp_text_layer_get_font(layer))
        container_line_height = pdb.gimp_text_layer_get_line_spacing(layer)
        indent = pdb.gimp_text_layer_get_indent(layer)
        markup = pdb.gimp_text_layer_get_markup(pdb.gimp_image_get_active_drawable(img))
        if not markup:
            markup = "<markup>" + pdb.gimp_text_layer_get_text(pdb.gimp_image_get_active_drawable(img)) + "<markup>"
        fontsize = pdb.gimp_text_layer_get_font_size(layer)
        factor = pdb.gimp_unit_get_factor(fontsize[1])
        hackToTypoGr = 1.0
        if fontsize[1] < 9:
            hackToTypoGr =72.2/72.0
        if fontsize:
            if factor > 0:
                container_font_size = (fontsize[0] / (factor/resolution)) * hackToTypoGr
            else:
                container_font_size = math.floor(fontsize[0] * hackToTypoGr)
        container_letter_spacing = pdb.gimp_text_layer_get_letter_spacing(layer)
        direction = pdb.gimp_text_layer_get_base_direction(layer)
        container_direction = "rtl"
        if direction is 0:
            container_direction = "ltr"
        output = "Container Line Height: " + str(container_line_height) + "\n"
        output += "Container Letter Spacing: " + str(container_letter_spacing) + "\n"
        output += "Container Direction: " + container_direction + "\n"
        output += "Container Indent: " + str(indent) + "\n"
        output += "Container Width: " + str(layer.width) + "\n"
        output += "Container Height: " + str(layer.height) + "\n"
        output += "Container Offset X: " + str(layer.offsets[0]) + "\n"
        output += "Container Offset Y: " + str(layer.offsets[1]) + "\n"
        output += "Container Font: " + font_info.to_string() + "\n"
        output += "Container Font Size: " + str(container_font_size) + "\n"
        output += "Container Color: " + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + "," + str(color[3])  + "\n"
        output += "Input Resolution: " + str(resolution) + "\n"
        output += "Output Resolution: " + str(output_resolution) + "\n"
        output += "Markup: " + markup
        pdb.gimp_message(output)
    else:
        pdb.gimp_message("Selected layer is not a text layer or your Gimp version are not allowed")

register(
    proc_name=("python-fu-pango-info"),
    blurb=("Get pango info"),
    help=("Get pango info"),
    author=("Jabiertxof<jabier.arraiza@marker.es>"),
    copyright=("Jabiertxof"),
    date=("2016"),
    label=("Text Layer to pango markup"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
        (PF_BOOL, "resolution_96", "Use new SVG 96DPI resolution?", True)
        ],
    results=[],
    function=(get_pango_info),
    menu=("<Image>/File/Export/PANGO/")
    )

main()

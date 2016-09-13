# pangoToSVG
Version: 0.1.1, License: GPL v3+

##No Install
Use as helper to other code like [gimpToSVG](https://github.com/jabiertxof/gimpToSVG)

##Objective
Convert pango text to SVG

##Usage
> svg = PangoToSVG(pango_markup)
Create a object, pango_markup is a string like:"<markup>...</markup>"
Container inherits to childs if not full defined so we need to recreate container properties:
- **svg.setContainerLineHeight(10)** Line Height
- **svg.setContainerLetterSpacing(1)** Letter Spacing
- **svg.setContainerDirection("ltr")** Text Direction
- **svg.setContainerOffsetX(10)** Offset X
- **svg.setContainerOffsetY(100)** Offset Y
- **svg.setContainerFont(pango.FontDescription("serif"))** Font description
- **svg.setContainerFontSize(12)** Font Size
- **svg.setContainerColor([0,0,0,255])** Container Color
- **svg.setInputResolution(96)** Input resolution
- **svg.setOutputResolution(96.0)** Output resolution

Get the SVG output with:
> data = svg.parse()

##Know issues
Know issues in export as text:
- Text can be moved a bit
- Gimp fixed width box not fit perfect **gimpToSVG**
- Gimp indentation dont work **gimpToSVG**

##Changelog
- 0.1.0 Initial release
-0.1.1 Remove comments and move to .md

##Credits
```
Copyright 2015 Jabiertxo Arraiza (jabiertxof)
Special thanks to Erdem Guven Chris Mohler an Gez, and people helping in internet.
```

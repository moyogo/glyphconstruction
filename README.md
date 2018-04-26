Glyph Construction
==================

**Glyph Construction is a simple, human-readable, powerful language for describing how shapes are constructed.**

Glyph Construction can be used to create new glyphs from components. It is specially useful for creating accented glyphs.

Collections of Glyph Construction rules can be saved as `*.glyphConstruction` files, and can be shared between fonts.

[TOC]

## Assigning a construction to a glyph

Build `<destGlyphName>` out of one or more components.

```
<destGlyphName> = <glyphName> + <glyphName>
Aacute = A + acute
```

Optionally, a suffix can be provided. If a glyph with the given suffix does not exist in the font, the suffix is ignored.

```
Aacute = A + acute.cap
```

## Comments

A line starting with (or anything after) a `#` is a comment and will not be used during execution.

```
# this is a comment
Aacute = A + acute
Agrave = A + grave # this is also a comment
```

## Unicodes

```
<destGlyphName> = <glyphName> + <glyphName> | <unicode>
Aacute = A + acute | 00C1
```

## Mark Color

```
<destGlyphName> = <glyphName> + <glyphName> ! <rgba>
Aacute = A + acute ! 1, 0, 0, 1
```

## Metrics

### Width

```
<destGlyphName> = <glyphName> + <glyphName> ^ <width>
Aacute = A + acute ^ 400
```

### Left and Right Margins

```
<destGlyphName> = <glyphName> + <glyphName> ^ <leftmargin>, <rightMargin>
Aacute = A + acute ^ 30, 30
```

Width and margin values can also be defined using basic maths and references to `width`, `leftMargin` or `rightMargin` of other glyphs.

```
# width is equal to twice the width of A
Aacute = A + acute ^ A * 2

# left margin is equal to one third of the left margin of A
# right margin is equal to twice the right margin of B
Aacute = A + acute ^ A / 3, B * 2
```

## Ignore existing glyphs

Add `?` before a glyph construction rule to ignore this glyph if it already exists in the font.

```
?Aacute = A + acute
```

## Positioning

The Glyph Construction language offers different ways to position the added components in relation to the current glyph.

### By Numbers

```
Aacute = A + acute@100
Aacute = A + acute@100,100
```

### By Percentages

```
Aacute = A + acute@50%,50%
```

### By Reference

A reference could be (in this order):

- double anchor (with the `_<anchorName>` notation)
- a single anchor name
- a local guide name
- a global guide name
- a font dimension attribute: `descender`, `xHeight`, `capHeight`, `ascender`
- a calculated reference position: `top`, `bottom`, `left`, `right`, `innerLeft`, `innerRight`, `center`, `origin`, `width`

```
Aacute = A + acute@center,top
```

### By Transformation Matrix

`@` followed by a transformation matrix: 6 values `xx, xy, yx, yy, x, y`

```
Aacute = A + acute@1, 0, 0, 1, 100, 100
```

### Change the current glyph

The current glyph is always the last component added.

For example, `Aacute = A + acute` will:

- add component with name `A` (there is no current glyph)
- add component with name `acute` (the current glyph is `A`)
- force the current glyph with `@<glyphName>:<pos>`

```
Ocircumflexdotaccent =  O + circumflex@center,top + dotaccent@O:center,bottom
```

### Flipping

`~` followed by a position will flip a component:

```
# flip horizontal
Aacute = A + acute@~center,top

# flip vertical
Aacute = A + acute@center,~top

# flip both horizontal and vertical
Aacute = A + acute@~center,~top
```

## Stacking Vertically

```
Aringacute = A + ring@center,top + acute@center,top
```

## Positioning formulas

```
Aringacute = A + ring@center,`top+10` + acute@center,`top-10`
```

## Stacking Horizontally

```
ffi = f & f & i
```

## Variables

Glyph Construction supports variables, which can be defined once at the top of the document and used multiple times.

```
$name = something # declaration
{name} # usage

$myColorMark = 1, 0, 0, 1 # declaration
agrave = a + grave@center,top ! {myColorMark} # usage
```

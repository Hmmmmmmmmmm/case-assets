# Fluffy cartoon revision

Method: built-in image-generation editor, using `case-original.png` as the edit target and requesting transparency. No model selector was available, so image-gen-2.5 is not claimed.

## Base edit prompt

Use case: style-transfer. Edit target: supplied original C.A.S.E. mascot. Create one single centered mascot, no markers, no text, fully transparent background. Restyle this SAME character as a charming fluffy cartoon sticker illustration. Preserve yellow softly rounded triangular body, same upright orientation, large black oval/circular eyeglasses with yellow inside, two black oval eyes, black bow tie at bottom, same proportions. Make fur visibly soft and fluffy with little tufted contour and gently drawn tufts, clean expressive cartoon rendering rather than photorealistic fur. Keep glasses and bow tie strong black with smooth cartoon outlines. Neutral friendly face, no mouth needed, no arms or legs or additional accessories. Character fills square with generous unclipped margin. Real RGBA transparent background, no checkerboard or background color. Preserve identity and geometry aggressively; only increase fluffiness and cartoon style.

## Composition

`compose.py` uses one shared 410 px fluffy base at (18,70). Cartoon marker layers are 216 px wide, rendered at 3× resolution for clean edges, with dark outlines and white sticker borders. Bottom-right markers begin at (292,292); top-right markers at (292,0). Status colors and meanings are preserved. Expressions use small mouths and eyebrows. Historical initial assets remain recoverable from Git history.

# Short-haired 3D cartoon revision

Method: built-in image-generation editor, original mascot as edit target, transparency requested. Model identifier is not exposed. Saved base: `case-3d-base.png`. The original remains unchanged.

## Base edit prompt

Use case: style-transfer. Edit ONLY the supplied ORIGINAL yellow C.A.S.E. mascot into a polished cute 3D cartoon icon on fully transparent background. Most important: preserve the exact original softly rounded triangular silhouette and proportions, same eyeglasses shape/size/position, two black oval eyes, black bow tie shape/position, original yellow, original orientation. No bulging body, no taller peak, no broadening or narrowing, no extra limbs. Surface is mostly smooth soft yellow with extremely short sparse tiny fine hairs, like a lightly fuzzy animated cartoon character; NOT fluffy, shaggy, feathered, woolly or tufted. No long hair or tufts changing the contour. Add gentle 3D rounded volume and soft shading within the original body silhouette, subtly dimensional black eyeglasses and bow tie. Keep simple original identity. One centered neutral mascot only, no mouth needed, no markers or text. Full character including bow tie fully inside square with margin. Real RGBA transparent background, no shadow on a ground, no checkerboard.

## Composition

All icons use one 410 px base at (18,70). `compose.py` adds minimal expressions and 216 px cartoon markers, thick dark outlines and white sticker borders. Bottom-right layers at (292,292); top-right at (292,0). Status meanings and larger marker design are retained. Composition is reproducible from the saved base; the generative edit itself is not deterministic.

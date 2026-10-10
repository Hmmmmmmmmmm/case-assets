# C.A.S.E. notification icons

A consistent family of transparent notification icons for the Bark iOS service. This public repository hosts notification assets.

![Contact sheet](previews/case-icon-contact-sheet.png)

## Icons and public URLs

| Preview | Status / intended use | CDN | Raw fallback |
|---|---|---|---|
| <img src="logos/case-info.png" width="64" alt="info"> | Routine information and important findings | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-info.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-info.png) |
| <img src="logos/case-success.png" width="64" alt="success"> | Successful completion | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-success.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-success.png) |
| <img src="logos/case-failure.png" width="64" alt="failure"> | Failed task | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-failure.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-failure.png) |
| <img src="logos/case-question.png" width="64" alt="question"> | Decision required | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-question.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-question.png) |
| <img src="logos/case-urgent.png" width="64" alt="urgent"> | Critical intervention | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-urgent.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-urgent.png) |
| <img src="logos/case-review.png" width="64" alt="review"> | Work ready for review | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-review.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-review.png) |
| <img src="logos/case-reminder.png" width="64" alt="reminder"> | Scheduled reminder | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-reminder.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-reminder.png) |
| <img src="logos/case-blocked.png" width="64" alt="blocked"> | Blocked job | [PNG](https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@main/logos/case-blocked.png) | [PNG](https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-blocked.png) |

Masters are 512 × 512 RGBA PNGs. Optimized 256 px versions use `logos/256/`. Branch URLs may retain a cached earlier revision. Verified current revision CDN base: `https://cdn.jsdelivr.net/gh/Hmmmmmmmmmm/case-assets@30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/`. Verified current raw base: `https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/`. Append any filename listed above. Both sets of eight pinned URLs returned HTTP 200 and matched local PNG checksums.

## Bark configuration

Preserve the existing autonomous escalation policy. Select group by required user action and level independently by urgency. Use these Bark_notifications.notify parameters:

| Occasion | icon | group | level | sound |
|---|---|---|---|---|
| Routine information | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-info.png | Information | active | telegraph |
| Important finding | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-info.png | Information | timeSensitive | newsflash |
| Successful completion | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-success.png | Information | timeSensitive | fanfare |
| Work ready for review | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-review.png | Review | timeSensitive | fanfare |
| Decision required | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-question.png | Action Needed | timeSensitive | bell |
| Job blocked | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-blocked.png | Action Needed | timeSensitive | alarm |
| Task failed | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-failure.png | Action Needed if intervention required; otherwise Information | context-dependent | alarm |
| Critical intervention | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-urgent.png | Action Needed | critical | horn |
| Scheduled reminder | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-reminder.png | Reminders | context-dependent | chime |

For critical alerts, set volume=10. Resolve context-dependent levels using the existing escalation policy. Do not add device keys to this configuration.

Example invocation parameters for `Bark_notifications.notify` (merge with the connected tool's required title/body fields):

```json
{
  "title": "C.A.S.E.",
  "body": "Work is ready for review.",
  "icon": "https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/30ad4ef640bafcd95e33e06b3d7d6e427a696569/logos/case-review.png",
  "group": "Review",
  "level": "timeSensitive",
  "sound": "fanfare"
}
```

## Method and validation

The revised short-haired 3D cartoon mascot was created with the built-in image-generation editor using the user-supplied original as its reference. The tool does not expose a model selector; no claim is made that image-gen-2.5 was used. The generated base is retained in `sources/case-3d-base.png`; the untouched original remains in `sources/case-original.png`. All eight icons share the same generated base. The original rounded triangular silhouette is retained with tiny fine surface hairs, without the long contour tufts of the previous revision. Pillow adds minimal expressions and consistent larger cartoon markers with thick dark outlines and white sticker borders. Marker layers are 216 px wide and may overlap roughly a third of the character's side, as requested in the revision.

Rebuild the exported icons from the saved generated base with Python and Pillow: `python3 sources/compose.py`. This composition is reproducible; generation of the 3D base is not deterministic. The script uses Arial Bold on macOS, with DejaVu Sans Bold as fallback. Exact typography requires the same font. `sources/validation.json` records dimensions and sizes. All 16 PNG exports were decoded and checked for RGBA encoding, requested dimensions and transparent corners. The contact sheet includes visually inspected 64 px previews. Review retains a blue exclamation mark; blocked retains a red octagonal stop sign and the exact text BLOCKED. The BLOCKED label remains small at 64 px, but is larger than in the initial family. `sources/public-url-validation.json` records remote verification.

Original mascot supplied by the user; retained in `sources/case-original.png`. No copyright ownership claim or third-party license is assigned. No Bark device keys or credentials are included.

# website_silvia

Static personal homepage for planetary astronomer Dr. Silvia Protopapa. The site is ready to be deployed on GitHub Pages.

## Getting Started

1. Clone the repository to your local machine.
2. Open `index.html` in your browser to preview the site.
3. To host on GitHub Pages, push the repository to a GitHub repository named `<username>.github.io` or enable Pages on the repository settings.

## Local imagery

The live site is intended to load a portrait from `assets/images/silvia-protopapa-headshot.jpg`. The actual photograph is not
committed to this repository so it can be uploaded manually without hitting binary-file restrictions. Until the real image is in
place the `<img>` element will gracefully fall back to `assets/images/headshot-fallback.svg`.

Run the helper script to fetch the latest portrait when you have network access:

```bash
python scripts/download_assets.py
```

If the download fails, please check your connectivity or manually copy a headshot for Dr. Protopapa into
`assets/images/silvia-protopapa-headshot.jpg`.

## Content Overview

- Hero section featuring Dr. Protopapa, quick links, and a Pluto background image from the New Horizons mission.
- About section summarizing research interests.
- Featured projects highlighting mission-related work.
- Call-to-action with links to CV, publication records, and contact information.

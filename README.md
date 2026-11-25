# socialmediamasters.in

Website for **Social Media Masters**, Delhi. *Brands That Outlast the Feed.*

Plain HTML, CSS and JavaScript in the Midnight Luxe brand style. No frameworks, no build tools to install beyond Python 3.

## Folder layout

| Path | What it is |
| --- | --- |
| `src/pages/*.html` | Page content (one file per page). Edit text here. |
| `build.py` | Wraps every page in the shared header, footer and meta tags, and writes the finished site to `public/`. |
| `assets/` | CSS, JavaScript, logo, favicons, social share image. |
| `public/` | The finished site that gets deployed. Do not edit by hand; run the build. |
| `app.yaml` | Google App Engine config that serves `public/`. |

## Change something

1. Edit the page in `src/pages/` (or `assets/css/style.css`).
2. Run `python3 build.py`.
3. Commit both the source change and the updated `public/`.

## Preview locally

```
python3 build.py
cd public && python3 -m http.server 8000
```
Then open http://localhost:8000.

## Deploy (Google Cloud App Engine)

```
gcloud app deploy app.yaml --project <your-project-id>
```
Then map the custom domain in Google Cloud Console > App Engine > Settings > Custom domains, and add the DNS records it shows in BigRock. Google issues the HTTPS certificate automatically.

## Forms

The Free Audit and Contact forms need no server: they open WhatsApp (+91 99119 41474) with the visitor's details filled in.

# pix2chocolate-shop

A [nanodjango](https://github.com/radiac/nanodjango) pseudo-ecommerce web application to design, preview, order and generate chocolate low-relief chips.

To be presented at the GrafikLabor 2026 conference :)

## Architecture
This webapp embeds a headless Blender3D as library (bpy), a Django+SQL app (with administration and endpoints) and a React order form (soon). 

### Endpoints
Typically running on `http://localhost:8000/`:
- `POST /api/preview`: (from file upload of a 1275x800 greyscale image) generates a .PNG chocolate biscuit 2D image preview (<3 seconds rendering)
- `POST /api/cad_part`: (from file upload of a 1275x800 greyscale image) generates .STL a pluggable 3D printable chocolate matrix insert for vacuum-forming
- `GET /api/docs`: OpenAPI (ex-Swagger) documentation. 
- `GET /admin`: Django's admin app. A default admin user login and password are given on first installation.
- `GET /`: (coming soon): online form.
- `POST /api/order`: (coming soon) order writing from the online form.

## Installing
Using the `uv` Python package manager:

```sh
uv pip install -r pyproject.toml
```

## Running
Optional (may fix site package issues):
```sh
. venv/bin/activate
```

```sh
nanodjango run app.py
```

## Requirements
Any Linux with a CPU (no need for a GPU).
The project mainly depends on `nanodjango`/Django and `bpy` (Blender as a Python module).
Downloading and installing packets may take long as `bpy` is heavy (about 300MB) and depends on scientific modules such as `numpy`, which might compile on download.


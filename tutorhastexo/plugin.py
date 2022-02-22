from .__about__ import __version__
from glob import glob
import os
import pkg_resources


templates = pkg_resources.resource_filename(
    "tutorhastexo", "templates"
)

config = {
    "add": {
        "XBLOCK_SETTINGS": {},
        "SECRET_KEY": "{{ 50|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "GUACD_DOCKER_IMAGE": "guacamole/guacd:1.4.0",
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}hastexo:{{ HASTEXO_VERSION }}",
        "XBLOCK_VERSION": "stable",
        "DEBUG": False,
    }
}

hooks = {
    "build-image": {
        "hastexo": "{{ HASTEXO_DOCKER_IMAGE }}"
    },
    "remote-image": {
        "hastexo": "{{ HASTEXO_DOCKER_IMAGE }}"
    }
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorhastexo", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches

Tutor plugin for the [Hastexo Guacamole Client](https://github.com/hastexo/hastexo-xblock/tree/master/hastexo_guacamole_client)
===============================================


This is a plugin for [Tutor](https://docs.tutor.overhang.io) that
deploys the [Hastexo Guacamole
Client](https://github.com/hastexo/hastexo-xblock/tree/master/hastexo_guacamole_client)
application alongside Open edX.  Using this plugin is neccessary for
running the [Hastexo
XBlock](https://github.com/hastexo/hastexo-xblock) in your Tutor Open
edX platform.


Installation
------------

First of all, before installing this plugin, make sure you have
installed the [Hastexo
XBlock](https://github.com/hastexo/hastexo-xblock) to your Open edX
platform running with Tutor. For that, add the XBlock to your
`OPENEDX_EXTRA_PIP_REQUIREMENTS` in `config.yml`:

```
OPENEDX_EXTRA_PIP_REQUIREMENTS:
- git+https://github.com/hastexo/hastexo-xblock.git
```

rebuild the `openedx` docker image:

```
tutor images build openedx
```

then upload the image to the registry of your choice, and set
`DOCKER_IMAGE_OPENEDX` in your `config.yml` to reference that image.

For more information about installing XBlocks, please refer to the
[Tutor documentation for installing
XBlocks](https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements)


Then, to install this plugin, run:

```
pip install git+https://github.com/hastexo/tutor-contrib-hastexo
```

To enable this plugin, run:

```
tutor plugins enable hastexo
```

Before starting Tutor, build the docker image for the `hastexo`
service:

```
tutor images build hastexo
```

then (as with the `openedx` image) upload the image to your preferred
registry, and set `HASTEXO_DOCKER_IMAGE` to point to that image.

Configuration
-------------

* `HASTEXO_XBLOCK_SETTINGS`: The Hastexo XBlock settings, examples and
  details provided in the [XBlock
  README](https://github.com/hastexo/hastexo-xblock#deployment). (default:
  `{}`)
* `HASTEXO_XBLOCK_VERSION`: The Hastexo XBlock version. (default:
  `stable`)
* `HASTEXO_GUACD_DOCKER_IMAGE`:
  [guacd](https://hub.docker.com/r/guacamole/guacd) version. (default:
  `guacamole/guacd:1.4.0`)

License
-------

This software is licensed under the terms of the AGPLv3.

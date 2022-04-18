Unreleased
-----------------------------

* Refactor the way we add `HASTEXO_XBLOCK_SETTINGS` to the
  `XBLOCK_SETTINGS`. Add the settings under the `hastexo` key
  without overriding the general definition.
* Fix terminal customisation options. Override the default
  settings module for the `hastexo_guacamole_client`
  so that the `XBLOCK_SETTINGS` will be present in the
  `hastexo` container and thus, will make it possible to
  define custom settings for the terminal window.

## Version 0.0.2 (2022-02-25)

* Fix version number as it appears in pip list (previously, all
  installations would show up as version 0.0.0, including
  installations from the 0.0.1 tag).


## Version 0.0.1 (2022-02-24)

**Experimental. Do not use in production.**

* Add basic testing via tox
* Initial Git import

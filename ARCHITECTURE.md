# The OpenPype Arquitecture

OpenPype Project is made of X distinctive modules/directories:
  * `openpype` (module) the core of the pipeline,
    a collation of Avalon and Pyblish with glue around them both.

  * `igniter` (module) is a GUI tool to deploy a given OpenPype bundle, it can install a fresh version
    or update an existing one. It's currently bundled with OpenPype since it relies on the original
    source code found in `openpype` to create a zip version of it, which is then used to install in
    the user directory. It's threaded so the main UI can stay reactive while performing the install.

  * `repos` folder to clone other projcts, at the moment only `avalon-core`
    https://github.com/getavalon/core 

  * `schema` All data within the database and on disk follow a strict layout,
    known as a "schema", read more on these at https://getavalon.github.io/2.0/reference/#schemas

  * `tests` (module) the test suite for OpenPype and the different modules. 
    https://openpype.io/docs/dev_testing

  * `tools` (directory) a collection of tools to help the development, deployment and operation
    of OpenPype. Some of theses are in both `bash` and `Powershell` scripts. Desribed in:
    https://openpype.io/docs/dev_build/#platform-specific-steps
    https://openpype.io/docs/dev_build/#script-tools

  * `vendor` (directory) a placeholder directory where to download different vendored tools,
    namely `ffmpeg` and `oiio`.

  * `website` the source files for the OpenPype.org (?) website.



ASCII ART DISPLAYING HOW THESE ARE INTERCONNECTED.

Following is a more in depth description of the OpenPype module, note that this might overlap slightly with the docs,
so these will be refered when that occurs. And the docs will *always* take precedence over this document.

## OpenPype (`openpype`)
OpenPype (OP) is the core module of, you guessed it, OpenPype, it's the self-contained module that is the brains of the
deployed pipeline.

The main entry point is the `cli.py` file, which exposes most of the sub-modules in a friendly way (through an abstraction found
in `pype_commands.py`), when interacting through code though, the main enty point should be through `api.py` which imports the public
functions to interact with OP.

The files `__init__.py`, `action.py` and `plugin.py` are top-level overrides/extensions for or around pyblish and avalon.

A quick rundown of all the sub-modules:
  * `hooks` - Functions to be triggered when something else happens (i.e: creating the destination directory of a publish).
  * `hosts` - Digital Content Creation (DCC) specific sub-modules: utilities, pyblish plugins, hooks, menu/init files etc.
  * `lib` - The main library, that feeds into `cli` and the `api` such as `anatomy` a settings handler; `delivery` methods
    to generate delivey data, `mongo` methods to interact with the MongoDB and more.
  * `modules` - Addons that extend the OpenPype core functionality ie. ftrack actions, third party services integration, etc.
  * `pipeline` - Defines how data is created, loaded and published.
  * `plugins` - Extra, non-core functions for the load and publish pipeline functionality.
  * `resources` - Icons, fonts, etc.
  * `scripts` - Standalone scripts.
  * `settings` - All logic that handle and defines the project settings (constants, entities, host specifics...).
  * `style` - Qt related styling.
  * `tests` - Unit and integration tests.
  * `tools` - Tools to interact with OpenPype, i.e. `launcher`, `publisher`, `tray`, etc.
  * `vendor` - Vendored Python packages.
  * `widgets` - Qt Widgets used across OpenPype.



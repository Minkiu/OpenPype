import logging

from .utils import get_representation_path_from_context


class LoaderPlugin(list):
    """Load representation into host application

    Arguments:
        context (dict): avalon-core:context-1.0
        name (str, optional): Use pre-defined name
        namespace (str, optional): Use pre-defined namespace

    .. versionadded:: 4.0
       This class was introduced

    """

    families = list()
    representations = list()
    order = 0
    is_multiple_contexts_compatible = False

    options = []

    log = logging.getLogger("SubsetLoader")
    log.propagate = True

    def __init__(self, context):
        self.fname = self.filepath_from_context(context)

    @classmethod
    def get_representations(cls):
        return cls.representations

    def filepath_from_context(self, context):
        return get_representation_path_from_context(context)

    def load(self, context, name=None, namespace=None, options=None):
        """Load asset via database

        Arguments:
            context (dict): Full parenthood of representation to load
            name (str, optional): Use pre-defined name
            namespace (str, optional): Use pre-defined namespace
            options (dict, optional): Additional settings dictionary

        """
        raise NotImplementedError("Loader.load() must be "
                                  "implemented by subclass")

    def update(self, container, representation):
        """Update `container` to `representation`

        Arguments:
            container (avalon-core:container-1.0): Container to update,
                from `host.ls()`.
            representation (dict): Update the container to this representation.

        """
        raise NotImplementedError("Loader.update() must be "
                                  "implemented by subclass")

    def remove(self, container):
        """Remove a container

        Arguments:
            container (avalon-core:container-1.0): Container to remove,
                from `host.ls()`.

        Returns:
            bool: Whether the container was deleted

        """

        raise NotImplementedError("Loader.remove() must be "
                                  "implemented by subclass")

    @classmethod
    def get_options(cls, contexts):
        """
            Returns static (cls) options or could collect from 'contexts'.

            Args:
                contexts (list): of repre or subset contexts
            Returns:
                (list)
        """
        return cls.options or []


class SubsetLoaderPlugin(LoaderPlugin):
    """Load subset into host application
    Arguments:
        context (dict): avalon-core:context-1.0
        name (str, optional): Use pre-defined name
        namespace (str, optional): Use pre-defined namespace
    """

    def __init__(self, context):
        pass


def discover_loader_plugins():
    import avalon.api

    return avalon.api.discover(LoaderPlugin)


def register_loader_plugin(plugin):
    import avalon.api

    return avalon.api.register_plugin(LoaderPlugin, plugin)


def deregister_loader_plugin_path(path):
    import avalon.api

    avalon.api.deregister_plugin_path(LoaderPlugin, path)


def register_loader_plugin_path(path):
    import avalon.api

    return avalon.api.register_plugin_path(LoaderPlugin, path)


def deregister_loader_plugin(plugin):
    import avalon.api

    avalon.api.deregister_plugin(LoaderPlugin, plugin)

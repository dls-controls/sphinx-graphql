import os

from sphinx.util.fileutil import copy_asset

from sphinx_graphql._version_git import __version__
from sphinx_graphql.graphiql import SphinxGraphiQL

__all__ = ["__version__"]


def setup(app):
    app.add_directive("graphiql", SphinxGraphiQL)
    app.add_css_file("https://cdn.jsdelivr.net/npm/graphiql@1.0.3/graphiql.css")
    app.add_js_file(
        "https://cdn.jsdelivr.net/npm/react@16.13.1/umd/react.production.min.js"
    )
    app.add_js_file(
        "https://cdn.jsdelivr.net/npm/react-dom@16.13.1/umd/react-dom.production.min.js"
    )
    app.add_js_file("https://cdn.jsdelivr.net/npm/graphiql@1.0.3/graphiql.min.js")
    app.add_js_file("attachGraphiQL.js")
    src = os.path.join(os.path.dirname(__file__), "attachGraphiQL.js")
    dst = os.path.join(app.outdir, "_static")
    copy_asset(src, dst)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

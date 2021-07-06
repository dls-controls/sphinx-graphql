from docutils import nodes
from docutils.parsers.rst import Directive


class SphinxGraphiQL(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 1  # endpoint
    option_spec = {"height": int, "query": str, "response": str}

    def run(self):
        if self.arguments:
            self.options["endpoint"] = f'"{self.arguments[0].strip()}"'
        else:
            self.options["endpoint"] = "undefined"
        self.options.setdefault("height", 325)
        raw_content = (
            """
<style>
.graphiql {
    height: %(height)dpx;
    margin: 0 0 24px 0;
}
.graphiql-container .secondary-editor, .graphiql-container .toolbar,
.graphiql-ro .execute-button, .graphiql-ro .docExplorerShow {
    display: none
}
</style>
<div id="graphiql" class="graphiql">
    Loading GraphiQL...
    <div class="query">
%(query)s
    </div>
    <div class="response">
%(response)s
    </div>
    <script>
        attachGraphiQL(document.currentScript.parentNode, %(endpoint)s);
    </script>
</div>
"""
            % self.options
        )
        # Copied from the docutils.parsers.rst.directives.misc.Raw directive
        raw_node = nodes.raw("", raw_content, format="html")
        (raw_node.source, raw_node.line) = self.state_machine.get_source_and_line(
            self.lineno
        )
        return [raw_node]

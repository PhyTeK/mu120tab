class GetattrNode(Node):
    def __init__(self, vars):
        self.vars = vars

    def render(self, context):
        return str(resolve_variable("%s.%s" % (self.vars[0], resolve_variable(self.vars[1], context)), context))


def do_getattr(parser, token):
    """
    Return the value of the given attribute in the given object.

    This differs from the regular use of {{ object.attribute }}.  In the case of {% get object attr_var %}
    attr_var is a variable and the actual attribute fetched from 'object' is the value of that var not
    it's name like in regular Django variable resolution.
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError, "usage: getattr <object> <attribute>"
    return GetattrNode(bits[1:])


register_tag('getattr', do_getattr)

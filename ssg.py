import typer
from ssg.site import Site
import ssg.parsers
import sys

def main(source = "content", dest = "dist"):
    config = {"source" : source, "dest" : dest, "parsers" : [ssg.parsers.ResourceParser(), ssg.parsers.MarkdownParser(), ssg.parsers.ReStructuredTextParser()]}
    site = Site(**config).build()

@staticmethod
def error(message):
    sys.stderr.write("\x1b[1;31m{}\n").format(message)

typer.run(main)
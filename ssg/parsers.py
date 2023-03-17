from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []
    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(self, path, source, dest):
        self.path = Path(path)
        self.dest = Path(dest)
        self.source = Path(source)
        raise NotImplementedError
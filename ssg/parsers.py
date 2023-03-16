from typing import List
from pathlib import Path

class Parser:
    extensions = []
    def valid_extension(self, extension):
        if self.extensions in extension:
            return extension
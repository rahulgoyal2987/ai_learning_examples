import pathspec
spec_text = """  
/*
# But do not ignore debug.log
!*gz
!*ubyte
!.venv/
"""
spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, spec_text.splitlines())
matches = spec.match_tree("C:\\Users\\rahgoyal3\\myproject")
print(list(matches))

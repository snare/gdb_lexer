from setuptools import setup
 
__author__ = 'snare@ho.ax'
 
setup(
    name='GDB Pygments Lexer',
    version='0.1',
    description=__doc__,
    author=__author__,
    packages=['gdb_lexer'],
    entry_points='''[pygments.lexers]
gdblexer = gdb_lexer:GDBLexer
'''
)


import os
import tempfile
import pytest

#from flaskr import flaskr


@pytest.fixture
def client():
	a = 0
	b = 1
	print( a + b )

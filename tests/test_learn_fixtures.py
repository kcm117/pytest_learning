import pytest
import tempfile

from my_module.classes import C


# Fixture for a temporary directory
@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


# Fixture for returning an instance of a class to be shared across tests
# Dont call fixtures directly, fixtures can inherit other fixtures
@pytest.fixture
def c_instance(temporary_dir):
    return C()


# Use a fixture for everything in scope
# @pytest.fixture(autouse=True, scope='module')
# scope is 'function' by default, can be 'module', 'package' and 'session'. Session is the most common.
@pytest.fixture
def setup_teardown():
    print("setup")
    yield
    print("teardown")


# You can also rename fixtures if they have non-ideal names (examples: imports from other packages)
@pytest.fixture(name="fix")
def askdjhgkhsjkdghs():
    return 5


# Fixtures can be passed as arguments and they will trigger/be exectured
def test_with_setup_teardown(setup_teardown, fix):
    print("In Test")


# Notice how this has a temp directory from the fixture
def test_f(c_instance, temporary_dir):
    assert c_instance.f() == 1
    print(temporary_dir)


# Explicitly call another fixture to trigger, without passing as an argument
@pytest.mark.usefixtures("setup_teardown")
def test_g(c_instance):
    assert c_instance.g() == 2

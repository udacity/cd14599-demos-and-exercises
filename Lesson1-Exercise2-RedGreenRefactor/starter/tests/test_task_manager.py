from src.task_manager import TaskManager
import pytest

# Fixture to ensure a fresh TaskManager for each test
@pytest.fixture
def manager():
    return TaskManager()

# Existing test to verify setup (should pass)
def test_add_task_returns_uuid(manager):
    task_id = manager.add_task("Test UUID generation")
    assert isinstance(task_id, str)
    assert len(task_id) > 10 # Basic check for UUID-like string

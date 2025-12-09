import uuid

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title: str) -> str:
        """Adds a new task and returns its unique ID."""
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = {'id': task_id, 'title': title, 'completed': False}
        return task_id

    # The new get_task method will go here!

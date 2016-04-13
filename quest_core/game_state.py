# -*- coding: utf-8 -*-

class GameState:
    def __init__(self):
        self.device_master = None
        self.tasks = []

        self.active_tasks = []
        self.active_tasks_old_state = []

        self.skipped_tasks = [];

        # always allow to open enter door
        self.openDoorPermission = [True, False, False]

    def start_game_loop(self, callback):
        if not self.device_master: return
        if not self.slave: return

        root_task = self.find_task_with_id(Global.INIT_TASK_ID)
        self.active_tasks.append(root_task)

        while len(self.active_tasks):
            self.game_loop(callback)

    def game_loop(self, callback):
        if not self.state: return

        for task in self.active_tasks:
            self.perform_task_if_satisfies(task)

        if self.active_tasks_old_state != self.active_tasks:
            self.active_tasks_old_state = copy.copy(self.active_tasks)
            callback(None) if callback else None

    def perform_task_if_satisfies(self, task):

        task_success = task.success_requirements_satisfied(self.device_master, task, self)

        task_skipped = task in self.skipped_tasks

        if task_skipped:
            self.skipped_tasks.remove(task)

        if task_success or task_skipped:
            self.remove_active_task(task)
            task.perform_success_actions(self.device_master, task, self)

        elif task.failure_requirements_satisfied(self.device_master, task, self):
            self.remove_active_task(task)
            task.perform_failure_actions(self.device_master, task, self)


    def add_task(self, task):
        self.tasks.append(task)

    def task_with_id_active(self, task_id):
        for active_task in self.active_tasks:
            if active_task.id == task_id:
                return True
        return False

    def remove_active_task(self, task):
        if task in self.active_tasks:
            self.active_tasks.remove(task)

    def find_task_with_id(self, id):
        for task in self.tasks:
            if int(task.id) == int(id):
                return task

    def add_active_task_with_id(self, id):
        task = self.find_task_with_id(id)
        self.active_tasks.append(task)


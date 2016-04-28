from __future__ import print_function
import yaml
from game_state import GameState
from requirement import Requirement
from task import Task
from action import Action

import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from full_quest import *

def parse(file_name):
    game_state = GameState()
    f = open(file_name)
    quest_script_source = yaml.safe_load(f)
    f.close()
    for task_source in quest_script_source["tasks"]:
        task = fillTask(task_source)
        game_state.add_task(task)

    return game_state


def fillTask(task_source):
    task = Task()
    # print("{}".format(task_source["success_requirements"]))
    # print("=========================================\n{}".format(task_source))
    map(lambda req:    task.add_success_requirement(
            Requirement(eval(req))), task_source["success_requirements"])
    map(lambda req:    task.add_failure_requirement(
            Requirement(eval(req))), task_source["failure_requirements"])
    map(lambda action: task.add_success_action(
            Action(eval(action))), task_source["success_actions"])
    map(lambda action: task.add_failure_action(
            Action(eval(action))), task_source["failure_actions"])
    task.title = task_source["title"] if "title" in task_source else "No title"
    task.id = task_source["id"]
    if "showOnMonitor" in task_source:
        task.showOnMonitor = task_source["showOnMonitor"]
    if "type" in task_source:
        task.type = task_source["type"]
    # print("task id: {}".format(task.id))
    return task

import os

tasks_dict2 = {1: 'just_values', 2: 'just_graph', 3: 'graph_and_values'}
class MyTasks:
    def __init__(self, tasks_dict, dataset):
        self.tasks_dict = tasks_dict
        self.dataset = dataset

    def get_task_files(self, task_name):
        if task_name not in self.tasks_dict:
            print("Task is not in global tasks dictionary")
        return self.tasks_dict[task_name](self)

    # @staticmethod
    def just_values(self):
        directory_name = "JustValues"
        mission = 'just_values'
        params_file_path = os.path.join(directory_name, 'params', "best_params", f"{self.dataset}_{mission}.json")
        return directory_name, mission, params_file_path

    # @staticmethod
    def just_graph_structure(self):
        directory_name = "JustGraphStructure"
        mission = 'just_graph'
        params_file_path = os.path.join(directory_name, 'params', "best_params", f"{self.dataset}_{mission}.json")
        return directory_name, mission, params_file_path

    # @staticmethod
    def values_and_graph_structure(self):
        directory_name = "ValuesAndGraphStructure"
        mission = 'graph_and_values'
        params_file_path = os.path.join(directory_name, 'params', "best_params", f"{self.dataset}_{mission}.json")
        return directory_name, mission, params_file_path
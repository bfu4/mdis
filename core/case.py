

class Case:

    def __init__(self, compare_value, self_action):
        """
        Create case
        :param compare_value:
        """
        self.cmp = compare_value
        self.self_action = self_action

    def equals(self, to_compare):
        """
        Compare
        :param to_compare:
        :return:
        """
        return self.cmp == to_compare

    def enact(self, args):
        """
        Do something
        :param args: arguments
        :return:
        """
        self.self_action(args)
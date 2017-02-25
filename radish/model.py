# -*- coding: utf-8 -*-

"""
    This model provides a base class for all models:

    Models:
        * Feature
        * Scenario
        * ScenarioOutline
        * Step
"""

from .exceptions import RadishError


# FIXME: make ABC
class Model(object):
    """
        Represents a base model
    """
    class Context(object):
        """
            Represents a Models context.
            For every feature/scenario a new Context object is created
        """
        def __init__(self):
            self.constants = []

    def __init__(self, id, keyword, sentence, path, line, parent=None, tags=None):
        self.id = id
        self.keyword = keyword
        self.sentence = sentence
        self.path = path
        self.line = line
        self.parent = parent
        self.tags = tags or []
        self.starttime = None
        self.endtime = None

    @property
    def duration(self):
        """
            Returns the duration of this model
        """
        if not self.starttime or not self.endtime:
            raise RadishError("Cannot get duration of {0} '{1}' because either starttime or endtime is not set".format(self.keyword, self.sentence))

        return self.endtime - self.starttime

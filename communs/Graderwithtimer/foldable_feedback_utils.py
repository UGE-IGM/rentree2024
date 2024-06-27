class FoldableFeedbackContent:
    def __init__(self):
        self.content = []

    def add_feedback(self, name, description="", expected="", obtained="", arguments="", display=False, feedback_type="info"):
        self.content.append({
            "name": name,
            "description": description,
            "expected": expected,
            "obtained": obtained,
            "arguments": arguments,
            "display": display,
            "type" : feedback_type
        })

    def add_to_last_feedback(self, name=None, description=None, expected=None, obtained=None, arguments=None, display=None, feedback_type=None):
        if self.content:
            for feedback in reversed(self.content):
                if "feedbacks" not in feedback:
                    feedback["name"] = name if name is not None else feedback["name"]
                    feedback["description"] = description if description is not None else feedback["description"]
                    feedback["expected"] = expected if expected is not None else feedback["expected"]
                    feedback["obtained"] = obtained if obtained is not None else feedback["obtained"]
                    feedback["arguments"] = arguments if arguments is not None else feedback["arguments"]
                    feedback["display"] = display if display is not None else feedback["display"]
                    feedback["type"] = feedback_type if feedback_type is not None else feedback["type"]
                    break

    def add_category(self, name, description="", display=False, feedback_type="info", feedbacks=[]):
        if type(feedbacks) == list:
            self.content.append({
                "name": name,
                "description": description,
                "display": display,
                "type": feedback_type,
                "feedbacks": feedbacks
            })
        elif feedback_type(feedbacks) == FoldableFeedbackContent:
            self.content.append({
                "name": name,
                "description": description,
                "display": display,
                "type": feedback_type,
                "feedbacks": feedbacks.get()
            })
        else:
            raise Exception("Feedbacks must be a list or a FoldableFeedbackContent object")
        
    def add_to_last_category(self, name=None, description=None, display=None, feedback_type=None, feedbacks=None):
        if self.content:
            for feedback in reversed(self.content):
                if "feedbacks" in feedback:
                    feedback["name"] = name if name is not None else feedback["name"]
                    feedback["description"] = description if description is not None else feedback["description"]
                    feedback["display"] = display if display is not None else feedback["display"]
                    feedback["type"] = feedback_type if feedback_type is not None else feedback["type"]
                    if feedbacks is not None:
                        if type(feedbacks) == list:
                            feedback["feedbacks"].extend(feedbacks)
                        elif type(feedbacks) == FoldableFeedbackContent:
                            feedback["feedbacks"].extend(feedbacks.get())
                        else:
                            raise Exception("Feedbacks must be a list or a FoldableFeedbackContent object")
                    break
        
    def get_last_category(self):
        for feedback in reversed(self.content):
            if "feedbacks" in feedback:
                return feedback
        return None

    def get(self):
        return self.content

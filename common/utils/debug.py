class Debug:
    def __str__(self) -> str:
        return_text = self.__class__.__name__
        return_text += "("
        for index, (key, value) in enumerate(self.__dict__.items()):
            return_text += f"{key}:{value}"
            if index < len(self.__dict__) - 1:
                return_text += ","
        return_text += ")"
        return return_text

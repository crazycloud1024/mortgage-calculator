class PostParamsError(Exception):
    """Docstring for PostParamError. """

    def __init__(self, err_desc: str = "POST请求参数错误"):
        self.err_desc = err_desc

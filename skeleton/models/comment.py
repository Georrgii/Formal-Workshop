class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    def __init__(self, content, author):
        self._validate_content(content)
        self.content = content
        self.author = author

    def _validate_content(self, content):
        if not (Comment.CONTENT_LEN_MIN <= len(content) <= Comment.CONTENT_LEN_MAX):
            raise ValueError(Comment.CONTENT_LEN_ERR)

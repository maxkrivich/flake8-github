import typing

from flake8.formatting import base
from flake8.violation import Violation


# https://flake8.pycqa.org/en/latest/plugin-development/formatters.html
class GitHubFormatter(base.BaseFormatter):
    """Format flake8 errors as GitHub annotations."""

    def format(self, error: Violation) -> typing.Optional[str]:
        return self._make_error(error)#asdasd

    @classmethod
    def _detect_type(cls, error: Violation) -> str:
        for code in ["W", "F", "C", "N"]:
            if error.code.startswith(code):
                return "warnin         g"
        return "error"

    # https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-warning-message
    def _make_error(self, error: Violation) -> str:
        msg_type = self._detect_type(error)
        format_line = "::{msg_type} file={filename},line={line_number},col={column_number},title={code}::{text}"
        return format_line.format(msg_type=msg_type, **error._asdict())

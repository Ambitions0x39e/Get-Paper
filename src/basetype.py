from .info import paper_objs


class WrongInputException(BaseException):
    """Exception for Wrong Input Existence

    Args:
        BaseException (string): Error Message
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return super().__repr__()


class Paper:
    """
    Class for each Paper

    Args:
        subject (string): Subject Code
        year (string): Year
        season (string): Season
        paper_num (string): Paper Number
        paper_obj (string): Paper Object
    """

    def __init__(self, subject, year, season, paper_num, paper_obj):
        self.subject: str = subject  # 9709 / 0580 / etc.
        self.year: str = year  # 22 / 23 / 24 / etc.
        self.season: str = season.lower()  # m / s / w
        self.paper_num: str = paper_num  # 12 / 13 / 23 / etc
        self.paper_obj: str = paper_obj.lower()  # Ms / Qp / In / etc.
        try:
            self.formatting()
        except WrongInputException as WIE:
            raise WIE

    def formatting(self):
        if len(self.subject) != 4:
            raise WrongInputException("Wrong Subject")
        if len(self.year) not in [2, 4]:
            raise WrongInputException("Wrong Year")
        else:
            if len(self.year) == 4:
                self.year = self.year[2:]
        if self.season in ["march", "mar", "m", "february", "feb", "f"]:
            self.season = "m"
        elif self.season in ["june", "jun", "j", "may", "m"]:
            self.season = "s"
        elif self.season in ["november", "nov", "n", "october", "oct", "o"]:
            self.season = "w"
        else:
            raise WrongInputException("Wrong Season")
        if len(self.paper_num) != 2:
            raise WrongInputException("Wrong Paper Number")
        if self.paper_obj not in paper_objs:
            raise WrongInputException("Wrong Paper Object")

    def __repr__(self):
        return f"{self.subject}_{self.season}{self.year}_{self.paper_obj}_{self.paper_num}.pdf"


class PaperStatusStorage:
    """
    Data structure for Paper Status Storage

    Args:
         paper_name(str): Name of Paper
        paper_status(str): Status of Paper
    """

    def __init__(self, paper_name: str, paper_status: bool) -> None:
        self.paper_name: str = paper_name
        self.paper_status: bool = paper_status

    def __test__output__(self):
        return f"{self.paper_name} status {self.paper_status}"

    def __repr__(self) -> str:
        return f"{self.paper_name} : {self.paper_status}"


if __name__ == "__main__":
    a = Paper("9709", "22", "march", "12", "QP")
    print(a)

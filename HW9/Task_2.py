from datetime import datetime


class WorkerInfo:
    def __init__(self, first_name, last_name, gender, age, birthday, salary, city, position):
        """
        Initializes a WorkerInfo object.

        Args:
            first_name (str): The first name of the worker.
            last_name (str): The last name of the worker.
            gender (str): The gender of the worker.
            age (int): The age of the worker.
            birthday (str): The birthday of the worker in the format "YYYY-MM-DD".
            salary (float): The salary of the worker.
            city (str): The city where the worker resides.
            position (str): The position of the worker.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.birthday = birthday
        self.salary = salary
        self.city = city
        self.position = position

    @staticmethod
    def validate_birthday_format(birthday):
        """
        Validates the format of the birthday string.

        Args:
            birthday (str): The birthday string to validate.

        Returns:
            bool: True if the format is valid, False otherwise.
        """
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @classmethod
    def from_dict(cls, data):
        """
        Creates a WorkerInfo object from a dictionary.

        Args:
            data (dict): A dictionary containing the worker information.

        Returns:
            WorkerInfo: A WorkerInfo object.
        """
        return cls(
            data['first_name'],
            data['last_name'],
            data['gender'],
            data['age'],
            data['birthday'],
            data['salary'],
            data['city'],
            data['position']
        )

    @property
    def full_name(self):
        """
        Gets the full name of the worker.

        Returns:
            str: The full name of the worker.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def age_category(self):
        """
        Gets the age category of the worker based on their age.

        Returns:
            str: The age category of the worker.
        """
        if self.age < 18:
            return "Minor"
        elif self.age < 65:
            return "Adult"
        else:
            return "Senior"

    @property
    def birthday(self):
        """
        Gets the birthday of the worker.

        Returns:
            str: The birthday of the worker in the format "YYYY-MM-DD".
        """
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        """
        Sets the birthday of the worker.

        Args:
            value (str): The birthday to set in the format "YYYY-MM-DD".
        """
        if WorkerInfo.validate_birthday_format(value):
            self._birthday = value
        else:
            raise ValueError("Invalid birthday format. Please use 'YYYY-MM-DD'.")

    def __str__(self):
        """
        Returns a string representation of the WorkerInfo object.

        Returns:
            str: A string representation of the WorkerInfo object.
        """
        return f"Worker Information:\n" \
               f"Name: {self.full_name}\n" \
               f"Gender: {self.gender}\n" \
               f"Age: {self.age}\n" \
               f"Birthday: {self.birthday}\n" \
               f"Salary: {self.salary}\n" \
               f"City: {self.city}\n" \
               f"Position: {self.position}\n"


worker1 = WorkerInfo("Ivan", "Syla", "Male", 30, "1992-05-10", 5000.0, "Odessa", "Manager")
worker2 = WorkerInfo("Olesia", "Smith", "Female", 25, "1997-12-03", 4000.0, "Poltava", "Developer")
worker3 = WorkerInfo("Mykola", "Johnson", "Male", 45, "1978-09-22", 6000.0, "Lutsk", "Accountant")

print(worker1)
print(worker2)
print(worker3)

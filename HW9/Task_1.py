import random


class CompanyInfo:
    def __init__(self, name: str, city: str, industry: str, employee_count: int, revenue: str, founding_year: str,
                 website: str, contact_email: str, phone_number: int, address: str, values: str, certifications: bool):
        """
        Initializes a CompanyInfo instance.

        Args:
            name (str): The name of the company.
            city (str): The city where the company is located.
            industry (str): The industry of the company.
            employee_count (int): The number of employees in the company.
            revenue (str): The revenue of the company.
            founding_year (str): The year the company was founded.
            website (str): The website URL of the company.
            contact_email (str): The contact email of the company.
            phone_number (int): The phone number of the company.
            address (str): The address of the company.
            values (str): The core values of the company.
            certifications (bool): Indicates if the company has certifications.
        """
        self._name = name
        self._city = city
        self._industry = industry
        self._employee_count = employee_count
        self._revenue = revenue
        self._founding_year = founding_year
        self._website = website
        self._contact_email = contact_email
        self._phone_number = phone_number
        self._address = address
        self._values = values
        self._certifications = certifications

    @property
    def name(self) -> str:
        """str: The name of the company."""
        return self._name

    @property
    def city(self) -> str:
        """str: The city where the company is located."""
        return self._city

    @city.setter
    def city(self, new_city: str):
        """
        Sets the city of the company.

        Args:
            new_city (str): The new city to set.

        Raises:
            Warning: If the new city is "Zhytomyr".
        """
        if new_city == "Zhytomyr":
            raise Warning("Is it a joke? Zhytomyr doesn't exist")
        else:
            self._city = new_city

    def update_website(self, new_website: str):
        """
        Updates the website URL of the company.

        Args:
            new_website (str): The new website URL.
        """
        self._website = new_website

    def display_company_info(self):
        """Displays the company information."""
        print("Company Information:")
        print(f"Name: {self._name}")
        print(f"City: {self._city}")
        print(f"Industry: {self._industry}")
        print(f"Employee Count: {self._employee_count}")
        print(f"Revenue: {self._revenue}")
        print(f"Founding Year: {self._founding_year}")
        print(f"Website: {self._website}")
        print(f"Contact Email: {self._contact_email}")
        print(f"Phone Number: {self._phone_number}")
        print(f"Address: {self._address}")
        print(f"Values: {self._values}")
        print(f"Certifications: {'Yes' if self._certifications else 'No'}")

    def get_employee_count(self) -> int:
        """int: Returns the number of employees in the company."""
        return self._employee_count

    def get_random_phone_number(self) -> int:
        """int: Generates and returns a random phone number."""
        random_digits = [str(random.randint(0, 9)) for _ in range(10)]
        phone_number = "".join(random_digits)
        return int(phone_number)

    @classmethod
    def from_dict(cls, company_dict: dict):
        """
        Creates a CompanyInfo instance from a dictionary.

        Args:
            company_dict (dict): The dictionary containing company information.

        Returns:
            CompanyInfo: The created CompanyInfo instance.
        """
        return cls(**company_dict)

    @staticmethod
    def is_revenue_greater(company1, company2) -> bool:
        """
        Compares the revenue of two companies.

        Args:
            company1 (CompanyInfo): The first company.
            company2 (CompanyInfo): The second company.

        Returns:
            bool: True if the revenue of company1 is greater than company2, False otherwise.
        """
        return int(company1._revenue) > int(company2._revenue)

    @staticmethod
    def get_working_mode() -> str:
        """str: Returns the working mode of the company."""
        return '4/3: 4 days of work - 3 days off'

    @staticmethod
    def departments_activities():
        """
        Displays the activities of different company departments.
        """
        print("""
        Some of the company departments and their regular activities described below:

            Sales and Marketing: Promoting products or services, generating leads, and driving revenue through
            various marketing and sales strategies.

            Research and Development: Conducting scientific, technological, or market research to innovate and develop new 
            products, services, or solutions.

            Human Resources: Managing employee recruitment, training, performance evaluation, compensation, benefits, 
            and maintaining a positive work environment.

            Information Technology: Developing and managing IT systems, software applications, networks, cybersecurity, 
            and providing technical support to meet the company's technology needs.

            Customer Service: Providing assistance and support to customers, addressing inquiries, resolving issues, 
            and ensuring customer satisfaction.

            Quality Assurance: Implementing processes and procedures to ensure the quality and consistency of products or 
            services through testing, inspection, and quality control measures.

            Training and Development: Designing and delivering training programs, workshops, and professional development 
            initiatives to enhance employee skills and knowledge.

            Corporate Strategy: Formulating long-term goals, strategic plans, and initiatives to drive business growth, 
            competitiveness, and adaptability in the market.
            """)


companies = []
for _ in range(3):
    company_dict = {
        "name": f"Company_{random.randint(1, 100)}",
        "city": "New York",
        "industry": "Technology",
        "employee_count": random.randint(10, 100),
        "revenue": f"${random.randint(1000000, 10000000)}",
        "founding_year": str(random.randint(1990, 2022)),
        "website": "www.example.com",
        "contact_email": "info@example.com",
        "phone_number": random.randint(1000000000, 9999999999),
        "address": "123 Street, New York",
        "values": "Innovation, Quality, Collaboration",
        "certifications": True
    }
    company = CompanyInfo.from_dict(company_dict)
    companies.append(company)

for company in companies:
    company.display_company_info()

print("Employee Count for Companies:")
for company in companies:
    print(f"{company.name}: {company.get_employee_count()} employees")

companies[0].city = "Zhytomyr"

print(f"\nThe {companies[1].name}'s website is '{companies[1].website}'")
companies[1].update_website("www.updated.website.net")
print(f"The {companies[1].name}'s website was changed to '{companies[1].website}'")

print("\nWorking Mode for Companies:")
print(CompanyInfo.get_working_mode())
print(CompanyInfo.departments_activities())

print("\nRandom Phone Number:")
for _ in range(3):
    company = random.choice(companies)
    print(f"{company.name}: {company.get_random_phone_number()}")

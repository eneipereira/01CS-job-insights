from src.sorting import sort_by

JOBS_MOCK = [
    {
        "title": "Senior Salesforce Developer",
        "min_salary": "10000",
        "max_salary": "25000",
        "date_posted": "2021-09-23",
    },
    {
        "title": "Ultrasound Technologist",
        "min_salary": "7500",
        "max_salary": "18750",
        "date_posted": "2022-10-24",
    },
    {
        "title": "Pest Control Technician",
        "min_salary": "5000",
        "max_salary": "12500",
        "date_posted": "2020-08-22",
    },
]

CRITERIA = ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria():
    sort_by(JOBS_MOCK, CRITERIA[0])
    assert JOBS_MOCK[0]["title"] == "Pest Control Technician"

    sort_by(JOBS_MOCK, CRITERIA[1])
    assert JOBS_MOCK[0]["title"] == "Senior Salesforce Developer"

    sort_by(JOBS_MOCK, CRITERIA[2])
    assert JOBS_MOCK[0]["title"] == "Ultrasound Technologist"

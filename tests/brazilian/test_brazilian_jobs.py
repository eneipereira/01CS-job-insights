from src.brazilian_jobs import read_brazilian_file

PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    jobs_BR = read_brazilian_file(PATH)

    for job in jobs_BR:
        assert "title" in job and "titulo" not in job
        assert "salary" in job and "salario" not in job
        assert "type" in job and "tipo" not in job

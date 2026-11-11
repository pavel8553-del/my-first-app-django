# FitPulse / Django gym tracker

Based on the original `my-first-app-django` project. The two existing models `Member` and `WorkoutLog` are preserved.

## Assignment requirements

1. **Fork** the upstream repository into your GitHub account using the GitHub Fork button. Downloading this ZIP is **not** a GitHub fork.
2. **Migrate DB**: Configure SQL Server with `DB_ENGINE=mssql`, then run `python manage.py migrate` to create the Django tables. The original `0001_initial.py` migration is reused. For an easy local test, omit `.env` to use SQLite.
3. **2 functions per object**: Member -> Add / Delete; WorkoutLog -> Add / Delete.
4. **Show on screen**: Hebrew RTL lists and forms for both objects, plus buttons and status messages.

## Windows setup (PowerShell / VS Code terminal)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### SQL Server with Windows Authentication

1. In SSMS, create an empty database named `GymTrackerDB` (or choose another name). Confirm your Windows user can create tables in it (e.g. db_owner for development only).
2. Install **Microsoft ODBC Driver 18 for SQL Server** on Windows.
3. Copy `.env.example` to `.env`, and change `DB_HOST` to **your exact SSMS Server name**, e.g. `localhost\SQLEXPRESS` or `DESKTOP-ABC\SQLEXPRESS` (no need to change Windows authentication credentials).
4. Run:

```powershell
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/gym/ to see members, and http://127.0.0.1:8000/gym/workouts/ for workouts.

If you just want to quickly test without SQL Server, delete or rename `.env` (default is SQLite), then run `python manage.py migrate` and `python manage.py runserver`. **SQLite demo does not fulfill the SQL Server DB requirement.**

## Tests

```powershell
python manage.py test
```

## Notes

- Deleting a member also deletes their workouts due to `on_delete=models.CASCADE`.
- Delete actions only accept POST and contain CSRF protection and browser confirmation.
- This demo assumes a local development environment; configure credentials, deployment security, and access control before any production use.

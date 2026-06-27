import os
import unittest
from unittest.mock import patch

from app.core.database import DB_PATH, connect_args_for, resolve_database_url


class DatabaseConfigTests(unittest.TestCase):
    def test_uses_local_sqlite_when_database_url_is_absent(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_database_url(), f"sqlite:///{DB_PATH}")

    def test_normalizes_legacy_postgres_scheme(self):
        with patch.dict(os.environ, {"DATABASE_URL": "postgres://db.example/phyllos"}):
            self.assertEqual(
                resolve_database_url(),
                "postgresql://db.example/phyllos",
            )

    def test_sqlite_only_connect_args(self):
        self.assertEqual(
            connect_args_for("sqlite:////tmp/phyllos.db"),
            {"check_same_thread": False},
        )
        self.assertEqual(connect_args_for("postgresql://db/phyllos"), {})


if __name__ == "__main__":
    unittest.main()

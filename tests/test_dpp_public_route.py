import asyncio
import json
import unittest
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

from app.core.database import Base
from app.main import consumer_dpp
from app.models.models import FichaTecnica, Peca


def request_for(path: str) -> Request:
    return Request({
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": path,
        "raw_path": path.encode(),
        "query_string": b"",
        "headers": [],
        "client": ("testclient", 123),
        "server": ("testserver", 80),
    })


class DppPublicRouteTests(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(
            "sqlite:///:memory:",
            connect_args={"check_same_thread": False},
        )
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.engine.dispose()

    def test_get_public_dpp_returns_published_tier1_page(self):
        db = self.Session()
        peca = Peca(
            codigo="PILOTO-TIER1",
            nome="Peça Piloto Tier 1",
            dpp_uuid="uuid-publico-tier1",
            dpp_status="publicado",
            pais_fabricacao="BR",
        )
        db.add(peca)
        db.flush()
        db.add(FichaTecnica(
            peca_id=peca.id,
            composicao_fibras=json.dumps([{"fibra": "algodao", "pct": 100}]),
            instrucoes_reparo="Lavar a frio",
            instrucoes_fim_de_vida="Reparar, doar ou reciclar",
            evidencia_statuses=json.dumps({"composicao_fibras": "declarado"}),
        ))
        db.commit()
        db.close()

        with patch("app.main.SessionLocal", self.Session):
            response = asyncio.run(consumer_dpp(
                request_for("/p/uuid-publico-tier1"),
                "uuid-publico-tier1",
            ))

        self.assertEqual(response.status_code, 200)
        html = response.body.decode()
        self.assertIn("Peça Piloto Tier 1", html)
        self.assertIn("SKU PILOTO-TIER1", html)
        self.assertNotIn("GTIN None", html)
        self.assertIn("Declarado pela marca", html)

    def test_get_public_dpp_rejects_unknown_uuid(self):
        with patch("app.main.SessionLocal", self.Session):
            response = asyncio.run(consumer_dpp(
                request_for("/p/uuid-ausente"),
                "uuid-ausente",
            ))

        self.assertEqual(response.status_code, 404)
        self.assertIn("Passaporte não encontrado", response.body.decode())


if __name__ == "__main__":
    unittest.main()

"""
PHYLLOS Impact Collector — módulo autônomo de coleta de dados de impacto ambiental.

Interface pública:
    from impact_collector import collect_material_impact, ImpactEvidence
"""

from impact_collector.flows.main_flow import collect_material_impact
from impact_collector.models import ImpactEvidence, ImpactSource

__all__ = ["collect_material_impact", "ImpactEvidence", "ImpactSource"]

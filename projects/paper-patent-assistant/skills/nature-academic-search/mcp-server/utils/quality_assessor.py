"""Paper quality assessment module.

Provides multi-dimensional quality scoring using metrics from OpenAlex,
Semantic Scholar, and CrossRef. Designed to help users evaluate citation value
of retrieved papers.
"""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class QualityTier(str, Enum):
    A = "A"   # High-impact, peer-reviewed, well-cited
    B = "B"   # Good quality, moderate citations
    C = "C"   # Acceptable, low citations or preprint
    D = "D"   # Low quality, very few citations, or retracted


@dataclass
class QualityAssessment:
    """Multi-dimensional quality assessment for a paper."""

    # Quantitative metrics
    citation_count: int = 0
    influential_citations: int = 0
    is_open_access: bool = False
    is_peer_reviewed: bool = True
    is_preprint: bool = False
    year: int | None = None
    journal: str = ""

    # Computed scores
    quality_score: float = 0.0
    quality_tier: QualityTier = QualityTier.C
    recommendation: str = ""
    factors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "citation_count": self.citation_count,
            "influential_citations": self.influential_citations,
            "is_open_access": self.is_open_access,
            "is_peer_reviewed": self.is_peer_reviewed,
            "is_preprint": self.is_preprint,
            "year": self.year,
            "journal": self.journal,
            "quality_score": round(self.quality_score, 1),
            "quality_tier": self.quality_tier.value,
            "recommendation": self.recommendation,
            "factors": self.factors,
        }


class QualityAssessor:
    """Assesses paper quality using multi-source metrics."""

    def assess(self, paper_data: dict) -> QualityAssessment:
        """Assess quality of a paper from unified result format.

        Args:
            paper_data: Unified result dict from any source adapter.
                Expected keys: citation_count, influential_citation_count,
                is_open_access, year, journal, source, publication_types, etc.

        Returns:
            QualityAssessment with computed score and tier.
        """
        qa = QualityAssessment()
        factors: list[str] = []

        # Extract metrics
        qa.citation_count = paper_data.get("citation_count", 0) or 0
        qa.influential_citations = paper_data.get("influential_citation_count", 0) or 0
        qa.is_open_access = bool(paper_data.get("is_open_access", False))
        qa.year = paper_data.get("year")
        qa.journal = paper_data.get("journal", "")

        # Detect preprint
        source = paper_data.get("source", "")
        pub_types = paper_data.get("publication_types", [])
        qa.is_preprint = (
            source == "arxiv"
            or "preprint" in (paper_data.get("type", "") or "").lower()
            or "Preprint" in pub_types
        )
        qa.is_peer_reviewed = not qa.is_preprint

        # --- Scoring dimensions ---

        score = 0.0

        # 1. Citation impact (0-40 points)
        citation_score = self._citation_score(qa.citation_count, qa.year)
        score += citation_score * 0.4
        if citation_score > 70:
            factors.append(f"High citation impact ({qa.citation_count} citations)")
        elif citation_score < 20:
            factors.append(f"Low citations ({qa.citation_count})")

        # 2. Influential citations (0-20 points)
        if qa.influential_citations > 0:
            inf_ratio = qa.influential_citations / max(qa.citation_count, 1)
            inf_score = min(inf_ratio * 200, 100)
            score += inf_score * 0.2
            if inf_ratio > 0.3:
                factors.append(f"High influence ratio ({qa.influential_citations} influential)")

        # 3. Peer review status (0-25 points)
        if qa.is_peer_reviewed:
            score += 80 * 0.25
            factors.append("Peer-reviewed")
        else:
            score += 30 * 0.25
            factors.append("Preprint (not peer-reviewed)")

        # 4. Recency bonus (0-15 points)
        recency_score = self._recency_score(qa.year)
        score += recency_score * 0.15
        if recency_score > 70:
            factors.append(f"Recent ({qa.year})")

        qa.quality_score = min(score, 100)
        qa.factors = factors

        # --- Tier assignment ---
        qa.quality_tier = self._assign_tier(qa)
        qa.recommendation = self._generate_recommendation(qa)

        return qa

    def assess_batch(self, papers: list[dict]) -> list[QualityAssessment]:
        """Assess quality for a list of papers.

        Args:
            papers: List of unified result dicts.

        Returns:
            List of QualityAssessment objects, one per paper.
        """
        return [self.assess(p) for p in papers]

    # ------------------------------------------------------------------
    # Scoring functions
    # ------------------------------------------------------------------

    @staticmethod
    def _citation_score(citation_count: int, year: int | None) -> float:
        """Score based on citation count, age-adjusted.

        A paper from 2024 with 10 citations is more impressive than
        one from 2010 with 10 citations.
        """
        if citation_count <= 0:
            return 5.0

        # Log-scale to handle wide range
        raw = math.log10(citation_count + 1) * 30

        # Age adjustment: newer papers get a boost
        if year:
            import datetime
            age = max(1, datetime.datetime.now().year - year)
            citations_per_year = citation_count / age
            if citations_per_year > 50:
                raw += 20
            elif citations_per_year > 20:
                raw += 10
            elif citations_per_year > 5:
                raw += 5

        return min(raw, 100)

    @staticmethod
    def _recency_score(year: int | None) -> float:
        """Score based on publication year. More recent = higher."""
        if not year:
            return 30.0
        import datetime
        age = datetime.datetime.now().year - year
        if age <= 1:
            return 100
        elif age <= 3:
            return 85
        elif age <= 5:
            return 70
        elif age <= 10:
            return 50
        elif age <= 20:
            return 30
        return 15

    @staticmethod
    def _assign_tier(qa: QualityAssessment) -> QualityTier:
        """Assign quality tier based on computed score and factors."""
        s = qa.quality_score

        if s >= 65 and qa.is_peer_reviewed:
            return QualityTier.A
        elif s >= 45:
            return QualityTier.B
        elif s >= 25:
            return QualityTier.C
        return QualityTier.D

    @staticmethod
    def _generate_recommendation(qa: QualityAssessment) -> str:
        """Generate a human-readable recommendation."""
        if qa.quality_tier == QualityTier.A:
            return "Strong citation candidate. Well-cited, peer-reviewed."
        elif qa.quality_tier == QualityTier.B:
            return "Good citation candidate. Verify relevance to your specific claim."
        elif qa.quality_tier == QualityTier.C:
            if qa.is_preprint:
                return "Preprint — cite with caution. Check if a peer-reviewed version exists."
            return "Marginal citation. Consider finding stronger alternatives."
        return "Weak citation. Avoid unless no better source exists."

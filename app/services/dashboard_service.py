from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository
from app.schemas.dashboard import DashboardResponse


class DashboardService:

    @staticmethod
    def dashboard(
        db: Session
    ) -> DashboardResponse:

        istatistikler = DashboardRepository.tum_istatistikleri_getir(db)
        return DashboardResponse(**istatistikler)
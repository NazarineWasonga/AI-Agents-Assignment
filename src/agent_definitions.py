class QualityControlAgent:
    """
    Monitors production quality, detects defects, and triggers alerts.
    """
    def __init__(self, defect_threshold=0.05):
        self.defect_threshold = defect_threshold

    def analyze_batch(self, defect_rate):
        if defect_rate > self.defect_threshold:
            return "Alert: High defect rate detected"
        return "Batch within acceptable quality"


class MaintenanceAgent:
    """
    Predicts machine downtime and schedules preventive maintenance.
    """
    def predict_downtime(self, sensor_data):
        # Simplified example: downtime if sensor > threshold
        if max(sensor_data) > 80:
            return "Maintenance Required"
        return "Machine OK"


class ProductionSchedulingAgent:
    """
    Optimizes production schedules based on demand, labor availability, and machine status.
    """
    def optimize_schedule(self, demand, labor_available, machine_status):
        if machine_status != "Machine OK":
            return "Reschedule production"
        return f"Schedule production for {demand} units with {labor_available} workers"

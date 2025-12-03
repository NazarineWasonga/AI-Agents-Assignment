from agent_definitions import QualityControlAgent, MaintenanceAgent, ProductionSchedulingAgent

# Sample production data
sample_defect_rate = 0.15
sample_sensor_data = [60, 55, 82, 70]
demand = 500
labor_available = 12

# Initialize agents
qc_agent = QualityControlAgent()
maintenance_agent = MaintenanceAgent()
scheduler_agent = ProductionSchedulingAgent()

# Run simulation
print("=== Quality Control ===")
print(qc_agent.analyze_batch(sample_defect_rate))

print("\n=== Maintenance Prediction ===")
print(maintenance_agent.predict_downtime(sample_sensor_data))

print("\n=== Production Scheduling ===")
machine_status = maintenance_agent.predict_downtime(sample_sensor_data)
print(scheduler_agent.optimize_schedule(demand, labor_available, machine_status))

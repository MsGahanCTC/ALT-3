# ----------------------------------------------------------------------
# SIMULATION AND MODELLING ACTIVITY: BALL TRAJECTORY PREDICTOR
# ----------------------------------------------------------------------

# This model predicts how far a ball will travel horizontally when launched.

import math # We need this to use mathematical functions like sin() and radians()

# --- STEP 1: DEFINE THE PROBLEM ---
# Problem: We want to calculate the maximum horizontal distance (Range) a ball
# travels before landing, based on its launch speed and angle.

# --- STEP 2: IDENTIFY KEY VARIABLES AND PARAMETERS ---

# PARAMETERS (Constants of the system - fixed for all runs):
# Acceleration due to gravity (g) in meters per second squared.
# This value defines the physics of the environment.
GRAVITY_G = 9.81

# INPUT VARIABLES (Scenario data - defined later):
# 1. Initial Launch Velocity (speed)
# 2. Launch Angle (in degrees)

# --- STEP 3: BUILD THE MODEL (The core logic/formula) ---

def calculate_range(initial_velocity_m_s: float, launch_angle_degrees: float) -> float:
    """
    This function represents our MODEL. It applies the projectile motion formula
    to calculate the horizontal range (R) in metres.

    The model uses the formula: R = (v^2 * sin(2*theta)) / g

    Args:
        initial_velocity_m_s: The speed (m/s) at which the ball is launched.
        launch_angle_degrees: The angle (degrees) relative to the ground.

    Returns:
        The maximum horizontal distance traveled (Range) in metres.
    """
    # 3.1 Convert the angle from degrees (easy for humans) to radians (needed for Python's math)
    angle_radians = math.radians(launch_angle_degrees)

    # 3.2 Calculate the numerator of the formula: v^2 * sin(2*theta)
    numerator = (initial_velocity_m_s ** 2) * math.sin(2 * angle_radians)

    # 3.3 Calculate the denominator
    denominator = GRAVITY_G

    # 3.4 The final model calculation
    range_m = numerator / denominator

    # We only want positive distances
    return max(0, range_m)

# --- STEP 4: EXPERIMENTATION (RUNNING SCENARIOS AND COLLECTING RESULTS) ---

# Define a list of SCENARIOS (different inputs to test the model's behaviour)
scenarios = [
    {"name": "Scenario A: High Speed, Low Angle", "velocity": 30.0, "angle": 25.0},
    {"name": "Scenario B: Max Range Angle (Ideal)", "velocity": 30.0, "angle": 45.0},
    {"name": "Scenario C: High Angle, Same Speed", "velocity": 30.0, "angle": 70.0},
    {"name": "Scenario D: Slower Speed Test", "velocity": 15.0, "angle": 45.0}
]

print("--- Projectile Simulation Setup ---")
print(f"Gravity (g): {GRAVITY_G} m/s² (Fixed Parameter)")
print("-" * 50)
print("RUNNING EXPERIMENT SCENARIOS...")
print("-" * 50)

# Run the simulation for each defined scenario
for scenario in scenarios:
    name = scenario["name"]
    velocity = scenario["velocity"]
    angle = scenario["angle"]

    # 4.1. Run the Model (The Simulation Step)
    # We pass the input variables (velocity and angle) to the model function.
    range_result = calculate_range(velocity, angle)

    # 4.2. Output the Data (Collect Results)
    print(f"| {name:<30} | V: {velocity:<4} m/s | Angle: {angle:<3}° | Range: {range_result:.2f} metres |")

print("-" * 50)
print("Simulation Experiment Complete. Results collected.")

# --- STEP 5: INTERPRETATION (Discussion points for the class) ---
# 1. Compare Scenarios A, B, and C. Which angle gives the longest range, and why?
# 2. Compare Scenarios B and D. How does cutting the initial velocity in half affect the range?
# 3. How would you modify the model (the code) if we were simulating this on the Moon (where gravity is about 1.62 m/s²)?

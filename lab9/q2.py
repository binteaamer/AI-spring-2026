#task 2

!pip install pgmpy 

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define structure
model = BayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Step 2: Define CPDs
cpd_i = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.7], [0.3]])
cpd_s = TabularCPD(variable='StudyHours', variable_card=2, values=[[0.6], [0.4]])
cpd_d = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.4], [0.6]])

# Intelligence: 0=High, 1=Low; StudyHours: 0=Sufficient, 1=Insufficient; Difficulty: 0=Hard, 1=Easy
cpd_g = TabularCPD(
    variable='Grade', variable_card=3, 
    values=[[0.7, 0.9, 0.4, 0.6, 0.3, 0.5, 0.1, 0.2],  # Grade A
            [0.2, 0.08, 0.4, 0.3, 0.4, 0.3, 0.4, 0.4], # Grade B
            [0.1, 0.02, 0.2, 0.1, 0.3, 0.2, 0.5, 0.4]], # Grade C
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

cpd_p = TabularCPD(
    variable='Pass', variable_card=2,
    values=[[0.95, 0.80, 0.50],  # Pass = Yes
            [0.05, 0.20, 0.50]], # Pass = No
    evidence=['Grade'], evidence_card=[3]
)

# Step 3: Add CPDs and perform inference
model.add_cpds(cpd_i, cpd_s, cpd_d, cpd_g, cpd_p)
inference = VariableElimination(model)

# Task: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
q1 = inference.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
print("Probability student passes (Study=Sufficient, Difficulty=Hard):")
print(q1)

# Task: P(Intelligence | Pass=Yes)
q2 = inference.query(variables=['Intelligence'], evidence={'Pass': 0})
print("\nProbability of High Intelligence given Pass=Yes:")
print(q2)



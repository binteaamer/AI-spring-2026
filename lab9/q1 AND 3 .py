Task 1: Probability with CardsTask 1: Probability with Cards

Probability of drawing a red card:
Total cards = 52
Red cards (Hearts + Diamonds) = 26
P(Red) = 26/52 = 1/2

Given that a red card is drawn, probability it is a heart:
Hearts = 13
Total red cards = 26
P(Heart | Red) = 13/26 = 1/2

Given that the card is a face card, probability it is a diamond:
Face cards = 12 (Jack, Queen, King of 4 suits)
Diamond face cards = 3 (J, Q, K of Diamonds)
P(Diamond | Face) = 3/12 = 1/4

Given that the card is a face card, probability it is a spade or a queen:
Spade face cards (J, Q, K of Spades) = 3
Queens = 4 (Spades, Hearts, Diamonds, Clubs)
Overlap (Queen of Spades) = 1
P(Spade ∪ Queen | Face) = (3 + 4 - 1)/12 = 6/12 = 1/2

Task 3: Disease Bayesian Network
Given Probabilities from Manual:

P(Flu) = 0.3, P(Cold) = 0.7

P(Fever|Flu) = 0.9, P(Fever|Cold) = 0.5

P(Cough|Flu) = 0.8, P(Cough|Cold) = 0.6

P(Chills|Flu) = 0.6, P(Chills|Cold) = 0.4

P(Fatigue|Flu) = 0.7, P(Fatigue|Cold) = 0.3

Task 1: Calculate P(Flu | Fever=Yes, Cough=Yes)
Using Bayes Rule (Proportionality):

P(Flu) × P(Fever|Flu) × P(Cough|Flu) = 0.3 × 0.9 × 0.8 = 0.216

P(Cold) × P(Fever|Cold) × P(Cough|Cold) = 0.7 × 0.5 × 0.6 = 0.21
Normalize:
P(Flu | Fever, Cough) = 0.216 / (0.216 + 0.21) = 0.216 / 0.426 ≈ 0.507

Task 2: Calculate P(Flu | Fever=Yes, Cough=Yes, Chills=Yes)
Using Bayes Rule (Proportionality):

P(Flu) × P(Fever|Flu) × P(Cough|Flu) × P(Chills|Flu) = 0.3 × 0.9 × 0.8 × 0.6 = 0.1296

P(Cold) × P(Fever|Cold) × P(Cough|Cold) × P(Chills|Cold) = 0.7 × 0.5 × 0.6 × 0.4 = 0.084
Normalize:
P(Flu | Fever, Cough, Chills) = 0.1296 / (0.1296 + 0.084) = 0.1296 / 0.2136 ≈ 0.607

Task 3: Calculate P(Fatigue = Yes | Disease = Flu)
From the given Conditional Probability Table (CPT):
P(Fatigue = Yes | Disease = Flu) = 0.7

Explanation:
This value is a direct entry in the CPT. Since the evidence specifies the parent node (Disease = Flu) is known with certainty, the probability of the child node (Fatigue) is simply the corresponding value in the table, requiring no further Bayesian normalization.

Probability of drawing a red card:
Total cards = 52
Red cards (Hearts + Diamonds) = 26
P(Red) = 26/52 = 1/2

Given that a red card is drawn, probability it is a heart:
Hearts = 13
Total red cards = 26
P(Heart | Red) = 13/26 = 1/2

Given that the card is a face card, probability it is a diamond:
Face cards = 12 (Jack, Queen, King of 4 suits)
Diamond face cards = 3 (J, Q, K of Diamonds)
P(Diamond | Face) = 3/12 = 1/4

Given that the card is a face card, probability it is a spade or a queen:
Spade face cards (J, Q, K of Spades) = 3
Queens = 4 (Spades, Hearts, Diamonds, Clubs)
Overlap (Queen of Spades) = 1
P(Spade ∪ Queen | Face) = (3 + 4 - 1)/12 = 6/12 = 1/2

Task 3: Disease Bayesian Network
Given Probabilities from Manual:

P(Flu) = 0.3, P(Cold) = 0.7

P(Fever|Flu) = 0.9, P(Fever|Cold) = 0.5

P(Cough|Flu) = 0.8, P(Cough|Cold) = 0.6

P(Chills|Flu) = 0.6, P(Chills|Cold) = 0.4

P(Fatigue|Flu) = 0.7, P(Fatigue|Cold) = 0.3

Task 1: Calculate P(Flu | Fever=Yes, Cough=Yes)
Using Bayes Rule (Proportionality):

P(Flu) × P(Fever|Flu) × P(Cough|Flu) = 0.3 × 0.9 × 0.8 = 0.216

P(Cold) × P(Fever|Cold) × P(Cough|Cold) = 0.7 × 0.5 × 0.6 = 0.21
Normalize:
P(Flu | Fever, Cough) = 0.216 / (0.216 + 0.21) = 0.216 / 0.426 ≈ 0.507

Task 2: Calculate P(Flu | Fever=Yes, Cough=Yes, Chills=Yes)
Using Bayes Rule (Proportionality):

P(Flu) × P(Fever|Flu) × P(Cough|Flu) × P(Chills|Flu) = 0.3 × 0.9 × 0.8 × 0.6 = 0.1296

P(Cold) × P(Fever|Cold) × P(Cough|Cold) × P(Chills|Cold) = 0.7 × 0.5 × 0.6 × 0.4 = 0.084
Normalize:
P(Flu | Fever, Cough, Chills) = 0.1296 / (0.1296 + 0.084) = 0.1296 / 0.2136 ≈ 0.607

Task 3: Calculate P(Fatigue = Yes | Disease = Flu)
From the given Conditional Probability Table (CPT):
P(Fatigue = Yes | Disease = Flu) = 0.7

Explanation:
This value is a direct entry in the CPT. Since the evidence specifies the parent node (Disease = Flu) is known with certainty, the probability of the child node (Fatigue) is simply the corresponding value in the table, requiring no further Bayesian normalization.

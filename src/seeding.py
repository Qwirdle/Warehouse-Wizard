from src.models import db, User, Item
import uuid
from random import choice

def generateCredentials(count, username_prefix='user'):
    credentials = []
    for _ in range(count):
        uid = uuid.uuid4().hex  # 32-char hex string
        username = f"{username_prefix}_{uid[:8]}"  # e.g., user_1a2b3c4d
        password = uuid.uuid4().hex  # 32-char unique password
        credentials.append((username, password))
    return credentials

class Seeder:

    def __init__(self):
        
        # Chemical name and descriptors
        self.chemicals = [
            ["Sodium Chloride", "Table salt, used in food and chemical processing."],
            ["Ethanol", "Alcohol used in sanitizers, solvents, and fuel."],
            ["Acetic Acid", "Main component of vinegar, used in food and cleaning."],
            ["Hydrochloric Acid", "Strong acid used in cleaning, digestion, and industry."],
            ["Sodium Bicarbonate", "Baking soda, used in cooking and pH regulation."],
            ["Sulfuric Acid", "Highly corrosive acid used in batteries and manufacturing."],
            ["Ammonia", "Pungent gas used in cleaning and fertilizers."],
            ["Methanol", "Wood alcohol, used as a solvent and antifreeze."],
            ["Calcium Carbonate", "Used in antacids and chalk; found in limestone."],
            ["Potassium Nitrate", "Used in fertilizers, food preservation, and explosives."],
            ["Glucose", "Simple sugar essential for energy in cells."],
            ["Citric Acid", "Naturally found in citrus fruits, used as a preservative."],
            ["Sodium Hydroxide", "Lye; strong base used in soap and drain cleaners."],
            ["Magnesium Sulfate", "Epsom salt; used in baths and as a laxative."],
            ["Acetone", "Solvent commonly used in nail polish remover."],
            ["Formaldehyde", "Used in embalming and disinfectants."],
            ["Benzene", "Aromatic hydrocarbon used in plastic and fuel production."],
            ["Toluene", "Solvent used in paint thinners and adhesives."],
            ["Chloroform", "Used historically as an anesthetic; now mostly phased out."],
            ["Isopropyl Alcohol", "Rubbing alcohol used for disinfection."],
            ["Hydrogen Peroxide", "Used as a bleach and antiseptic."],
            ["Calcium Hypochlorite", "Used in disinfecting drinking water and pools."],
            ["Sodium Thiosulfate", "Used in photography and dechlorination."],
            ["Nitric Acid", "Used in fertilizer and explosives manufacturing."],
            ["Phosphoric Acid", "Used in soft drinks and rust removal."],
            ["Zinc Oxide", "Used in sunscreens and ointments."],
            ["Copper Sulfate", "Blue crystalline chemical used in agriculture."],
            ["Sodium Carbonate", "Washing soda; used in glass and soap making."],
            ["Aluminum Hydroxide", "Used as an antacid and in water purification."],
            ["Lactic Acid", "Found in sour milk; used in cosmetics and food."],
            ["Ascorbic Acid", "Vitamin C; antioxidant used in food and supplements."],
            ["Salicylic Acid", "Used in acne treatments and skincare."],
            ["Glycerol", "Thick, sweet-tasting liquid used in cosmetics and food."],
            ["Calcium Chloride", "Used for de-icing roads and moisture absorption."],
            ["Sodium Nitrate", "Preservative and fertilizer."],
            ["Urea", "Used in fertilizers and skin creams."],
            ["Sodium Benzoate", "Preservative used in acidic foods and drinks."],
            ["Tartaric Acid", "Used in baking powders and wine production."],
            ["Sodium Citrate", "Used to control acidity in food and medicine."],
            ["Borax", "Cleaning agent and component of slime."],
            ["Potassium Permanganate", "Strong oxidizer used in water treatment."],
            ["Sodium Lauryl Sulfate", "Surfactant used in soaps and shampoos."],
            ["Silicon Dioxide", "Found in sand; used as an anti-caking agent."],
            ["Magnesium Hydroxide", "Milk of magnesia; used as an antacid."],
            ["Chromic Acid", "Used for cleaning glassware and etching."],
            ["Hexane", "Non-polar solvent used in extractions."],
            ["Butane", "Flammable gas used in lighters and fuels."],
            ["Propylene Glycol", "Humectant used in food and pharmaceuticals."],
            ["Boric Acid", "Mild antiseptic and insecticide."],
            ["Hydrofluoric Acid", "Very corrosive acid used in glass etching."],
            ["Ferric Chloride", "Used in water treatment and etching PCBs."]
        ]

        

    def getChem(self):
        info = choice(self.chemicals)
        return Item(name=info[0], description=info[1])

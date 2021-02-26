# check whether SuperRobot is a subclass of AstromechDroid,
# MedicalDroid, BattleDroid, and PilotDroid

# the order is IMPORTANT
for t in (AstromechDroid, MedicalDroid, BattleDroid, PilotDroid):
    print(issubclass(SuperRobot, t))

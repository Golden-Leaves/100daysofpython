import random
def simulate_microcredit_effect(population,loan_amount,years):
    businesses_created = 0
    total_income = 0
    successful_repayments = 0
    
    def is_successful():
        return random.choice((True,False,False,True,True)) #0.65 success chance
    
    for year in range(1,years + 1):
        for villager in population:
            businesses_created += 1
            if is_successful():
                villager["income"] += loan_amount * 1.5#Assuming 50% ROI
                successful_repayments += 1
                
            else:
                villager["income"] -= loan_amount #Mf defaulted
            total_income += villager["income"]
    repayment_rate = successful_repayments / len(population) * 100
    avg_income = total_income / len(population)
    return repayment_rate,avg_income,businesses_created
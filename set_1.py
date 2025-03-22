# no 1
def savings(gross_pay, tax_rate, expenses):
	takehome_pay = int(gross_pay * tax_rate) - expenses
	
	return takehome_pay


# no 2
def material_waste(total_material, material_units, num_jobs, job_consumption):
	waste = total_material - num_jobs * job_consumption

	return f"{waste}{material_units}"


# no 3
def interest(principal, rate, periods):
  final_investment = int(principal + principal * rate * periods)
  
  return final_investment

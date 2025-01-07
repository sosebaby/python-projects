import statistics
class Temperature:
	"""to collect daily temperatures, compute mean,
	minimum, maximum, and standard deviation of temperatures."""
	def __init__(self):
		self.temperatures=[]
	def printTemperature(self):
		days=int(input("Enter the number of event days:\n"))
		for i in range(1,days+1):
			temp=int(input(f"Enter the maximum Temperature on day {i}"))
			self.temperatures.append(temp)
		print(f"Temperature values: ",self.temperatures)
	def calculateStatistics(self):
		if self.temperatures:
			mean=statistics.mean(self.temperatures)
			minimum=min(self.temperatures)
			maximum = max(self.temperatures)
			standarddeviation = statistics.stdev(self.temperatures) if len(self.temperatures)>1 else 0
			print("Temperature statistics:\n")
			print(f"Mean: {mean:.2f}")
			print(f"Minimum value: {minimum:.2f}")
			print(f"Maximum value: {maximum:.2f}")
			print(f"Standard deviation: {standarddeviation:.2f}")
		else:
			print("Please input a temperature")
temperature = Temperature()  
temperature.printTemperature()  
temperature.calculateStatistics() 

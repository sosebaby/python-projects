def myExpertSystem_areYouSad(car, food, movie):
    # Define the knowledge base of valid options
    valid_cars = ['tesla', 'toyota', 'honda']
    valid_food = ['pasta', 'burger', 'pizza']
    valid_movies = ['dune', 'venom']

    # Handle cases where any input is missing
    if not car.strip() or not food.strip() or not movie.strip():
        return "You are sad because of empty input."

    # Validate if the provided car is in the list
    if car.lower().strip() not in valid_cars:
        return "You are sad because of the car."

    # Validate if the provided food is in the list
    if food.lower().strip() not in valid_food:
        return "You are sad because of the food."

    # Validate if the provided movie is in the list
    if movie.lower().strip() not in valid_movies:
        return "You are sad because of the movie."

    # Return a positive response if all inputs are valid
    return "You are happy!"

# Test scenarios to verify the system
test1 = myExpertSystem_areYouSad('tesla', 'pasta', 'dune')  # Expected: happy response
test2 = myExpertSystem_areYouSad('tesla', 'pasta', ' ')     # Expected: sad due to missing movie
test3 = myExpertSystem_areYouSad('pizza', 'toyota ', 'dune')  # Expected: sad due to invalid car
test4 = myExpertSystem_areYouSad(' ', 'pizza', 'dune')      # Expected: sad due to missing car
test5 = myExpertSystem_areYouSad('kia', 'pizza', 'dune')    # Expected: sad due to invalid car

# Display the results for each test
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

# -*- coding: utf-8 -*-

# 운행하는 차를 정의합니다.
cars = 100
# 차량당 탑승할 수있는 승객수를 정의합니다.
#sapce_in_a_car = 4.0
# 부동소수점을 삭제한 차량당 승객수를 정의합니다.
sapce_in_a_car = 4
# 운전자를 정의합니다.
drivers = 30
# 함께 탈 사람을 정의합니다.
passengers = 90
# 빈 차를 정의합니다.
cars_not_driven = cars - drivers
# 운행가능한 운전자를 정의합니다.
cars_driven = drivers
# 차량당 탑승 가능 인원을 정의합니다.
carpool_capacity = cars_driven * sapce_in_a_car
# 운행할 차량에 탑승가능 한 평균 승객 수를 정의합니다.
average_passengers_per_car = passengers / cars_driven


print "자동차",cars, "대가 있읍니다."
print "운전자는",drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은",carpool_capacity, "명을 태울 수 있읍니다."
print "함께 탈 사람은", passengers, "명 있읍니다."
print "차마다", average_passengers_per_car,"명 정도씩 타야 합니다."

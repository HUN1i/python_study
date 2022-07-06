#PDF 10, 11
This_year = int(input ("올해의 년도를 4자리로 입력하세요 :"))
Birth_year = int(input ("당신이 태어난 년도를 4자리로 입력하세요 :"))
age = ((f"당신의 나이는 {This_year - Birth_year +1}입니다."))

print(f"{This_year}")
print(f"{Birth_year}")
print(f"{age}")

Max_weight = 600
object1 = float(input ("첫 번째 물건의 무게를 입력하세요 :"))
object2 = float(input ("두 번째 물건의 무게를 입력하세요 :"))
Current_weight = Max_weight - (object1 + object2)

print(f"{object1}")
print(f"{object2}")
print(f"현재 엘리베이터의 허용 무게는 {Current_weight}kg 입니다")

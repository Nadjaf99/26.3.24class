	
# Task5
# Funksiyalar yazılmalıdır!


# Maliyyə Sənayesi:
# Tapşırıq: Büdcə aləti yaradın
# Təsvir: Tələbələr aylıq xərclər və gəlirlər üçün daxil olan Python proqramı yaradacaqlar. Funksiya ümumi xərcləri, ümumi gəliri almalı və ayın qalan büdcəsini hesablamalıdır.






# def calculate_budget(expenses, income):
#     total_expenses = sum(expenses)
#     total_income = sum(income)
#     remaining_budget = total_income - total_expenses
#     return remaining_budget
# for x in range(12) :
#      expenses = [float(input("Xərclərinizi daxil edin: ")) ] 
#      income = [float(input("Gəlirlərinizi daxil edin: ")) ]   

#      remaining_budget = calculate_budget(expenses, income)
     
#      print("Qalan büdcə: ", remaining_budget)

# # print("Qalan büdcə: ", remaining_budget)

# calculate_budget(expenses,income)






# Səhiyyə Sənayesi:
# Tapşırıq: BMI Kalkulyatorunu tərtib edin.
# Təsvir: Python funksiyalarından istifadə edərək Bədən Kütləsi İndeksi (BMI) kalkulyatoru yaradın. İstifadəçilərdən parametr olaraq çəkilərini (kiloqramla) və boylarını (metrlə) daxil etmələri təklif edilməlidir və proqram BMI-ni hesablayıb çap etməlidir. Əlavə olaraq, istifadəçiyə BMI kateqoriyası (məsələn, az çəki, normal çəki, artıq çəki və ya piylənmə) haqqında rəy bildirin.


# def calculate_bmi(weight, height):

#     bmi = weight / (height ** 2)
#     return bmi

# def get_bmi_category(bmi):
#     if bmi < 18.5:
#         return "(Az çəki)"
#     elif 18.5 <= bmi < 25:
#         return "Normal (Sağlam çəki)"
#     elif 25 <= bmi < 30:
#         return "Artiq çəki (Obez)"
#     else:
#         return "Qeyri-adi çəki(piylenme) "

# def bmi_calculator():
#     weight = float(input("Kiloqram cinsində çəkini daxil edin: "))
#     height = float(input("Metrlərdə boyunuzu daxil edin: "))
    
#     bmi = calculate_bmi(weight, height)
#     bmi_category = get_bmi_category(bmi)
    
#     print("BMI-niz:", bmi)
#     print("BMI kateqoriyası:", bmi_category)

# bmi_calculator()


# # Təhsil Sənayesi:
# # Tapşırıq: Tələbə Qiymət Kalkulyatoru.
# # Təsvir: Müxtəlif fənlər üzrə topladıqları ballara əsasən tələbələrin qiymətlərini hesablamaq üçün proqram yaradın. İstifadəçidən hər bir fənn üzrə xalları daxil etməyi, orta qiyməti hesablamağı və onların fəaliyyəti haqqında rəy bildirməyi təklif edin (məsələn, məktub qiymətləri). Orta hesablamaq və qiyməti müəyyən etmək üçün funksiyalardan istifadə edin və qiymətləndirmə meyarları üçün if-else ifadələrini birləşdirin. Qeyd: Bu taskdan bütün biliklərinizi maksimum istifadə edin və məntiqli kod yazmağa çalışın


# def calculate_average_score(scores):
#     total = sum(scores)
#     count = len(scores)
#     if count == 0:
#         return 0
#     return total / count

# def evaluate_performance(average_score):
#     if average_score >= 90:
#         return "A"
#     elif 80 <= average_score < 90:
#         return "B"
#     elif 70 <= average_score < 80:
#         return "C"
#     elif 60 <= average_score < 70:
#         return "D"
#     elif 50 <= average_score < 60:
#         return "E"
#     else:
#         return "F"
      

# def student_grading_calculator():
#     subjects = ['Math', 'Physics', 'Chemistry']  

#     scores = []
#     for subject in subjects:
#         score = float(input(f"Enter the score for {subject}: "))
#         scores.append(score)

#     average_score = calculate_average_score(scores)
#     performance = evaluate_performance(average_score)

#     print("Average Score:", average_score)
#     print("Performance:", performance)

# student_grading_calculator()




# *******























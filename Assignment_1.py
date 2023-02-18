# Result Sheet
Student_name = input('My name is ')
print(Student_name)
# obtained marks in matric
English = float(input('Obtained Marks in English : '))
Urdu = float(input('Obtained Marks in Urdu : '))
Math = float(input('Obtained Marks in Math : '))
Biology = float(input('Obtained Marks in Biology : '))
Chemistry = float(input('Obtained Marks in Chemistry :') )
Physics = float(input('Obtained Marks in Physics : '))
Islamiyat = float(input('Obtained Marks in Islamiyat : '))
Pakstudies = float(input('Obtained Marks in Pak_studies : '))
Total_Obtained_Marks = (English + Urdu + Math + Biology + Chemistry + Physics + Islamiyat + Pakstudies)

print('Total Obtained Marks in Matric : ' , Total_Obtained_Marks)
# Percentage in matric
percentage = ((Total_Obtained_Marks/800)*100)
print('percentage = ' , percentage)

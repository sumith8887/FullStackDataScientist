import ast
class Patients:
    def check_disease(self,patients_list,search_disease):
        disease_list=[]
        for patient in patients_list:
            if patient.get("Disease") == search_disease:
                disease_list.append(patient.get("Name"))
        if disease_list:
            print(f"Patients with {search_disease}: {disease_list}")
        else:
            print(f"No patients found with {search_disease}.")

patients_obj=Patients()
patients_list=ast.literal_eval(input("Enter patient details(name,age,diesease) in key:value pairs in a list : "))
search_disease=input("Enter the disease to be searched : ")
patients_obj.check_disease(patients_list,search_disease)
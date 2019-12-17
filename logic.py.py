from nltk.corpus import stopwords
import re
import nltk


# creating funtion for which contains the stop words logic
def func(x, y):
    count = 0
    # while loop which acts as do while
    while True:
        string = input("Did u take a thyroid test:")  # asking questions to the user

        stop_words = set(stopwords.words())  # taking stopwords as set
        stop_words.remove('no')
        spl = re.findall(r"[\w']+",
                         string)  # findall means finding all the data and \w defines a each alphabets and numerics from 0-9 which eliminates the extra characters
        # print(spl)
        main_words = []
        # for loop which checking the stopwords and eliminates the stopwords
        for i in spl:
            if i not in stop_words:
                main_words.append(i)  # append means adding the at end of the list
        # print(main_words)
        l = "yes"  # string comparing
        k = "no"  # string for comparing
        # for loop running through the main_words list
        for i in range(0, len(main_words)):
            # if condition for whether the list elements is equal to string or not and returns x
            if main_words[i] == l:
                count += 1
                return x
        # for loop running through the main_words list
        for i in range(0, len(main_words)):
            # if condition for whether the list elements is equal to string or not and returns x,y
            if main_words[i] == k:
                count += 1
                return y
        # if the user enter un valid  information then we asks to dispaly  valid information

        else:
            print("please enter a valid information")
        if count == 0:
            continue

#function for treatements for hyper
def treathyper():
    print("Add these to your Diet':coffee,tea(without diary),egg whites,oats,honey,potatoes,mushrooms,green leafy vegetables,meat such as beef and lamb,whole grains,unsalted nuts and seeds.\n'Remove these foods in your Diet':fish,prawns,crabs,lobster,sushi,milk and dairy,cheese,egg yolks,Soy based foods,caffeine")
#function for treatments for hypo
def treathypo():
    print("Add these to your Diet':peas,asparagus,sesame seeds,tuna,cheese,eggs,milk,taking vitamin B-12 supplements,meat,fish,vegetables,fruits,gluten free grains,beverages.\n 'Remove these to your Diet:millet,highly processed foods like hot dogs, cakes, cookies, supplements,soy-based foods,coffee, green tea, and alcohol,peaches, pears and strawberries")
# taking the dictionary with only symptoms as keys
Hypo = {'Fatigue': '', 'Increased_sensitivity_to_cold': '', 'Constipation': '', 'Weight_gain': '',
        'Puffy_face': '', 'Hoarseness': '', 'Muscle_weakness': '', 'Elevated_blood_cholesterol_level': '',
        'Pain_stiffness': '', 'Thinning_hair': '', 'Depression': '', 'Enlarged_thyroid_gland': '', }
Hyper = {'anxiety': '', 'increased_appetite': '', 'fatigue': '', 'muscle weakness': '', 'difficulty_sleeping': '',
         'hair_loss': '', 'itching': '', 'nausea': '', 'weight_loss': '', 'sweating': '', 'bowel_movements': '',
         'Enlarged_thyroid_gland': '', }
Thyroid = {'report': ''}
# another dictionary for storing the report values which is very important to identifing the diseases
report = {'Serum_tsh': '', 'Serum_T3': '', 'Serum_T4': ''}
Thyroid['report'] = func('yes', 'no')  # calling the funtion
# if condition for taking report values if the user has taken the test report
if Thyroid['report'] == 'yes':
    report['Serum_T3'] = float(input("Please provide the Serum T3 value:"))
    report['Serum_T4'] = float(input("Please provide the Serum T4 value:"))
    report['Serum_Tsh'] = float(input("Please provide the Serum TSH value:"))
    if report['Serum_T3'] > 2.3 and report['Serum_T4'] > 12.0 and report['Serum_Tsh'] > 5.5:
        print("Your test results say, you have Hypothyroidism")
        treathypo()
    elif report['Serum_T3'] > 2.3 and report['Serum_T4'] > 12.0:
        print("Your test results say, you have Hypothyroidism")
        treathypo()
    elif report['Serum_T4'] > 12.0 and report['Serum_Tsh'] > 5.5:
        print("Your test results say, you have Hypothyroidism")
        treathypo()
    elif report['Serum_Tsh'] > 5.5 and report['Serum_T3'] > 2.3:
        print("Your test results say, you have Hypothyroidism")
        treathypo()
    elif report['Serum_Tsh'] > 5.5:
        print("You have Hypothyroidism")
        treathypo()
    elif report['Serum_T3'] < 0.8 and report['Serum_T4'] < 4.8 and report['Serum_Tsh'] < 0.35:
        print("Your test results say, you have Hyperthyroidism")
        treathyper()
    elif report['Serum_T3'] < 0.8 and report['Serum_T4'] < 4.8:
        print("Your test results say, you have Hyperthyroidism")
        treathyper()
    elif report['Serum_T4'] < 4.8 and report['Serum_Tsh'] < 0.35:
        print("Your test results say, you have Hyperthyroidism")
        treathyper()
    elif report['Serum_Tsh'] < 0.35 and report['Serum_T3'] < 0.8:
        print("Your test results say, you have Hyperthyroidism")
        treathyper()
    elif report['Serum_Tsh'] < 0.35:
        print("You have Hyperthyroidism")
        treathyper()


# conditon for identifing the disease by identifing the symptoms
if Thyroid['report'] == 'no':
    Hypo['Fatigue'] = input(
        "These days do you feel fatigue easily:").lower()  # .lower to convert the user input to lower case alphabets and input value is assinged to dictionary
    Hypo['Increased_sensitivity_to_cold'] = input("Do you feel extreme sensitivity to cold:").lower()
    Hypo['Constipation'] = input("Do you get more constipation problems these days:").lower()
    Hypo['Weight_gain'] = input("Have you being putting on or gaining weight lately:").lower()
    Hypo['Puffy_face'] = input("Do you ever feel your face has been puffed up:").lower()
    Hypo['Hoarseness'] = input("Do you feel hoarseness(sounding rough) in your voice:").lower()
    Hypo['Muscle_weakness'] = input("Have you ever felt weakness in your muscles:").lower()
    Hypo['Pain_stiffness'] = input("Do you feel pain and swelling in your joints:").lower()
    Hypo['Thinning_hair'] = input("Do you have more hair fall:").lower()
    Hypo['Depression'] = input("Do you feel depressed lately:").lower()
    Hypo['Enlarged_thyroid_gland'] = input("Do you have a swelling at the base of the neck:").lower()
if (Hypo['Fatigue'] and Hypo['Weight_gain'] and Hypo['Enlarged_thyroid_gland'] and Hypo[
        'Increased_sensitivity_to_cold']) == 'yes' or (Hypo['Fatigue'] and Hypo['Weight_gain'] and Hypo['Enlarged_thyroid_gland'] and Hypo[
        'Increased_sensitivity_to_cold']) == 'y' :
        print("You might be suffering from Hypothyroidism")
        treathypo()
else:
    print("you do not seem to have hypothyroid ")
    print("checking for Hyper thyroidism")

    Hyper['anxiety'] = input("These days do you feel anxiety or irritation for everything:").lower()
    Hyper['increased_appetite'] = input("Lately have you felt that your appetite increased:").lower()
    Hyper['fatigue'] = input("Do you feel tired easily these days:").lower()
    Hyper['muscle_weakness'] = input("Have you ever felt weakness in your muscles:").lower()
    Hyper['difficulty_sleeping'] = input(
            "Lately do you experience any difficulties while sleeping or unable to sleep:").lower()
    Hyper['hair_loss'] = input("Do you feel that your hairfall increased lately:").lower()
    Hyper['itching'] = input("Have you experienced any problems like itching on your body:").lower()
    Hyper['nausea'] = input("Do you feel nausea(uneasiness in the stomach)and throws up(vomitings):").lower()
    Hyper['weight_loss'] = input(
            "Have you been experiencing weight loss suddenly even though your appetite increased: ").lower()
    Hyper['sweating'] = input(
            "Lately do you feel that your sweating increased more than before(unusual sweating): ").lower()
    Hyper['bowel_movements'] = input(
            "Do you have frequent and more bowel movements(loose,watery motions like in diarrhea): ").lower()
    Hyper['Enlarged_thyroid_gland'] = input("Do you have a swelling at the base of the neck:").lower()
if (Hyper['weight_loss'] and Hyper['sweating'] and Hyper['Enlarged_thyroid_gland'] and Hyper[
        'bowel_movements'] )== 'yes' or (Hyper['weight_loss'] and Hyper['sweating'] and Hyper['Enlarged_thyroid_gland'] and Hyper[
        'bowel_movements'] )== 'y':
        print("You might be suffering from Hyperthyroidism")
        treathyper()
else:
    print("you do not seem to have hyper thyroidism anyways we suggest you to consult a doctor for accurate results.")


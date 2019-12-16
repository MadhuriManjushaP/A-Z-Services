'''finding the diseases by identifing the symptoms'''
# string array
names = ["hoarseness", "swelling", "heavy breathing", "dizziness", "neck vein"]
name = input()
# for loop iterating the list
if name in names:
    # if condition satisfies then only enters into loop
    # for every symptom the process is same
    if name == 'Hoarseness' or name == 'hoarseness':
        print("When do you feel Hoarseness?")
        # taking  string input from the user
        a = input()
        print("Okay,Do you have any swelling over neck?")
        count = 0
        '''while loop which acts  like do while'''
        while True:
            b = input()
            if b == "yes" or b == "no" or b == "nope":
                print("Are you suffering from cough")
                count += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count == 0:
                continue
        count0 = 0
        while True:
            c = input()
            if c == "yes" or c == "no" or c == "nope":
                print("is there any dizziness when you raised your arms")
                count0 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count0 == 0:
                continue
        count1 = 0
        while True:
            d = input()
            if d == "yes" or d == "no" or d == "nope":
                print("Did you feel any neck vein")
                count1 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count1 == 0:
                continue
        count2 = 0
        while True:
            f = input()
            if f == "yes" or f == "no" or f == "nope":
                print("it seems you have goiter ,please consult doctor as soon as possible")
                count2 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count2 == 0:
                continue
    elif name == 'Swelling' or name == 'swelling':
        print("when did you start observing the change?")
        a = input()
        print("Okay,is there any dizziness when you raise your hand above the head?")
        count = 0
        while True:
            b = input()
            if b == "yes" or b == "no" or b == "nope":
                print("Did you observe any weight loss?")
                count += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count == 0:
                continue
        count0 = 0
        while True:
            c = input()
            if c == "yes" or c == "no" or c == "nope":
                print("is there heavy swetting?")
                count0 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count0 == 0:
                continue
        count1 = 0
        while True:
            d = input()
            if d == "yes" or d == "no" or d == "nope":
                print("Did you feel any neck vein")
                count1 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count1 == 0:
                continue
        count2 = 0
        while True:
            f = input()
            if f == "yes" or f == "no" or f == "nope":
                print("it seems you have goiter ,please consult doctor as soon as possible")
                count2 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count2 == 0:
                continue
    elif name == 'heavybreathing' or name == 'heavy breathing':
        print("Do you face difficulty in breathing only when running, walking or all the time?")
        a = input()
        print("Okay,Do you have any swelling over neck?")
        count = 0
        while True:
            b = input()
            if b == "yes" or b == "no" or b == "nope":
                print("is there any dizziness when you raised your arms above the head?")
                count += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count == 0:
                continue
        count0 = 0
        while True:
            print("Did you obseved any weight loss?")
            b = input()
            if b == "yes" or b == "no" or b == "nope":
                print("Did you obseved any weight loss?")

                count0 += 1
                break
            else:
                print("i don't understand plz enter again / Did you observed any weight loss")
            if count0 == 0:
                continue
        count1 = 0
        while True:
            c = input()
            if c == "yes" or c == "no" or c == "nope":
                print("did sweating is heavy?")
                count1 += 1
                break
            else:
                print("i don't understand plz enter again / Did you obseved any weight loss")
            if count1 == 0:
                continue

        count2 = 0
        while True:
            d = input()
            if d == "yes" or d == "no" or d == "nope":
                print("it seems you have goiter ,please consult doctor as soon as possible")
                count2 += 1
                break
            else:
                print("i don't understand plz enter again / did sweating is heaavy")
            if count2 == 0:
                continue
    elif name == "dizziness" or name == "Dizzinness":
        print("When do you feel dizzy?Only when you raise your arms or all the time?")
        a = input()
        print("okay,Do you have any swelling over neck?")
        count = 0
        while True:
            b = input()
            if b == "yes" or "no" or  "nope":
                print("Are you suffering from cough")
                count += 1
                break
            else:
                print("i don't understand plz enter again / Do you have any swelling over neck")
            if count == 0:
                continue
        count0 == 0

        while True:
            c = input()
            if c == "yes" or c == "no" or c == "nope":
                print("Did you observe any weight loss?")
                count0 += 1
                break
            else:
                print("i don't understand plz enter again / Are you suffering from cough ")
            if count0 == 0:
                continue
        count1 = 0
        while True:
            d = input()
            if d == "yes" or d == "no" or d == "nope":
                print("Did you feel any neck vein")
                count1 += 1
                break
            else:
                print("i don't understand plz enter again / Did you observe any weight loss")
            if count1 == 0:
                continue
        count2 = 0
        while True:
            f = input()
            if f == "yes" or f == "no" or f == "nope":
                print("it seems you have goiter ,please consult doctor as soon as possible")
                count2 += 1
                break
            else:
                print("i don't understand plz enter again / do you have any swelling over neck")
            if count2 == 0:
                continue
    elif name == 'neckvein' or name == 'neck vein':
        print("From how many days you are suffering from that?")
        a = input()
        print("Okay,Do you have any swelling over neck?")
        count = 0
        while True:
            b = input()
            if b == "yes" or b == "no" or b == "nope":
                print("did sweting is heavy?")
                count += 1
                break
            else:
                print("i don't understand plz enter again / Do you have any swelling over neck")
            if count == 0:
                continue
        count0 = 0
        while True:
            c = input()
            if c == "yes" or c == "no" or c == "nope":
                print("is there any dizziness when you raised your arms")
                count0 += 1
                break
            else:
                print("i don't understand plz enter again / did sweting is heavy")
            if count0 == 0:
                continue
        count1 = 0
        while True:
            d = input()
            if d == "yes" or d == "no" or d == "nope":
                print("did u have hoarsenss(husky/rough throat)")
                count1 += 1
                break
            else:
                print("i don't understand plz enter again / is there any dizziness when you raised your arms")
            if count1 == 0:
                continue
        count2 = 0
        while True:
            f = input()
            if f == "yes" or f == "no" or f == "nope":
                print("it seems you have goiter ,please consult doctor as soon as possible")
                count2 += 1
                break

            else:
                print("i don't understand plz enter again / did u have hoarsenss(husky/rough throat)")
            if count2 == 0:
                continue

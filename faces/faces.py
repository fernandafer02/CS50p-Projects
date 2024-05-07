
#promts user fpr input, calls convert, prints results
def main():
    emotion = input("How are you feeling today? ")
    emotion = emotion.replace(":)", "🙂").replace( ":(","🙁")
    print(emotion)



main()


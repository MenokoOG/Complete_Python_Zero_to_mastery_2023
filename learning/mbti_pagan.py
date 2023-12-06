"""A fun little project of taking MBTI personality type and then also listing the pagan type a person would be. L. Jefferson II, Menoko OG, 11/2023"""
#MBTI Personality Types
mbti_types = {
    "ISTJ" : "Inspector",
    "ISFJ" : "Protector",
    "INFJ" : "Counselor",
    "INTJ" : "Mastermind",    
    "ISTP" :"Craftsman",
    "ISFP" : "Composer",
    "INFP" : "Healer",
    "INTP" : "Architect",
    "ESTP" : "Dynamo",
    "ESFP" : "Performer",
    "ENFP" : "Champion",
    "ENTP" : "Inventor",
    "ESTJ" : "Supervisor",
    "ESFJ" : "Provider",
    "ENFJ" : "Teacher",
    "ENTJ" : "Commander"
    }

# Pagan Religion Personality Types
pagan_types = {
    "ISTJ" : "Astru",
    "ISFJ" : "Wiccan",
    "INFJ" : "Druid",
    "INTJ" : "Satanist",    
    "ISTP" :"Shaman",
    "ISFP" : "Buddhist",
    "INFP" : "Pantheist",
    "INTP" : "Deist",
    "ESTP" : "Agnostic",
    "ESFP" : "Atheist",
    "ENFP" : "New Age",
    "ENTP" : "Humanist",
    "ESTJ" : "Christian",
    "ESFJ" : "Muslim",
    "ENFJ" : "Jewish",
    "ENTJ" : "Hindu"
}
if __name__ == "__main__":
    
# function to print MBTI and pagan types based on input
    def print_personality_types():
        """function to print MBTI and pagan types based on input"""
        user_type = input("What is your MBTI type? ")
        mbti_type = user_type.upper()
        if mbti_type in mbti_types:
            print(f"Your MBTI types is {mbti_types[mbti_type]}.")
        
            print(f"Your pagan type is {pagan_types[mbti_type]}.")
        elif mbti_type not in mbti_types:
            print("Invalid MBTI type entered.")
        
print_personality_types()

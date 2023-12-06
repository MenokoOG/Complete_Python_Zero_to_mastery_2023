"""conditional exercise by L. Jefferson II, Menoko OG 11/2023"""
is_magician = True
is_expert = False

#check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")
    #check if magician but not expert: "at least you are getting there."
elif is_magician and not is_expert:
    print("at least you are getting there.")
# If you're not a magician: "You need magic powers."
# else: or you can use the line below becasue it does not matter if expert, if no magic then can not be expert either.
elif not is_magician:
    print("You need magic powers.")
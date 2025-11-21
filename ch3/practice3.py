# practice set3
# Que1->program to display a user entered name followed by Good Afternoon usuing input() function 
name=input("Enter your name:")
print(f"Good Afternoon {name}")#F string
# Que2->porgram to fill in a letter template with name and date
letter='''
Dear <|name|>
YOu are selected
<|Date|>'''
print(letter.replace("<|name|>","mayuri").replace("<|Date|>","22/12//2025"))

# Que3->detect doubble space in a string and replace it with single space
st="hello good  morning"
print(st.find("  "))
print(st.replace("  "," "))

# Que4->use escale characters
letter="hello dear mayuri,\nThis python course is nice.\nThank!"
print(letter)
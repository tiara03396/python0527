全班學生=set(["john","mary","tina","fiona","claire","eva","ben","bill","bert"])
英文及格=set(["john","mary","fiona","ben","bill","claire"])
數學及格=set(["mary","fiona","claire","eva","ben"])
print("英文及數學都及格"+str(英文及格&數學及格))
print("數學不及格"+str(全班學生-數學及格))
print("英文及格且數學不及格"+str(英文及格&全班學生-數學及格))


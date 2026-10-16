color = input("Enter colour :")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
        
    case _:
        print("DEFAULT /Wrong")
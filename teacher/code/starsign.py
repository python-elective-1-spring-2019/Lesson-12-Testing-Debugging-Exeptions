def starsign(month, day):
    if month == 1:
        if day <= 20:
            return "Capricorn"
        else:
            return "Aquarius"

    elif month == 5:
        if day <= 21:
            return "Taurus"
        else:
            return "Gemini"
    else:
        if day <= 21:
            return "Sagittarius"
        else:
            return "Capricorn"

starsign(1, 6)

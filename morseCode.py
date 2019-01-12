def toMorse(text):
    symbolsToMorse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", " ":"/", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", ".":".-.-.-", ",":"--..--", "?":"..--..", "-":"-....-", "=":"-...-", ":":"---...", ";":"-.-.-.", "(":"-.--.", ")":"-.--.-", "/":"-..-.", '"':".-..-.", "$":"...-..-", "'":".----.", "_":"..--.-", "@":".--.-.", "!":"---.", "+":".-.-.", "~":".-...", "#":"...-.-"}
    result = ""
    for x in text:
        try:
            result += symbolsToMorse[x] + " "
        except:
            result += x + " "
    return result

def fromMorse(symbols):
    morseToSymbols = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", "/":" ", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", ".-.-.-":".", "--..--":",", "..--..":"?", "-....-":"-", "-...-":"=", "---...":":", "-.-.-.":";", "-.--.":"(", "-.--.-":")", "-..-.":"/", ".-..-.":'"', "...-..-":"$", ".----.":"'", "..--.-":"_", ".--.-.":"@", "---.":"!", "-.-.--":"!", ".-.-.":"+", ".-...":"~", "...-.-":"#"}
    result = ""
    for x in symbols.split(" "):
        try:
            result += morseToSymbols[x]
        except:
            result += x
    return result
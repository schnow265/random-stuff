import pyqrcode
print("Gib deine URL ein!")
print("Das Bild wird als pygrcode.png gesichert!")
url = pyqrcode.create(input())
print(url.png("pyqrcode.png"))
print("QR-Code wurde erstellt, und liegt im Ordner, wo du die App installiert hast.")

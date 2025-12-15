import qrcode

myqr = qrcode.make("https://doc.squareyards.com/ProjectKnowledge/Brochure_d2e6c3b286b04e26990c087fc308567c.pdf")

myqr.save("myqr.png", scale = 8)


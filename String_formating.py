adresy = "SJM Sojka Vlastimil Ing. a Sojková Lenka PhDr. Ing. PhD., Křižíkova 231/62, Liberec IX-Janův Důl, 46007 Liberec	"

print(adresy.split(",", 1)[0])
adresa = adresy.split(",", 1)[1]
print(adresa.lstrip())

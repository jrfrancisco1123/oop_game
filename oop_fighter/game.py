from classes.guile import Guile
from classes.bison import Bison

guile = Guile("Guile")
m_bison = Bison("M. Bison")

# m_bison.show_stats()
# guile.show_stats()

m_bison.normal_attack(guile)
guile.flash_kick(m_bison)
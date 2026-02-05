import math


ascii_0p = """

....................
............................
.................................
..................................
.................................
............................
………...........


"""

   
ascii_3p = """ 

               . . . . . . . . . . .\n
          . . . . . . . . . . . . . . . . .\n
         . . . . . . . . . . . . . . . . . : #\n
        . . . . . . . . . . . . . . . . . . . :\n
         . . . . . . . . . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . . .\n
               . . . . . . . . . . .\n

   
"""

ascii_6p = """

               . . . . . . . . . . : \n
          . . . . . . . . . . . . . . . : #\n
         . . . . . . . . . . . . . . . . . : #\n
        . . . . . . . . . . . . . . . . . . : #\n
         . . . . . . . . . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . : #\n
               . . . . . . . . . . : \n


"""

ascii_9p = """

               . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . : #\n
         . . . . . . . . . . . . . . . . . : #\n
        . . . . . . . . . . . . . . . . . : # #\n
         . . . . . . . . . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . : #\n
               . . . . . . . . . : #\n


"""

ascii_12p = """

               . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . # #\n
         . . . . . . . . . . . . . . . . . # #\n
        . . . . . . . . . . . . . . . . . : # #\n
         . . . . . . . . . . . . . . . . . # #\n
          . . . . . . . . . . . . . . . : #\n
               . . . . . . . . . : #\n


"""

ascii_15p = """

               . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . # #\n
         . . . . . . . . . . . . . . . . . # #\n
        . . . . . . . . . . . . . . . . : # # @\n
         . . . . . . . . . . . . . . . . . # #\n
          . . . . . . . . . . . . . . . : #\n
               . . . . . . . . . : #\n


"""

ascii_18p = """

               . . . . . . . . . : #\n
          . . . . . . . . . . . . . . . # #\n
         . . . . . . . . . . . . . . . . . # @\n
        . . . . . . . . . . . . . . . . : # # @\n
         . . . . . . . . . . . . . . . . . # @\n
          . . . . . . . . . . . . . . . : #\n
               . . . . . . . . . : #\n


"""

ascii_21p = """

               . . . . . . . . : # #\n
          . . . . . . . . . . . . . . . # @\n
         . . . . . . . . . . . . . . . . . # @\n
        . . . . . . . . . . . . . . . . : # # @\n
         . . . . . . . . . . . . . . . . . # @\n
          . . . . . . . . . . . . . . . # @\n
               . . . . . . . . : # #\n


"""

ascii_24p = """

               . . . . . . . : # # @\n
          . . . . . . . . . . . . . . # # @\n
         . . . . . . . . . . . . . . . . # # @\n
        . . . . . . . . . . . . . . . : # # @ @\n
         . . . . . . . . . . . . . . . . # # @\n
          . . . . . . . . . . . . . . # # @\n
               . . . . . . . : # # @\n


"""

ascii_27p = """

               . . . . . . . : # # @\n
          . . . . . . . . . . . . . . # # @\n
         . . . . . . . . . . . . . . . . # # @\n
        . . . . . . . . . . . . . . . : # # @ @\n
         . . . . . . . . . . . . . . . . # # @\n
          . . . . . . . . . . . . . . # # @\n
               . . . . . . . : # # @\n


"""

ascii_30p = """
~30% : ascii a faire

"""

ascii_33p = """
~33% : ascii a faire

"""

ascii_36p = """
~36% : ascii a faire

"""

ascii_39p = """
~39% : ascii a faire

"""

ascii_42p = """
~42% : ascii a faire

"""

ascii_45p = """
~45% : ascii a faire

"""

ascii_48p = """
~48% : ascii a faire

"""
ascii_51p = """
~51% : ascii a faire

"""

ascii_54p = """
~54% : ascii a faire

"""

ascii_57p = """
~57% : ascii a faire

"""

ascii_60p = """
~60% : ascii a faire

"""

ascii_63p = """
~63% : ascii a faire

"""

ascii_66p = """
~66% : ascii a faire

"""

ascii_69p = """
~69% : ascii a faire

"""

ascii_72p = """
~72% : ascii a faire

"""

ascii_75p = """
~75% : ascii a faire

"""

ascii_78p = """
~78% : ascii a faire

"""

ascii_81p = """
~81% : ascii a faire

"""

ascii_84p = """
~84% : ascii a faire

"""

ascii_87p = """

          ##@@@@@@            
        ...:###@@@@@@         
       ...:###@@@@@@@@        
      ...:###@@@@@@@@@@       
       ...:###@@@@@@@@        
        ...:###@@@@@@         
          ##@@@@@@            

            
"""

ascii_90p = """
~90% : ascii a faire

"""

ascii_93p = """
~93% : ascii a faire

"""

ascii_96p = """
~96% : ascii a faire

"""

ascii_99p = """
~99% : ascii a faire

"""

ascii_100p = """
~100% : ascii a faire

"""

lunes_phases = [
        ascii_0p,
        ascii_3p,
        ascii_6p,
        ascii_9p,
        ascii_12p,
        ascii_15p,
        ascii_18p,
        ascii_21p,
        ascii_24p,
        ascii_27p,
        ascii_30p,
        ascii_33p,
        ascii_36p,
        ascii_39p,
        ascii_42p,
        ascii_45p,
        ascii_48p,
        ascii_51p,
        ascii_54p,
        ascii_57p,
        ascii_60p,
        ascii_63p,
        ascii_66p,
        ascii_69p,
        ascii_72p,
        ascii_75p,
        ascii_78p,
        ascii_81p,
        ascii_84p,
        ascii_87p,
        ascii_90p,
        ascii_93p,
        ascii_96p,
        ascii_99p,
        ascii_100p,

]


def miroir_ascii(ascii_art):
    lignes = ascii_art.splitlines()
    lignes_miroir = [ligne[::-1] for ligne in lignes]
    return "\n".join(lignes_miroir)


def lune(illumination, age_lune, cycle=29.53058867):
    index = int(illumination // 3)
    index = max(0, min(index, len(lunes_phases) - 1))

    ascii_lune = lunes_phases[index]

    #decroissance
    if age_lune > cycle / 2:
        ascii_lune = miroir_ascii(ascii_lune)

    return ascii_lune
